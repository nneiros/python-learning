import getopt
import os
import re
import string
import sys
import tempfile
#?????????????????????????????????????????????
from cgi import escape
import urllib2

try:
  from reportlab.lib.pagesizes import letter
  from reportlab.lib.styles import getSampleStyleSheet
  from reportlab.lib.units import inch
  from reportlab.platypus import (Paragraph, SimpleDocTemplate, Spacer,
                                  Preformatted)
except ImportError:
  print ('You need to install reportlab from http://www.reportlab.org/')
  sys.exit(-1)


# Defines how wide the margins should be.
MARGIN = 1.5 * inch

# Set printer options here. I usually use:
#   -o Duplex=DuplexNoTumble -o InputSlot=Tray2
# This duplexes jobs and uses the second tray.
# Make this be "" if there are none.
PRINTER_OPT = "-o Duplex=DuplexNoTumble -o InputSlot=Tray2"

# URL where RFCs are stored. Used to allow printing by number.
RFC_URL = 'http://tools.ietf.org/rfc/rfc'


class mySimpleDocTemplate(SimpleDocTemplate):
  pass

  def handle_pageBegin(self):
    """Move the frame right on even pages so that when we duplex the left
    margin becomes the right."""
    # When we print a job in duplex (and use DuplexNoTumble to lpr), the
    # printer flips the page. If we keep the margin on the left and then
    # punch a fole, we will go through the text (the left becomes the
    # right). This shifts the entire frame right to fix this. In theory there
    # are better ways of doing this, but it seems to go odd with
    # SimpleDocTemplate and Preformatted (page feeds are ignored)
    SimpleDocTemplate.handle_pageBegin(self)
    if self.pageTemplates[0].frames[0]._leftPadding !=6:
      self.pageTemplates[0].frames[0]._leftPadding = 6
    else:
      self.pageTemplates[0].frames[0]._leftPadding = -MARGIN/2

def myLaterPages(canvas, doc):
  """ Put stuff here if you want it on all (non-first) pages."""
  pass
  # Example:
  #canvas.line (66,72,22,33)

def usage():
  print """
  This script prints an Internet Draft (or RFC). It does this by
  reading the file (possibly first fetching it from the Internet),
  converting it to a PDF (and doing basic munging on it and then
  sending the PDF to lpr to actually do the printing.

  Usage:
        -F, --file <filename>  -- print this local file.
        -N, --number           -- prints this RFC number (e.g: 1998)
        -O, --outdir <dir>     -- save the converted PDF in this dir.
        -h, --help             -- this help.
        <url>                  -- fetch (and print) the file at the URL.
  Example:
      %(name)s  http://tools.ietf.org/rfc/rfc5635.txt
         Fetches and prints RFC5635 from the ietf.org site and prints it.

      %(name)s -F ~wkumari/docs/IETF/MyDrafts/deprecate-as-sets-00.txt
         Prints the local file called deprecate-as-sets-00.txt.
      """ % {'name' : sys.argv[0]}
  sys.exit()

if __name__ == "__main__":
  if len(sys.argv) < 2:
      usage()
  else:
      filename = ''
      outdir = ''
      url = ''
      rfc_number = ''
      options, remainder = getopt.gnu_getopt(sys.argv[1:], 'F:N:O:h',
                                             ['file=',
                                              'number=',
                                              'outdir=',
                                              'help',
                                              ])
      for opt, arg in options:
        if opt in ('-F', '--file'):
          filename = arg
        elif opt in ('-N', '--number'):
          rfc_number = arg
        elif opt in ('-O', '--outdir'):
          outdir = arg
        elif opt in ('-h', '--help'):
          usage()

      # TEST:
      if remainder:
        url = remainder[0]
      # Add up the number of options and make sure there is only 1.
      if sum(map(lambda x: 1 if x else 0, (filename, rfc_number, url))) != 1:
        print 'ERROR: Must supply 1 (and only 1) of filename, number or URL.\n'
        usage()

      if filename:
        # Local file.
        if '://' in filename:
          print '%s appears to be a URL. Please check and retry.' % filename
        try:
          text = open(filename).read()
        except IOError, e:
          print "Unable to open and read %s (%s)" % (filename, e)
          sys.exit()
        filename = re.search ('^.*/(.*)\.txt', filename).group(1)
      else:
        if rfc_number:
          url = RFC_URL + rfc_number + '.txt'
        #url = sys.argv[1]
        if '://' not in url:
          print '%s does not seem to be a URL. Bailing out....' % url
          sys.exit()
        filename = re.search ('^.*/(.*)\.txt', url).group(1)
        out_filename = "./pdf/" + filename + ".pdf"

        try:
          print "Fetching: %s" % url
          response = urllib2.urlopen(url)
        except urllib2.URLError, e:
          if e == 404:
            print "File not found: %s" % url
          else:
            print "Couldn't open %s, got error %s." % (url, e)
          sys.exit(-1)
        text = response.read()

      if outdir:
        out_filename = outdir + '/' + filename + ".pdf"
      else:
        out_filename = tempfile.mktemp()
      # Regardles of the standard, sometimes the file is in DOS format.
      # This replaces LF/CR with CR.
      text = string.join(string.split(text,'\r\n'),'\n')
      print "File seems valid"
      print "Setting up PDF creator..."
      pdf = mySimpleDocTemplate(out_filename, pagesize = letter,
        leftMargin = MARGIN)
      story = []
      style = getSampleStyleSheet()

      mystyle = style["Normal"]
      mystyle.fontName = "Courier"

      story.append(Preformatted(text, mystyle))
      print "Creating PDF..."
      pdf.build(story)
      print "Done..."

      print "Sending %s to printer with options: %s" % (out_filename,
                                                        PRINTER_OPT)
      cmd = "lpr %s %s" % (out_filename, PRINTER_OPT)
      os.popen (cmd)

      if outdir:
        print "Converted file saved as: %s" % out_filename
