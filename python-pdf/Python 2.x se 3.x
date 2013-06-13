
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    
    <title>Python 3 Porting Guide &mdash; Porting to Python 3 v1 documentation</title>
    <link rel="stylesheet" href="_static/nature.css" type="text/css" />
    <link rel="stylesheet" href="_static/pygments.css" type="text/css" />
    <script type="text/javascript">
      var DOCUMENTATION_OPTIONS = {
        URL_ROOT:    '',
        VERSION:     '1',
        COLLAPSE_INDEX: false,
        FILE_SUFFIX: '.html',
        HAS_SOURCE:  true
      };
    </script>
    <script type="text/javascript" src="_static/jquery.js"></script>
    <script type="text/javascript" src="_static/underscore.js"></script>
    <script type="text/javascript" src="_static/doctools.js"></script>
    <link rel="top" title="Porting to Python 3 v1 documentation" href="index.html" />
    <link rel="next" title="Python 3 Extension Porting Guide" href="c-porting.html" />
    <link rel="prev" title="Welcome to Porting to Python 3’s documentation!" href="index.html" /> 
  </head>
  <body>
    <div class="related">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="genindex.html" title="General Index"
             accesskey="I">index</a></li>
        <li class="right" >
          <a href="c-porting.html" title="Python 3 Extension Porting Guide"
             accesskey="N">next</a> |</li>
        <li class="right" >
          <a href="index.html" title="Welcome to Porting to Python 3’s documentation!"
             accesskey="P">previous</a> |</li>
        <li><a href="index.html">Porting to Python 3 v1 documentation</a> &raquo;</li> 
      </ul>
    </div>  

    <div class="document">
      <div class="documentwrapper">
        <div class="bodywrapper">
          <div class="body">
            
  <div class="section" id="python-3-porting-guide">
<h1>Python 3 Porting Guide<a class="headerlink" href="#python-3-porting-guide" title="Permalink to this headline">¶</a></h1>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field"><th class="field-name">Author:</th><td class="field-body">Brian Curtin &lt;<a class="reference external" href="mailto:curtin&#37;&#52;&#48;acm&#46;org">curtin<span>&#64;</span>acm<span>&#46;</span>org</a>&gt;</td>
</tr>
<tr class="field"><th class="field-name">Date:</th><td class="field-body">July 29, 2010</td>
</tr>
</tbody>
</table>
<div class="admonition warning">
<p class="first admonition-title">Warning</p>
<p class="last">This document is under construction.</p>
</div>
<div class="section" id="introduction">
<h2>Introduction<a class="headerlink" href="#introduction" title="Permalink to this headline">¶</a></h2>
<p>The move from Python 2.x to 3.x introduced a window of time where a number
of changes could be made in order to cleanup the language. In doing so, a
level of backwards incompatibility was introduced for the betterment the
language.</p>
<p>Outlined below are details of the changes introduced in Python 3 and their
impact on porting. Where possible, example code is used.</p>
</div>
<div class="section" id="organizational-changes">
<span id="id1"></span><h2>Organizational Changes<a class="headerlink" href="#organizational-changes" title="Permalink to this headline">¶</a></h2>
<p>Over the lifetime of Python, the names of some packages and modules have
deviated from the standards laid out in <span class="target" id="index-0"></span><a class="pep reference external" href="http://www.python.org/dev/peps/pep-0008"><strong>PEP 8</strong></a>. During the creation of
Python 3, several changes were made to bring names back to conformance with
the standard and reorganize some of the common functionality which existed
side-by-side.</p>
<div class="section" id="name-changes">
<h3>Name Changes<a class="headerlink" href="#name-changes" title="Permalink to this headline">¶</a></h3>
<p>The following modules were renamed outright.</p>
<table border="1" class="docutils">
<colgroup>
<col width="44%" />
<col width="56%" />
</colgroup>
<thead valign="bottom">
<tr><th class="head">Python 2 name</th>
<th class="head">Python 3 name</th>
</tr>
</thead>
<tbody valign="top">
<tr><td><a class="reference external" href="http://docs.python.org/library/__builtin__.html#module-__builtin__" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">__builtin__</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/builtins.html#module-builtins" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">builtins</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/configparser.html#module-ConfigParser" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">ConfigParser</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/configparser.html#module-configparser" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">configparser</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/copy_reg.html#module-copy_reg" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">copy_reg</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/copyreg.html#module-copyreg" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">copyreg</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/pickle.html#module-cPickle" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">cPickle</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/pickle.html#module-pickle" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">pickle</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/queue.html#module-Queue" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">Queue</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/queue.html#module-queue" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">queue</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/repr.html#module-repr" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">repr</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/reprlib.html#module-reprlib" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">reprlib</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/socketserver.html#module-SocketServer" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">SocketServer</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/socketserver.html#module-socketserver" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">socketserver</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/tkinter.html#module-Tkinter" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">Tkinter</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/tkinter.html#module-tkinter" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">tkinter</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/_winreg.html#module-_winreg" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">_winreg</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/winreg.html#module-winreg" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">winreg</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/thread.html#module-thread" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">thread</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/_thread.html#module-_thread" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">_thread</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/dummy_thread.html#module-dummy_thread" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">dummy_thread</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/_dummy_thread.html#module-_dummy_thread" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">_dummy_thread</span></tt></a></td>
</tr>
<tr><td><tt class="xref py py-mod docutils literal"><span class="pre">markupbase</span></tt></td>
<td><tt class="xref py py-mod docutils literal"><span class="pre">_markupbase</span></tt></td>
</tr>
</tbody>
</table>
<p>When writing code to support both Python 2 and 3 in the same codebase, a
common import idiom is to try the new name first, then fall back to the old
name imported as the new name.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">try</span><span class="p">:</span>
    <span class="kn">import</span> <span class="nn">queue</span>
<span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
    <span class="kn">import</span> <span class="nn">Queue</span> <span class="kn">as</span> <span class="nn">queue</span>
</pre></div>
</div>
</div>
<div class="section" id="reorganization">
<span id="id2"></span><h3>Reorganization<a class="headerlink" href="#reorganization" title="Permalink to this headline">¶</a></h3>
<p>The following objects were renamed and moved into packages in order to group
common functionality.</p>
<table border="1" class="docutils">
<colgroup>
<col width="39%" />
<col width="61%" />
</colgroup>
<thead valign="bottom">
<tr><th class="head">Python 2 name</th>
<th class="head">Python 3 name</th>
</tr>
</thead>
<tbody valign="top">
<tr><td><a class="reference external" href="http://docs.python.org/library/functions.html#xrange" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">xrange()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/functions.html#range" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">range()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/functions.html#reduce" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">reduce()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/functools.html#functools.reduce" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">functools.reduce()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/functions.html#intern" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">intern()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/sys.html#sys.intern" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">sys.intern()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/functions.html#unichr" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">unichr()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/functions.html#chr" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">chr()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/functions.html#basestring" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">basestring()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/functions.html#str" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">str()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/functions.html#long" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">long()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/functions.html#int" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">int()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/itertools.html#itertools.izip" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">itertools.izip()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/functions.html#zip" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">zip()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/itertools.html#itertools.imap" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">itertools.imap()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/functions.html#map" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">map()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/itertools.html#itertools.ifilter" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">itertools.ifilter()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/functions.html#filter" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">filter()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/itertools.html#itertools.ifilterfalse" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">itertools.ifilterfalse()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/itertools.html#itertools.filterfalse" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">itertools.filterfalse()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/cookielib.html#module-cookielib" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">cookielib</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/http.cookiejar.html#module-http.cookiejar" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">http.cookiejar</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/cookie.html#module-Cookie" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">Cookie</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/http.cookies.html#module-http.cookies" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">http.cookies</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/htmllib.html#module-htmlentitydefs" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">htmlentitydefs</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/html.entities.html#module-html.entities" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">html.entities</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/htmlparser.html#module-HTMLParser" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">HTMLParser</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/html.parser.html#module-html.parser" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">html.parser</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/httplib.html#module-httplib" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">httplib</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/http.client.html#module-http.client" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">http.client</span></tt></a></td>
</tr>
<tr><td><tt class="xref py py-mod docutils literal"><span class="pre">Dialog</span></tt></td>
<td><tt class="xref py py-mod docutils literal"><span class="pre">tkinter.dialog</span></tt></td>
</tr>
<tr><td><tt class="xref py py-mod docutils literal"><span class="pre">FileDialog</span></tt></td>
<td><tt class="xref py py-mod docutils literal"><span class="pre">tkinter.FileDialog</span></tt></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/scrolledtext.html#module-ScrolledText" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">ScrolledText</span></tt></a></td>
<td><tt class="xref py py-mod docutils literal"><span class="pre">tkinter.scolledtext</span></tt></td>
</tr>
<tr><td><tt class="xref py py-mod docutils literal"><span class="pre">SimpleDialog</span></tt></td>
<td><tt class="xref py py-mod docutils literal"><span class="pre">tkinter.simpledialog</span></tt></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/tix.html#module-Tix" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">Tix</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/tkinter.tix.html#module-tkinter.tix" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">tkinter.tix</span></tt></a></td>
</tr>
<tr><td><tt class="xref py py-mod docutils literal"><span class="pre">Tkconstants</span></tt></td>
<td><tt class="xref py py-mod docutils literal"><span class="pre">tkinter.constants</span></tt></td>
</tr>
<tr><td><tt class="xref py py-mod docutils literal"><span class="pre">Tkdnd</span></tt></td>
<td><tt class="xref py py-mod docutils literal"><span class="pre">tkinter.dnd</span></tt></td>
</tr>
<tr><td><tt class="xref py py-mod docutils literal"><span class="pre">tkColorChooser</span></tt></td>
<td><tt class="xref py py-mod docutils literal"><span class="pre">tkinter.colorchooser</span></tt></td>
</tr>
<tr><td><tt class="xref py py-mod docutils literal"><span class="pre">tkCommonDialog</span></tt></td>
<td><tt class="xref py py-mod docutils literal"><span class="pre">tkinter.commondialog</span></tt></td>
</tr>
<tr><td><tt class="xref py py-mod docutils literal"><span class="pre">tkFileDialog</span></tt></td>
<td><tt class="xref py py-mod docutils literal"><span class="pre">tkinter.filedialog</span></tt></td>
</tr>
<tr><td><tt class="xref py py-mod docutils literal"><span class="pre">tkFont</span></tt></td>
<td><tt class="xref py py-mod docutils literal"><span class="pre">tkinter.font</span></tt></td>
</tr>
<tr><td><tt class="xref py py-mod docutils literal"><span class="pre">tkMessageBox</span></tt></td>
<td><tt class="xref py py-mod docutils literal"><span class="pre">tkinter.messagebox</span></tt></td>
</tr>
<tr><td><tt class="xref py py-mod docutils literal"><span class="pre">tkSimpleDialog</span></tt></td>
<td><tt class="xref py py-mod docutils literal"><span class="pre">tkinter.simpledialog</span></tt></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/robotparser.html#module-robotparser" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">robotparser</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.robotparser.html#module-urllib.robotparser" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">urllib.robotparser</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urlparse.html#module-urlparse" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">urlparse</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.parse.html#module-urllib.parse" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">urllib.parse</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/stringio.html#cStringIO.StringIO" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">cStringIO.StringIO()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/io.html#io.StringIO" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">io.StringIO</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/userdict.html#module-UserString" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">UserString</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/collections.html#collections.UserString" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">collections.UserString</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/userdict.html#module-UserList" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">UserList</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/collections.html#collections.UserList" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">collections.UserList</span></tt></a></td>
</tr>
</tbody>
</table>
<p>The contents of the following modules were merged into other modules which
share a common theme.</p>
<table border="1" class="docutils">
<colgroup>
<col width="55%" />
<col width="45%" />
</colgroup>
<thead valign="bottom">
<tr><th class="head">Python 2 name</th>
<th class="head">Python 3 name</th>
</tr>
</thead>
<tbody valign="top">
<tr><td><a class="reference external" href="http://docs.python.org/library/basehttpserver.html#module-BaseHTTPServer" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">BaseHTTPServer</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/http.server.html#module-http.server" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">http.server</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/cgihttpserver.html#module-CGIHTTPServer" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">CGIHTTPServer</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/http.server.html#module-http.server" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">http.server</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/simplehttpserver.html#module-SimpleHTTPServer" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">SimpleHTTPServer</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/http.server.html#module-http.server" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">http.server</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/whichdb.html#module-whichdb" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">whichdb</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/library/dbm.html#module-dbm" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">dbm</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/anydbm.html#module-anydbm" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">anydbm</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/library/dbm.html#module-dbm" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">dbm</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/dbm.html#module-dbm" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">dbm</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/dbm.html#module-dbm.ndbm" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">dbm.ndbm</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/dumbdbm.html#module-dumbdbm" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">dumbdbm</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/dbm.html#module-dbm.dumb" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">dbm.dumb</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/gdbm.html#module-gdbm" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">gdbm</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/dbm.html#module-dbm.gnu" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">dbm.gnu</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/dbm.html#module-dbm" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">dbm</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/dbm.html#module-dbm.ndbm" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">dbm.ndbm</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/dbm.html#module-dbm" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">dbm</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/dbm.html#module-dbm.ndbm" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">dbm.ndbm</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/docxmlrpcserver.html#module-DocXMLRPCServer" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">DocXMLRPCServer</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/xmlrpc.server.html#module-xmlrpc.server" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">xmlrpc.server</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/simplexmlrpcserver.html#module-SimpleXMLRPCServer" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">SimpleXMLRPCServer</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/xmlrpc.server.html#module-xmlrpc.server" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">xmlrpc.server</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/commands.html#module-commands" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">commands</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/library/subprocess.html#module-subprocess" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">subprocess</span></tt></a></td>
</tr>
</tbody>
</table>
<p>The following built-in functions were moved into packages.</p>
<table border="1" class="docutils">
<colgroup>
<col width="25%" />
<col width="15%" />
<col width="60%" />
</colgroup>
<thead valign="bottom">
<tr><th class="head">Python 2 name</th>
<th class="head" colspan="2">Python 3 name</th>
</tr>
</thead>
<tbody valign="top">
<tr><td colspan="3"><a class="reference external" href="http://docs.python.org/library/functions.html#reduce" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">reduce()</span></tt></a>  | <a class="reference external" href="http://docs.python.org/py3k/library/functools.html#functools.reduce" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">functools.reduce()</span></tt></a></td>
</tr>
<tr><td colspan="3"><a class="reference external" href="http://docs.python.org/library/functions.html#reload" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">reload()</span></tt></a>  | <a class="reference external" href="http://docs.python.org/py3k/library/imp.html#imp.reload" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">imp.reload()</span></tt></a></td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="url-related-modules">
<h3>URL-related modules<a class="headerlink" href="#url-related-modules" title="Permalink to this headline">¶</a></h3>
<p>Due to the common theme among <a class="reference external" href="http://docs.python.org/library/urllib.html#module-urllib" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">urllib</span></tt></a>, <a class="reference external" href="http://docs.python.org/library/urllib2.html#module-urllib2" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">urllib2</span></tt></a>, <a class="reference external" href="http://docs.python.org/library/urlparse.html#module-urlparse" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">urlparse</span></tt></a>,
and <a class="reference external" href="http://docs.python.org/library/robotparser.html#module-robotparser" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">robotparser</span></tt></a>, a change was made to split their contents into a
package containing modules specific to certain areas like requests and parsing.</p>
<p>As shown in <a class="reference internal" href="#reorganization"><em>Reorganization</em></a>, <a class="reference external" href="http://docs.python.org/library/robotparser.html#module-robotparser" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">robotparser</span></tt></a> was moved entirely into
<a class="reference external" href="http://docs.python.org/py3k/library/urllib.robotparser.html#module-urllib.robotparser" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">urllib.robotparser</span></tt></a>. Along with this, <a class="reference external" href="http://docs.python.org/library/urlparse.html#module-urlparse" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">urlparse</span></tt></a> was moved entirely
into <a class="reference external" href="http://docs.python.org/py3k/library/urllib.parse.html#module-urllib.parse" title="(in Python v3.1)"><tt class="xref py py-mod docutils literal"><span class="pre">urllib.parse</span></tt></a>.</p>
<p>The following charts lay out the locations of the 2.x objects and their new
locations.</p>
<div class="section" id="urllib">
<h4>urllib<a class="headerlink" href="#urllib" title="Permalink to this headline">¶</a></h4>
<table border="1" class="docutils">
<colgroup>
<col width="30%" />
<col width="70%" />
</colgroup>
<thead valign="bottom">
<tr><th class="head">Python 2 name</th>
<th class="head">Python 3 name</th>
</tr>
</thead>
<tbody valign="top">
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib.html#urllib.urlopen" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.urlopen()</span></tt></a></td>
<td>Deprecated. See <a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.urlopen" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.request.urlopen()</span></tt></a> which mirrors <a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.urlopen" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">urllib2.urlopen()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib.html#urllib.urlretrieve" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.urlretrieve()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.urlretrieve" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.request.urlretrieve()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib.html#urllib.urlcleanup" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.urlcleanup()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.urlcleanup" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.request.urlcleanup()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib.html#urllib.quote" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.quote()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.parse.html#urllib.parse.quote" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.parse.quote()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib.html#urllib.quote_plus" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.quote_plus()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.parse.html#urllib.parse.quote_plus" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.parse.quote_plus()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib.html#urllib.unquote" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.unquote()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.parse.html#urllib.parse.unquote" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.parse.unquote()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib.html#urllib.unquote_plus" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.unquote_plus()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.parse.html#urllib.parse.unquote_plus" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.parse.unquote_plus()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib.html#urllib.urlencode" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.urlencode()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.parse.html#urllib.parse.urlencode" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.parse.urlencode()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib.html#urllib.pathname2url" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.pathname2url()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.pathname2url" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.request.pathname2url()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib.html#urllib.url2pathname" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.url2pathname()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.url2pathname" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.request.url2pathname()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib.html#urllib.getproxies" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.getproxies()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.getproxies" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.request.getproxies()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib.html#urllib.URLopener" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.URLopener</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.URLopener" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.URLopener</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib.html#urllib.FancyURLopener" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.FancyURLopener</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.FancyURLopener" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.FancyURLopener</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib.html#urllib.ContentTooShortError" title="(in Python v2.7)"><tt class="xref py py-exc docutils literal"><span class="pre">urllib.ContentTooShortError</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.error.html#urllib.error.ContentTooShortError" title="(in Python v3.1)"><tt class="xref py py-exc docutils literal"><span class="pre">urllib.error.ContentTooShortError</span></tt></a></td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="urllib2">
<h4>urllib2<a class="headerlink" href="#urllib2" title="Permalink to this headline">¶</a></h4>
<table border="1" class="docutils">
<colgroup>
<col width="47%" />
<col width="53%" />
</colgroup>
<thead valign="bottom">
<tr><th class="head">Python 2 name</th>
<th class="head">Python 3 name</th>
</tr>
</thead>
<tbody valign="top">
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.urlopen" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">urllib2.urlopen()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.urlopen" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.request.urlopen()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.install_opener" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">urllib2.install_opener()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.install_opener" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.request.install_opener()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.build_opener" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">urllib2.build_opener()</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.build_opener" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">urllib.request.build_opener()</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.URLError" title="(in Python v2.7)"><tt class="xref py py-exc docutils literal"><span class="pre">urllib2.URLError</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.error.html#urllib.error.URLError" title="(in Python v3.1)"><tt class="xref py py-exc docutils literal"><span class="pre">urllib.error.URLError</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.HTTPError" title="(in Python v2.7)"><tt class="xref py py-exc docutils literal"><span class="pre">urllib2.HTTPError</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.error.html#urllib.error.HTTPError" title="(in Python v3.1)"><tt class="xref py py-exc docutils literal"><span class="pre">urllib.error.HTTPError</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.Request" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.Request</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.Request" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.Request</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.OpenerDirector" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.OpenerDirector</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.OpenerDirector" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.OpenerDirector</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.BaseHandler" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.BaseHandler</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.BaseHandler" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.BaseHandler</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.HTTPDefaultErrorHandler" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.HTTPDefaultErrorHandler</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.HTTPDefaultErrorHandler" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.HTTPDefaultErrorHandler</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.HTTPRedirectHandler" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.HTTPRedirectHandler</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.HTTPRedirectHandler" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.HTTPRedirectHandler</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.HTTPCookieProcessor" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.HTTPCookieProcessor</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.HTTPCookieProcessor" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.HTTPCookieProcessor</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.ProxyHandler" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.ProxyHandler</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.ProxyHandler" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.ProxyHandler</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.HTTPPasswordMgr" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.HTTPPasswordMgr</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.HTTPPasswordMgr" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.HTTPPasswordMgr</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.HTTPPasswordMgrWithDefaultRealm" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.HTTPPasswordMgrWithDefaultRealm</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.HTTPPasswordMgrWithDefaultRealm" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.HTTPPasswordMgrWithDefaultRealm</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.AbstractBasicAuthHandler" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.AbstractBasicAuthHandler</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.AbstractBasicAuthHandler" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.AbstractBasicAuthHandler</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.HTTPBasicAuthHandler" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.HTTPBasicAuthHandler</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.HTTPBasicAuthHandler" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.HTTPBasicAuthHandler</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.ProxyBasicAuthHandler" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.ProxyBasicAuthHandler</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.ProxyBasicAuthHandler" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.ProxyBasicAuthHandler</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.AbstractDigestAuthHandler" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.AbstractDigestAuthHandler</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.AbstractDigestAuthHandler" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.AbstractDigestAuthHandler</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.HTTPDigestAuthHandler" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.HTTPDigestAuthHandler</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.HTTPDigestAuthHandler" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.HTTPDigestAuthHandler</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.ProxyDigestAuthHandler" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.ProxyDigestAuthHandler</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.ProxyDigestAuthHandler" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.ProxyDigestAuthHandler</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.HTTPHandler" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.HTTPHandler</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.HTTPHandler" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.HTTPHandler</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.HTTPSHandler" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.HTTPSHandler</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.HTTPSHandler" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.HTTPSHandler</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.FileHandler" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.FileHandler</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.FileHandler" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.FileHandler</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.FTPHandler" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.FTPHandler</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.FTPHandler" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.FTPHandler</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.CacheFTPHandler" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.CacheFTPHandler</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.CacheFTPHandler" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.CacheFTPHandler</span></tt></a></td>
</tr>
<tr><td><a class="reference external" href="http://docs.python.org/library/urllib2.html#urllib2.UnknownHandler" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">urllib2.UnknownHandler</span></tt></a></td>
<td><a class="reference external" href="http://docs.python.org/py3k/library/urllib.request.html#urllib.request.UnknownHandler" title="(in Python v3.1)"><tt class="xref py py-class docutils literal"><span class="pre">urllib.request.UnknownHandler</span></tt></a></td>
</tr>
</tbody>
</table>
</div>
</div>
<div class="section" id="optimized-modules">
<h3>Optimized Modules<a class="headerlink" href="#optimized-modules" title="Permalink to this headline">¶</a></h3>
<p>Modules such as <a class="reference external" href="http://docs.python.org/library/pickle.html#module-pickle" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">pickle</span></tt></a> and <a class="reference external" href="http://docs.python.org/library/stringio.html#module-StringIO" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">StringIO</span></tt></a>
have traditionally been offered with C implementations for performance reasons.
Rather than continue to expose two different implementations, a decision was
made to expose both implementations under the same name, choosing to utilize
the C implemenation if available and falling back to the pure-Python version
if not.</p>
<p>This decision removes the need for the following idiom, instead making the
more performant decision for the user.</p>
<blockquote>
<dl class="docutils">
<dt>try:</dt>
<dd>import cPickle as pickle</dd>
<dt>except ImportError:</dt>
<dd>import pickle</dd>
</dl>
</blockquote>
</div>
</div>
<div class="section" id="printing">
<span id="id3"></span><h2>Printing<a class="headerlink" href="#printing" title="Permalink to this headline">¶</a></h2>
<p>One of the most obvious changes when porting code to Python 3 is that
<tt class="docutils literal"><span class="pre">print</span></tt> is no longer a statement. Introduced in Python 3 and backported
as far back as 2.6 (although not as the default), <a class="reference external" href="http://docs.python.org/library/functions.html#print" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">print()</span></tt></a> became a
built-in function.</p>
<p><tt class="docutils literal"><span class="pre">print</span></tt> as a function offers all of the same features of <tt class="docutils literal"><span class="pre">print</span></tt> as a
statement but in a more natural syntax that fits with the rest of the language.</p>
<p>In the event that you need to support both Python 3 and Python 2.5 or prior,
it is best to use the <a class="reference external" href="http://docs.python.org/library/sys.html#module-sys" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">sys</span></tt></a> module&#8217;s output capabilities:
the <a class="reference external" href="http://docs.python.org/library/sys.html#sys.stdout" title="(in Python v2.7)"><tt class="xref py py-data docutils literal"><span class="pre">sys.stdout</span></tt></a> or <a class="reference external" href="http://docs.python.org/library/sys.html#sys.stderr" title="(in Python v2.7)"><tt class="xref py py-data docutils literal"><span class="pre">sys.stderr</span></tt></a> file objects. This method leaves
the handling of <tt class="docutils literal"><span class="pre">print</span></tt> features like separators and line endings up to the
user.</p>
<table border="1" class="docutils">
<colgroup>
<col width="37%" />
<col width="30%" />
<col width="33%" />
</colgroup>
<thead valign="bottom">
<tr><th class="head">Python 2.5 compatible format</th>
<th class="head">Python 2.6+ format</th>
<th class="head">Python 3 format</th>
</tr>
</thead>
<tbody valign="top">
<tr><td><div class="first last highlight-python"><div class="highlight"><pre><span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&quot;hello world</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">print</span> <span class="s">&quot;hello world&quot;</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">print</span><span class="p">(</span><span class="s">&quot;hello world&quot;</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr><td><div class="first last highlight-python"><div class="highlight"><pre><span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&quot;hello %</span><span class="se">\n</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">print</span> <span class="s">&quot;hello&quot;</span><span class="p">,</span> <span class="n">name</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">print</span><span class="p">(</span><span class="s">&quot;hello&quot;</span><span class="p">,</span> <span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr><td><div class="first last highlight-python"><div class="highlight"><pre><span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">]))</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">print</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">])</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><pre>print(x, y, sep="\n")</pre>
</div>
</td>
</tr>
<tr><td><div class="first last highlight-python"><div class="highlight"><pre><span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&quot;error</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">print</span> <span class="o">&gt;&gt;</span> <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="p">,</span> <span class="s">&quot;error&quot;</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><pre>print("error", file=sys.stderr)</pre>
</div>
</td>
</tr>
<tr><td><div class="first last highlight-python"><div class="highlight"><pre><span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&quot;one line&quot;</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">print</span> <span class="s">&quot;one line&quot;</span><span class="p">,</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><pre>print("one line", end="")</pre>
</div>
</td>
</tr>
</tbody>
</table>
<div class="admonition-backporting-note admonition ">
<p class="first admonition-title">Backporting Note</p>
<p class="last">The <a class="reference external" href="http://docs.python.org/library/functions.html#print" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">print()</span></tt></a> function was backported to Python 2.6 in the way of the
<a class="reference external" href="http://docs.python.org/library/__future__.html#module-__future__" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">__future__</span></tt></a> module. <tt class="docutils literal"><span class="pre">from</span> <span class="pre">__future__</span> <span class="pre">import</span> <span class="pre">print_function</span></tt> will
expose <a class="reference external" href="http://docs.python.org/library/functions.html#print" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">print()</span></tt></a> as a function and removes the ability to use <tt class="docutils literal"><span class="pre">print</span></tt>
as a statement.</p>
</div>
</div>
<div class="section" id="executing-arbitrary-code">
<h2>Executing Arbitrary Code<a class="headerlink" href="#executing-arbitrary-code" title="Permalink to this headline">¶</a></h2>
<div class="section" id="exec-statement">
<h3><tt class="docutils literal"><span class="pre">exec</span></tt> Statement<a class="headerlink" href="#exec-statement" title="Permalink to this headline">¶</a></h3>
<p>As with the <a class="reference internal" href="#printing"><em>print function</em></a>, <tt class="docutils literal"><span class="pre">exec</span></tt> has also become a
function. <a class="reference external" href="http://docs.python.org/py3k/library/functions.html#exec" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">exec()</span></tt></a> is used for the dynamic execution of arbitrary Python
code either as a string or a code object. Using <a class="reference external" href="http://docs.python.org/py3k/library/functions.html#exec" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">exec()</span></tt></a> as a function
is similar to <tt class="docutils literal"><span class="pre">exec</span></tt> as a statement.</p>
<p>Where the <tt class="docutils literal"><span class="pre">exec</span></tt> statement used to take the format
<tt class="docutils literal"><span class="pre">exec</span> <span class="pre">some_code</span> <span class="pre">in</span> <span class="pre">global_namespace,</span> <span class="pre">local_namespace</span></tt>, the order is still the
same, but just passed as parameters to the <a class="reference external" href="http://docs.python.org/py3k/library/functions.html#exec" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">exec()</span></tt></a> function.</p>
<table border="1" class="docutils">
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead valign="bottom">
<tr><th class="head">Python 2 format</th>
<th class="head">Python 3 format</th>
</tr>
</thead>
<tbody valign="top">
<tr><td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">exec</span> <span class="s">&quot;print &#39;hello&#39;&quot;</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">exec</span><span class="p">(</span><span class="s">&quot;print &#39;hello&#39;&quot;</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr><td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">exec</span> <span class="n">code</span> <span class="ow">in</span> <span class="n">global_ns</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">exec</span><span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">global_ns</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr><td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">exec</span> <span class="n">code</span> <span class="ow">in</span> <span class="n">global_ns</span><span class="p">,</span> <span class="n">local_ns</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">exec</span><span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">global_ns</span><span class="p">,</span> <span class="n">local_ns</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="execfile-statement">
<h3><tt class="docutils literal"><span class="pre">execfile</span></tt> Statement<a class="headerlink" href="#execfile-statement" title="Permalink to this headline">¶</a></h3>
<p>Starting with Python 3, the <tt class="docutils literal"><span class="pre">execfile</span></tt> statement is no longer available.
An alternative is to use the <a class="reference external" href="http://docs.python.org/library/functions.html#compile" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">compile()</span></tt></a> function in conjunction with
<a class="reference external" href="http://docs.python.org/py3k/library/functions.html#exec" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">exec()</span></tt></a>. <a class="reference external" href="http://docs.python.org/library/functions.html#compile" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">compile()</span></tt></a> can create a code object from a file, and then
it can be passed into <a class="reference external" href="http://docs.python.org/py3k/library/functions.html#exec" title="(in Python v3.1)"><tt class="xref py py-func docutils literal"><span class="pre">exec()</span></tt></a>.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">exec</span><span class="p">(</span><span class="nb">compile</span><span class="p">(</span><span class="n">source_code</span><span class="p">,</span> <span class="n">source_file_name</span><span class="p">,</span> <span class="s">&quot;exec&quot;</span><span class="p">))</span>
</pre></div>
</div>
</div>
</div>
<div class="section" id="exceptions">
<h2>Exceptions<a class="headerlink" href="#exceptions" title="Permalink to this headline">¶</a></h2>
<p>Exceptions were changed in a few ways for Python 3. First, strings are no
longer usable as exceptions. Additionally, the <tt class="xref std std-keyword docutils literal"><span class="pre">raise</span></tt> syntax no
longer accepts comma-separated arguments, instead working with exception
instances. Perhaps the largest difference in Python 3 is that exception
objects are only available via the <tt class="xref std std-keyword docutils literal"><span class="pre">as</span></tt> keyword, which was
introduced in 2.6.</p>
<div class="section" id="raising-exceptions">
<span id="id4"></span><h3>Raising Exceptions<a class="headerlink" href="#raising-exceptions" title="Permalink to this headline">¶</a></h3>
<p>Raising an exception creates an instance of <tt class="xref py py-class docutils literal"><span class="pre">Exception</span></tt> or a subclass,
so it follows that the <tt class="xref std std-keyword docutils literal"><span class="pre">raise</span></tt> statement uses the same syntax
required to create other class instances.</p>
<table border="1" class="docutils">
<colgroup>
<col width="45%" />
<col width="55%" />
</colgroup>
<thead valign="bottom">
<tr><th class="head">Python 2 format</th>
<th class="head">Python 3 format</th>
</tr>
</thead>
<tbody valign="top">
<tr><td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">raise</span> <span class="ne">IOError</span><span class="p">,</span> <span class="s">&quot;file error&quot;</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">raise</span> <span class="ne">IOError</span><span class="p">(</span><span class="s">&quot;file error&quot;</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr><td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">raise</span> <span class="s">&quot;ahhhh!&quot;</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s">&quot;ahhhh!&quot;</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr><td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">raise</span> <span class="ne">TypeError</span><span class="p">,</span> <span class="n">msg</span><span class="p">,</span> <span class="n">tb</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">raise</span> <span class="ne">TypeError</span><span class="o">.</span><span class="n">with_traceback</span><span class="p">(</span><span class="n">tb</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="handling-exceptions">
<h3>Handling Exceptions<a class="headerlink" href="#handling-exceptions" title="Permalink to this headline">¶</a></h3>
<p>A major change to exception handling is the use of the <tt class="xref std std-keyword docutils literal"><span class="pre">as</span></tt> keyword
for assignment of the exception object. Catching multiple exception classes
remains the same as before, implemented using a tuple with explicit
parentheses.</p>
<table border="1" class="docutils">
<colgroup>
<col width="48%" />
<col width="52%" />
</colgroup>
<thead valign="bottom">
<tr><th class="head">Python 2 format</th>
<th class="head">Python 3 format</th>
</tr>
</thead>
<tbody valign="top">
<tr><td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">try</span><span class="p">:</span>
    <span class="n">fn</span><span class="p">()</span>
<span class="k">except</span> <span class="ne">IOError</span><span class="p">,</span> <span class="n">err</span><span class="p">:</span>
    <span class="k">print</span> <span class="n">err</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">try</span><span class="p">:</span>
    <span class="n">fn</span><span class="p">()</span>
<span class="k">except</span> <span class="ne">IOError</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
    <span class="k">print</span><span class="p">(</span><span class="n">err</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr><td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">try</span><span class="p">:</span>
    <span class="n">fn</span><span class="p">()</span>
<span class="k">except</span> <span class="p">(</span><span class="ne">IOError</span><span class="p">,</span> <span class="ne">TypeError</span><span class="p">),</span> <span class="n">err</span><span class="p">:</span>
    <span class="k">print</span> <span class="n">err</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">try</span><span class="p">:</span>
    <span class="n">fn</span><span class="p">()</span>
<span class="k">except</span> <span class="p">(</span><span class="ne">IOError</span><span class="p">,</span> <span class="ne">TypeError</span><span class="p">)</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
    <span class="k">print</span><span class="p">(</span><span class="n">err</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<div class="admonition-backporting-note admonition ">
<p class="first admonition-title">Backporting Note</p>
<p class="last">The <tt class="docutils literal"><span class="pre">exception</span> <span class="pre">as</span> <span class="pre">var</span></tt> syntax was backported to Python 2.6 which allows
you to use either the 2.x or 3.x way simultaneously.</p>
</div>
<p>Due to the fact that the <tt class="xref std std-keyword docutils literal"><span class="pre">as</span></tt> keyword isn&#8217;t found Python 2.5 and
before, code which must run on versions with and without <tt class="xref std std-keyword docutils literal"><span class="pre">as</span></tt> support
can use the following idiom.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="kn">import</span> <span class="nn">sys</span>
<span class="k">try</span><span class="p">:</span>
    <span class="n">fn</span><span class="p">()</span>
<span class="k">except</span> <span class="p">(</span><span class="ne">IOError</span><span class="p">,</span> <span class="ne">TypeError</span><span class="p">):</span>
    <span class="n">err</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()[</span><span class="mi">1</span><span class="p">]</span>
    <span class="k">print</span><span class="p">(</span><span class="n">err</span><span class="p">)</span>
</pre></div>
</div>
<p>See <a class="reference external" href="http://docs.python.org/library/sys.html#sys.exc_info" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">sys.exc_info()</span></tt></a> for further details on it&#8217;s use.</p>
</div>
<div class="section" id="exceptions-from-generators">
<h3>Exceptions from Generators<a class="headerlink" href="#exceptions-from-generators" title="Permalink to this headline">¶</a></h3>
<p>Generators have a <tt class="xref py py-meth docutils literal"><span class="pre">throw()</span></tt> method to raise an exception in the current
frame, then return the next object in the function. The <tt class="xref py py-meth docutils literal"><span class="pre">throw()</span></tt> method
follows similar rules as <a class="reference internal" href="#raising-exceptions"><em>Raising Exceptions</em></a>: no string exceptions and
custom messages come in the form of an exception instance. The general case
of calling <tt class="docutils literal"><span class="pre">gen.throw(Exception)</span></tt> remains the same across 2 and 3.</p>
<table border="1" class="docutils">
<colgroup>
<col width="49%" />
<col width="51%" />
</colgroup>
<thead valign="bottom">
<tr><th class="head">Python 2 format</th>
<th class="head">Python 3 format</th>
</tr>
</thead>
<tbody valign="top">
<tr><td><div class="first last highlight-python"><div class="highlight"><pre><span class="n">gen</span><span class="o">.</span><span class="n">throw</span><span class="p">(</span><span class="ne">ValueError</span><span class="p">,</span> <span class="s">&quot;bad value&quot;</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><div class="highlight"><pre><span class="n">gen</span><span class="o">.</span><span class="n">throw</span><span class="p">(</span><span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;bad value&quot;</span><span class="p">))</span>
</pre></div>
</div>
</td>
</tr>
<tr><td><div class="first last highlight-python"><div class="highlight"><pre><span class="n">gen</span><span class="o">.</span><span class="n">throw</span><span class="p">(</span><span class="s">&quot;bad value&quot;</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td>Deprecated</td>
</tr>
</tbody>
</table>
</div>
</div>
<div class="section" id="division">
<h2>Division<a class="headerlink" href="#division" title="Permalink to this headline">¶</a></h2>
<p>Python 3 introduces the ability to do true division using the <tt class="docutils literal"><span class="pre">/</span></tt> division
operator, as proposed and outlined in <span class="target" id="index-1"></span><a class="pep reference external" href="http://www.python.org/dev/peps/pep-0238"><strong>PEP 238</strong></a>. Although the functionality
has been in place since Python 2.2, it did not become the default operation
for <tt class="docutils literal"><span class="pre">/</span></tt> until Python 3.</p>
<p>True division works for <a class="reference external" href="http://docs.python.org/library/functions.html#int" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">int()</span></tt></a> and <a class="reference external" href="http://docs.python.org/library/functions.html#long" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">long()</span></tt></a> as well as <a class="reference external" href="http://docs.python.org/library/functions.html#float" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">float()</span></tt></a>.
In all cases a <a class="reference external" href="http://docs.python.org/library/functions.html#float" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">float()</span></tt></a> object is the return value.</p>
<div class="admonition-pep-238-excerpt admonition ">
<p class="first admonition-title">PEP 238 Excerpt</p>
<p class="last">Note that for int and long arguments, true division may lose information;
this is in the nature of true division (as long as rationals are not in
the language).  Algorithms that consciously use longs should consider
using //, as true division of longs retains no more than 53 bits of
precision (on most platforms).</p>
</div>
<p>The following examples show the difference between the division operator
on Python 2 and 3.</p>
<table border="1" class="docutils">
<colgroup>
<col width="55%" />
<col width="45%" />
</colgroup>
<thead valign="bottom">
<tr><th class="head">Python 2 format</th>
<th class="head">Python 3 format</th>
</tr>
</thead>
<tbody valign="top">
<tr><td><div class="first last highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="mi">1</span><span class="o">/</span><span class="mi">10</span>
<span class="go">0</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mf">1.0</span><span class="o">/</span><span class="mi">10</span>
<span class="go">0.10000000000000001</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">10</span><span class="o">/</span><span class="mi">1</span>
<span class="go">10</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="mi">1</span><span class="o">/</span><span class="mi">10</span>
<span class="go">0.1</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mf">1.0</span><span class="o">/</span><span class="mi">10</span>
<span class="go">0.1</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">10</span><span class="o">/</span><span class="mi">1</span>
<span class="go">10.0</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<div class="section" id="preparation-options">
<h3>Preparation Options<a class="headerlink" href="#preparation-options" title="Permalink to this headline">¶</a></h3>
<p>Whether you are preparing to move from Python 2 or you need to support
both 2 and 3 at the same time, there are two ways to get true division on
Python 2.</p>
<p>Access to true division can be had via code by using the <a class="reference external" href="http://docs.python.org/library/__future__.html#module-__future__" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">__future__</span></tt></a>
module&#8217;s <tt class="docutils literal"><span class="pre">from</span> <span class="pre">__future__</span> <span class="pre">import</span> <span class="pre">division</span></tt>, which is available
dating back to Python 2.2.</p>
<p>Additionally, the <tt class="docutils literal"><span class="pre">-Q</span></tt> command line option to the Python 2 interpreter
allows the user to globally define what will occur during division operations.
The option accepts four arguments.</p>
<ul class="simple">
<li><strong>old</strong> is the default in Python 2.2 and forces the &#8220;classic&#8221; division
operator to be enabled.</li>
<li><strong>warn</strong> causes &#8220;classic&#8221; division of <tt class="docutils literal"><span class="pre">int</span></tt> and <tt class="docutils literal"><span class="pre">long</span></tt> to issue a
<tt class="xref py py-class docutils literal"><span class="pre">DeprecationWarning</span></tt>.</li>
<li><strong>warnall</strong> issues <tt class="xref py py-class docutils literal"><span class="pre">DeprecationWarning</span></tt> on &#8220;classic&#8221; division of
<tt class="docutils literal"><span class="pre">float</span></tt> or complex numbers, in addition to the characteristics of <strong>warn</strong>.</li>
<li><strong>new</strong> changes the <tt class="docutils literal"><span class="pre">/</span></tt> division operator to use true division. This is the
same result as using <tt class="docutils literal"><span class="pre">from</span> <span class="pre">__future__</span> <span class="pre">import</span> <span class="pre">division</span></tt>.</li>
</ul>
<p>The <tt class="docutils literal"><span class="pre">//</span></tt> floor division operator remains unchanged, providing the same
functionality across both versions.</p>
</div>
</div>
<div class="section" id="long-integers">
<h2>Long Integers<a class="headerlink" href="#long-integers" title="Permalink to this headline">¶</a></h2>
<p><span class="target" id="index-2"></span><a class="pep reference external" href="http://www.python.org/dev/peps/pep-0237"><strong>PEP 237</strong></a>, first drafted in 2001, introduced an effort to remove the
distinction between <tt class="docutils literal"><span class="pre">int</span></tt> and <tt class="docutils literal"><span class="pre">long</span></tt> integers. The work was completed in
a three-phased approach spanning Python 2.2 through 2.4. Python 3.0 added
a final step by officially removing the <a class="reference external" href="http://docs.python.org/library/functions.html#long" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">long()</span></tt></a> type and <tt class="docutils literal"><span class="pre">long</span></tt>
literals (e.g., <tt class="docutils literal"><span class="pre">123456789L</span></tt>).</p>
<p>In places where you would use <a class="reference external" href="http://docs.python.org/library/functions.html#long" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">long()</span></tt></a>, <a class="reference external" href="http://docs.python.org/library/functions.html#int" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">int()</span></tt></a> is the replacement
and it will store the value in the correct internal representation.</p>
<p>In places where you used the <tt class="docutils literal"><span class="pre">L</span></tt> suffix to produce``long`` literals, removal
of the <tt class="docutils literal"><span class="pre">L</span></tt> is necessary, otherwise a <tt class="xref py py-exc docutils literal"><span class="pre">SyntaxError</span></tt> will be raised.</p>
</div>
<div class="section" id="iterators">
<h2>Iterators<a class="headerlink" href="#iterators" title="Permalink to this headline">¶</a></h2>
<p>Python 3 introduced a <a class="reference external" href="http://docs.python.org/library/functions.html#next" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">next()</span></tt></a> function to replace the <tt class="xref py py-meth docutils literal"><span class="pre">next()</span></tt> method
on iterator objects. Rather than calling the method on the iterator, the
<a class="reference external" href="http://docs.python.org/library/functions.html#next" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">next()</span></tt></a> function is called with the iterable object as it&#8217;s sole
parameter, which calls the underlying <tt class="xref py py-meth docutils literal"><span class="pre">__next__()</span></tt> method.</p>
<div class="section" id="iterating">
<span id="id5"></span><h3>Iterating<a class="headerlink" href="#iterating" title="Permalink to this headline">¶</a></h3>
<p>Given the following simple generator function, getting the values one-by-one
is done slightly different across versions.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">word</span><span class="p">(</span><span class="n">letters</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">letter</span> <span class="ow">in</span> <span class="n">letters</span><span class="p">:</span>
        <span class="k">yield</span> <span class="n">letter</span>
</pre></div>
</div>
<table border="1" class="docutils">
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead valign="bottom">
<tr><th class="head">Python 2 format</th>
<th class="head">Python 3 format</th>
</tr>
</thead>
<tbody valign="top">
<tr><td><div class="first last highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">x</span> <span class="o">=</span> <span class="n">word</span><span class="p">(</span><span class="s">&quot;hi&quot;</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>
<span class="go">&#39;h&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>
<span class="go">&#39;i&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">x</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>
<span class="gt">Traceback (most recent call last):</span>
  File <span class="nb">&quot;&lt;stdin&gt;&quot;</span>, line <span class="m">1</span>, in <span class="n-Identifier">&lt;module&gt;</span>
<span class="nc">StopIteration</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">x</span> <span class="o">=</span> <span class="n">word</span><span class="p">(</span><span class="s">&quot;hi&quot;</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">next</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>
<span class="go">&#39;h&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">next</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>
<span class="go">&#39;i&#39;</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">next</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>
<span class="gt">Traceback (most recent call last):</span>
  File <span class="nb">&quot;&lt;stdin&gt;&quot;</span>, line <span class="m">1</span>, in <span class="n-Identifier">&lt;module&gt;</span>
<span class="nc">StopIteration</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<div class="admonition-backporting-note admonition ">
<p class="first admonition-title">Backporting Note</p>
<p class="last">The <a class="reference external" href="http://docs.python.org/library/functions.html#next" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">next()</span></tt></a> function was backported to Python 2.6 which allows you to
use either the 2.x or 3.x way simultaneously.</p>
</div>
</div>
<div class="section" id="creating-iterators">
<h3>Creating Iterators<a class="headerlink" href="#creating-iterators" title="Permalink to this headline">¶</a></h3>
<p>Due to the change discussed in <a class="reference internal" href="#iterating"><em>Iterating</em></a>, creation of iterators is also
slightly different in Python 3. The <a class="reference external" href="http://docs.python.org/library/functions.html#next" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">next()</span></tt></a> function now calls an
iterator&#8217;s <tt class="xref py py-meth docutils literal"><span class="pre">__next__()</span></tt> special method, whereas Python 2.5 and prior call
the iterator&#8217;s <tt class="xref py py-meth docutils literal"><span class="pre">next()</span></tt> method directly. The good thing is that it&#8217;s easy
to write iterators that can run on versions prior to 2.6 and 3 at the same
time.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">class</span> <span class="nc">Countdown</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">max</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="nb">max</span>

    <span class="k">def</span> <span class="nf">__iter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span>

    <span class="k">def</span> <span class="nf">__next__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;2.6-3.x version&quot;&quot;&quot;</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">next</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;2.5 version&quot;&quot;&quot;</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">-=</span> <span class="mi">1</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">StopIteration</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</pre></div>
</div>
</div>
</div>
<div class="section" id="dictionaries">
<h2>Dictionaries<a class="headerlink" href="#dictionaries" title="Permalink to this headline">¶</a></h2>
<p>A number of changes were made to the <a class="reference external" href="http://docs.python.org/library/stdtypes.html#dict" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">dict</span></tt></a> type to better integrate it
with the current trends in the language. <span class="target" id="index-3"></span><a class="pep reference external" href="http://www.python.org/dev/peps/pep-3106"><strong>PEP 3106</strong></a>, which was adopted in 3.0,
outlines the introduction of a new feature called dictionary views, or a more
lightweight replacement for the lists returned by several methods.
Additionally, the PEP explains the removal of <tt class="docutils literal"><span class="pre">iter*</span></tt> methods on
the attributes of dictionaries. Another removal is the <a class="reference external" href="http://docs.python.org/library/stdtypes.html#dict.has_key" title="(in Python v2.7)"><tt class="xref py py-meth docutils literal"><span class="pre">dict.has_key()</span></tt></a>
method.</p>
<div class="section" id="supporting-dictionary-views">
<h3>Supporting Dictionary Views<a class="headerlink" href="#supporting-dictionary-views" title="Permalink to this headline">¶</a></h3>
<p>Python 3.0 introduced the concept of views, or a dynamic peek into the
contents of a <a class="reference external" href="http://docs.python.org/library/stdtypes.html#dict" title="(in Python v2.7)"><tt class="xref py py-class docutils literal"><span class="pre">dict</span></tt></a>. Even when a dictionary is mutated, all of its
views are kept in-sync to reflect the current state of the dictionary.
Views are supported on <a class="reference external" href="http://docs.python.org/library/stdtypes.html#dict.items" title="(in Python v2.7)"><tt class="xref py py-meth docutils literal"><span class="pre">dict.items()</span></tt></a>, <a class="reference external" href="http://docs.python.org/library/stdtypes.html#dict.keys" title="(in Python v2.7)"><tt class="xref py py-meth docutils literal"><span class="pre">dict.keys()</span></tt></a>,
and <a class="reference external" href="http://docs.python.org/library/stdtypes.html#dict.values" title="(in Python v2.7)"><tt class="xref py py-meth docutils literal"><span class="pre">dict.values()</span></tt></a> to replace the old-style form which returned a
<tt class="xref py py-class docutils literal"><span class="pre">list</span></tt>.</p>
<div class="admonition-backporting-note admonition ">
<p class="first admonition-title">Backporting Note</p>
<p class="last">Since the view concept has no equivalent in 2.x, the backporting of views
was done in Python 2.7 under different names. View-returning methods are
prefixed with <tt class="docutils literal"><span class="pre">view</span></tt>, while the list-returning methods remain unchanged.</p>
</div>
<div class="section" id="supporting-2-7-and-3-x">
<h4>Supporting 2.7 and 3.x<a class="headerlink" href="#supporting-2-7-and-3-x" title="Permalink to this headline">¶</a></h4>
<p>Due to the name difference in the APIs, supporting views in both 2.7 and 3.x
results in a less than beautiful snipped of code.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="kn">import</span> <span class="nn">sys</span>

<span class="n">view_attr</span> <span class="o">=</span> <span class="s">&quot;items&quot;</span> <span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="o">.</span><span class="n">major</span> <span class="o">==</span> <span class="mi">3</span> <span class="k">else</span> <span class="s">&quot;viewitems&quot;</span>
<span class="n">location</span> <span class="o">=</span> <span class="p">{</span><span class="s">&quot;city&quot;</span> <span class="p">:</span> <span class="s">&quot;Chicago&quot;</span><span class="p">,</span> <span class="s">&quot;state&quot;</span> <span class="p">:</span> <span class="s">&quot;Illinois&quot;</span><span class="p">}</span>

<span class="k">def</span> <span class="nf">view_location</span><span class="p">():</span>
    <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">d</span><span class="p">,</span> <span class="n">view_attr</span><span class="p">)():</span>
        <span class="k">print</span><span class="p">(</span><span class="s">&quot;{}: {}&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">))</span>
</pre></div>
</div>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">view_location</span><span class="p">()</span>
<span class="go">city: Chicago</span>
<span class="go">state: Illinois</span>
</pre></div>
</div>
</div>
<div class="section" id="supporting-pre-2-7-and-3-x">
<h4>Supporting pre-2.7 and 3.x<a class="headerlink" href="#supporting-pre-2-7-and-3-x" title="Permalink to this headline">¶</a></h4>
<p>If your project supports versions prior to 2.7 where there is no concept
of a view, you can create a list from a view in order to safely remain
compatible across versions.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="n">keys</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">location</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</pre></div>
</div>
<p>Without a list, you should be aware of how views function when the dictionary
is changed. In a lot of cases you will be fine as-is. Other cases may require
an explicit list like above.</p>
<div class="highlight-python"><pre>Python 2.6.5+ (release26-maint:83007:83008, Jul 27 2010, 22:52:5)
[GCC 4.0.1 (Apple Inc. build 5465)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; location = {"city" : "Chicago", "state" : "Illinois"}
&gt;&gt;&gt; keys = location.keys()
&gt;&gt;&gt; print(keys)
['city', 'state']
&gt;&gt;&gt; del location["city"]
&gt;&gt;&gt; print(keys)
['city', 'state']</pre>
</div>
<div class="highlight-python"><pre>Python 3.2a0 (py3k:83172M, Jul 27 2010, 23:01:10)
[GCC 4.0.1 (Apple Inc. build 5465)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; location = {"city" : "Chicago", "state" : "Illinois"}
&gt;&gt;&gt; keys = location.keys()
&gt;&gt;&gt; print(keys)
dict_keys(['city', 'state'])
&gt;&gt;&gt; del location["city"]
&gt;&gt;&gt; print(keys)
dict_keys(['state'])</pre>
</div>
<p>Notice that the 3.2 code is using a view for <a class="reference external" href="http://docs.python.org/py3k/library/stdtypes.html#dict.keys" title="(in Python v3.1)"><tt class="xref py py-meth docutils literal"><span class="pre">dict.keys</span></tt></a>,
which results in the <tt class="docutils literal"><span class="pre">keys</span></tt> object being updated after the dictionary was
modified. Contrast that with the 2.6 example which uses a <tt class="xref py py-class docutils literal"><span class="pre">list</span></tt> for
<tt class="docutils literal"><span class="pre">keys</span></tt>, which does not stay in-sync with the dictionary from which the
keys are from.</p>
</div>
</div>
<div class="section" id="replacing-iter-methods">
<h3>Replacing <tt class="docutils literal"><span class="pre">iter*</span></tt> methods<a class="headerlink" href="#replacing-iter-methods" title="Permalink to this headline">¶</a></h3>
<p>Use of <a class="reference external" href="http://docs.python.org/library/stdtypes.html#dict.iteritems" title="(in Python v2.7)"><tt class="xref py py-meth docutils literal"><span class="pre">dict.iteritems()</span></tt></a> and <a class="reference external" href="http://docs.python.org/library/stdtypes.html#dict.itervalues" title="(in Python v2.7)"><tt class="xref py py-meth docutils literal"><span class="pre">dict.itervalues()</span></tt></a> should be replaced
by the following familiar looping construct.</p>
<div class="highlight-python"><pre>for key, value in d.items()</pre>
</div>
<p>The same could be done for <a class="reference external" href="http://docs.python.org/library/stdtypes.html#dict.iterkeys" title="(in Python v2.7)"><tt class="xref py py-meth docutils literal"><span class="pre">dict.iterkeys()</span></tt></a>; however, <tt class="docutils literal"><span class="pre">key</span> <span class="pre">in</span> <span class="pre">d</span></tt> is a
more common option.</p>
</div>
<div class="section" id="replacing-dict-has-key">
<h3>Replacing <a class="reference external" href="http://docs.python.org/library/stdtypes.html#dict.has_key" title="(in Python v2.7)"><tt class="xref py py-meth docutils literal"><span class="pre">dict.has_key()</span></tt></a><a class="headerlink" href="#replacing-dict-has-key" title="Permalink to this headline">¶</a></h3>
<p>The <a class="reference external" href="http://docs.python.org/library/stdtypes.html#dict.has_key" title="(in Python v2.7)"><tt class="xref py py-meth docutils literal"><span class="pre">dict.has_key()</span></tt></a> is not supported in Python 3.0, in favor of the
<tt class="docutils literal"><span class="pre">key</span> <span class="pre">in</span> <span class="pre">d</span></tt> idiom which was introduced in 2.2. Formal deprecation of
<a class="reference external" href="http://docs.python.org/library/stdtypes.html#dict.has_key" title="(in Python v2.7)"><tt class="xref py py-meth docutils literal"><span class="pre">dict.has_key()</span></tt></a> began in 2.6.</p>
<table border="1" class="docutils">
<colgroup>
<col width="57%" />
<col width="43%" />
</colgroup>
<thead valign="bottom">
<tr><th class="head">Python 2 format</th>
<th class="head">Python 3 format</th>
</tr>
</thead>
<tbody valign="top">
<tr><td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">if</span> <span class="n">d</span><span class="o">.</span><span class="n">has_key</span><span class="p">(</span><span class="s">&quot;foo&quot;</span><span class="p">):</span>
    <span class="n">bar</span><span class="p">()</span>
</pre></div>
</div>
</td>
<td><div class="first last highlight-python"><div class="highlight"><pre><span class="k">if</span> <span class="s">&quot;foo&quot;</span> <span class="ow">in</span> <span class="n">d</span><span class="p">:</span>
    <span class="n">bar</span><span class="p">()</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
<div class="section" id="strategies">
<h2>Strategies<a class="headerlink" href="#strategies" title="Permalink to this headline">¶</a></h2>
<p>When planning support for both Python 2 and 3 simultaneously, there are a
number of solutions to a number of problems. Perhaps the most important
prerequisite to supporting mutliple (or even one!) versions of Python is
tests. Without tests, it will be very hard to tell if your code works the way
you intend it to across versions, especially across 2 and 3. Consider
expanding your test coverage in order to ensure the quality of your
application as you introduce your users to Python 3.</p>
<p>What follows are three strategies for simultaneously supporting Python 2 and 3.
An option not listed here is to create two branches for your project and
support 2 and 3 separately. That method may require more work for a developer,
but it&#8217;s straightforward to do and doesn&#8217;t require any discussion here.</p>
<div class="section" id="single-codebase">
<h3>Single Codebase<a class="headerlink" href="#single-codebase" title="Permalink to this headline">¶</a></h3>
<p>One possibility for supporting both Python 2 and it&#8217;s backwards incompatible
successor, Python 3, is by writing all of your code in a single codebase.
Some users have been able to support ranges as wide as Python 2.0 through 3.0
all from one source.</p>
<div class="section" id="imports">
<h4>Imports<a class="headerlink" href="#imports" title="Permalink to this headline">¶</a></h4>
<p>As listed in <a class="reference internal" href="#organizational-changes"><em>Organizational Changes</em></a>, a number of package and module
names have changed in Python 3. In order to support import name changes,
an common idiom is to try one name and fallback to another.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">try</span><span class="p">:</span>
    <span class="c"># 3.x name</span>
    <span class="kn">import</span> <span class="nn">configparser</span>
<span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
    <span class="c"># 2.x name</span>
    <span class="kn">import</span> <span class="nn">ConfigParser</span> <span class="kn">as</span> <span class="nn">configparser</span>
</pre></div>
</div>
<p>However, the further back your support needs to go, the further you get away
from the <tt class="docutils literal"><span class="pre">as</span></tt> keyword and it&#8217;s nicetes. If you need to support Python 2.4
and prior, your conditional importing can use <a class="reference external" href="http://docs.python.org/library/functions.html#__import__" title="(in Python v2.7)"><tt class="xref py py-func docutils literal"><span class="pre">__import__()</span></tt></a>.</p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">try</span><span class="p">:</span>
    <span class="c"># 3.x name</span>
    <span class="kn">import</span> <span class="nn">configparser</span>
<span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
    <span class="c"># 2.x name</span>
    <span class="n">configparser</span> <span class="o">=</span> <span class="nb">__import__</span><span class="p">(</span><span class="s">&quot;ConfigParser&quot;</span><span class="p">)</span>
</pre></div>
</div>
</div>
<div class="section" id="defeating-deprecation">
<h4>Defeating Deprecation<a class="headerlink" href="#defeating-deprecation" title="Permalink to this headline">¶</a></h4>
<p>Over the 10 years since Python 2.0 came out in October 2000, plenty of things
have come and gone in the language. Due to the deprecation and introduction of
some things, codebases which support a wide range of versions will need to
do some operations in two different ways depending on the runtime version.</p>
<p>A good way to support differing underlying implementations is to create a
compatiblility module. You can use <a class="reference external" href="http://docs.python.org/library/sys.html#sys.version_info" title="(in Python v2.7)"><tt class="xref py py-data docutils literal"><span class="pre">sys.version_info</span></tt></a> to figure out
which version you are running on.</p>
<div class="highlight-python"><pre>compat/
    __init__.py
    two.py
    three.py</pre>
</div>
<p><tt class="docutils literal"><span class="pre">compat/__init__.py</span></tt></p>
<div class="highlight-python"><div class="highlight"><pre><span class="kn">import</span> <span class="nn">sys</span>
<span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="mi">2</span><span class="p">:</span>
    <span class="kn">from</span> <span class="nn">two</span> <span class="kn">import</span> <span class="o">*</span>
<span class="k">else</span><span class="p">:</span>
    <span class="kn">from</span> <span class="nn">.three</span> <span class="kn">import</span> <span class="o">*</span>
</pre></div>
</div>
<p>The idea here is that your 2.x-specific code resides in <tt class="docutils literal"><span class="pre">compat.two</span></tt> and
is only accessed when you import <tt class="docutils literal"><span class="pre">compat</span></tt> while running on 2.x. The same
for <tt class="docutils literal"><span class="pre">compat.three</span></tt> &#8211; it can use the new way to do things.</p>
<p><tt class="docutils literal"><span class="pre">compat/two.py</span></tt></p>
<div class="highlight-python"><div class="highlight"><pre><span class="kn">from</span> <span class="nn">types</span> <span class="kn">import</span> <span class="n">DictType</span>
<span class="k">def</span> <span class="nf">is_dict</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span>
    <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span> <span class="o">==</span> <span class="n">DictType</span>
</pre></div>
</div>
<p>As you may recognize, <tt class="docutils literal"><span class="pre">two</span></tt> uses an old method for figuring out if some
object is a dictionary.</p>
<p><tt class="docutils literal"><span class="pre">compat/three.py</span></tt></p>
<div class="highlight-python"><div class="highlight"><pre><span class="k">def</span> <span class="nf">is_dict</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span>
    <span class="k">return</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="nb">dict</span><span class="p">)</span>
</pre></div>
</div>
<p><tt class="docutils literal"><span class="pre">three</span></tt> uses the newer method, which would also work for recent versions of
Python 2.x as well.</p>
<div class="section" id="introducing-six">
<h5>Introducing <tt class="docutils literal"><span class="pre">six</span></tt><a class="headerlink" href="#introducing-six" title="Permalink to this headline">¶</a></h5>
<p>A compatibility-focused package currently exists to support this exact
method of working with Python 2 and 3 at the same time.
<a class="reference external" href="http://pypi.python.org/pypi/six/">six</a> is a package which includes
compatiblilty layers for imports, constants, syntax, and other areas which
differ between the two versions.</p>
</div>
</div>
</div>
<div class="section" id="pure-2-x-source">
<span id="x-source"></span><h3>Pure 2.x Source<a class="headerlink" href="#pure-2-x-source" title="Permalink to this headline">¶</a></h3>
<p>Maintaining individual branches for 2.x and 3.x support isn&#8217;t a well liked
solution for most projects. With the introduction of <tt class="xref py py-mod docutils literal"><span class="pre">2to3</span></tt>, projects
can keep their source in 2.x format and run <tt class="xref py py-mod docutils literal"><span class="pre">2to3</span></tt> when preparing for
a release. <tt class="xref py py-mod docutils literal"><span class="pre">2to3</span></tt> applies what are known as &#8220;fixers&#8221; in <a class="reference external" href="http://docs.python.org/library/2to3.html#module-lib2to3" title="(in Python v2.7)"><tt class="xref py py-mod docutils literal"><span class="pre">lib2to3</span></tt></a>
to convert 2.x code into the equivalent 3.x code.</p>
<p><tt class="docutils literal"><span class="pre">example.py</span></tt></p>
<div class="highlight-python"><div class="highlight"><pre><span class="c"># 2.x print without trailing new-line</span>
<span class="k">print</span> <span class="s">&quot;hello world&quot;</span><span class="p">,</span>
</pre></div>
</div>
<p>Output:</p>
<div class="highlight-python"><pre>$ example.py
RefactoringTool: Skipping implicit fixer: buffer
RefactoringTool: Skipping implicit fixer: idioms
RefactoringTool: Skipping implicit fixer: set_literal
RefactoringTool: Skipping implicit fixer: ws_comma
--- example.py (original)
+++ example.py (refactored)
@@ -1,2 +1,2 @@
 # 2.x print without trailing new-line
-print "hello world",
+print("hello world", end=' ')
RefactoringTool: Files that need to be modified:
RefactoringTool: example.py</pre>
</div>
<p>See the documentation for <tt class="xref py py-mod docutils literal"><span class="pre">2to3</span></tt> for all available options.</p>
<div class="section" id="tests">
<h4>Tests<a class="headerlink" href="#tests" title="Permalink to this headline">¶</a></h4>
<p>In order to successfully use <tt class="xref py py-mod docutils literal"><span class="pre">2to3</span></tt> at release time, your project should
have an exhaustive test suite. Although <tt class="xref py py-mod docutils literal"><span class="pre">2to3</span></tt> intends to be as complete
a tool as possible, there may be situations it does not currently handle which
could leave your project in a state different than expected.</p>
<p>Along with tests, you should manually review the changes made by <tt class="xref py py-mod docutils literal"><span class="pre">2to3</span></tt>
to ensure that your project was modified in a correct manner.</p>
</div>
</div>
<div class="section" id="pure-3-x-source">
<h3>Pure 3.x Source<a class="headerlink" href="#pure-3-x-source" title="Permalink to this headline">¶</a></h3>
<p>Thanks to <a class="reference external" href="http://pypi.python.org/pypi/3to2">3to2</a>, the possibility exists
to have 3.x source as your base and convert it to 2.x &#8211; the opposite of
<a class="reference internal" href="#x-source"><em>Pure 2.x Source</em></a>.</p>
<p>The project is currently underway for the Google Summer of Code, an extension
of the work done during the 2009 GSoC. For further details and examples,
see <a class="reference external" href="http://bitbucket.org/amentajo/lib3to2">http://bitbucket.org/amentajo/lib3to2</a>.</p>
<p>As with the <tt class="xref py py-mod docutils literal"><span class="pre">2to3</span></tt> method, a good test suite is instrumental in
succesfully using a 3.x base and <tt class="docutils literal"><span class="pre">3to2</span></tt> for conversion.</p>
</div>
</div>
<div class="section" id="references">
<h2>References<a class="headerlink" href="#references" title="Permalink to this headline">¶</a></h2>
<p>The following pages were either used in the creation of this document, or are
found to be generally useful. Thanks to the authors of all of the following.</p>
<ul class="simple">
<li><a class="reference external" href="http://pypi.python.org/pypi/six/">http://pypi.python.org/pypi/six/</a></li>
<li><a class="reference external" href="http://wiki.python.org/moin/Python3.0">http://wiki.python.org/moin/Python3.0</a></li>
<li><a class="reference external" href="http://ptgmedia.pearsoncmg.com/imprint_downloads/informit/promotions/python/python2python3.pdf">http://ptgmedia.pearsoncmg.com/imprint_downloads/informit/promotions/python/python2python3.pdf</a></li>
<li><a class="reference external" href="http://diveintopython3.org/porting-code-to-python-3-with-2to3.html">http://diveintopython3.org/porting-code-to-python-3-with-2to3.html</a></li>
<li><a class="reference external" href="http://pythonology.blogspot.com/2009/02/making-code-run-on-python-20-through-30.html">http://pythonology.blogspot.com/2009/02/making-code-run-on-python-20-through-30.html</a></li>
<li><a class="reference external" href="http://docs.python.org/library/2to3.html">http://docs.python.org/library/2to3.html</a></li>
<li><a class="reference external" href="http://pypi.python.org/pypi/3to2">http://pypi.python.org/pypi/3to2</a></li>
<li><a class="reference external" href="http://bitbucket.org/amentajo/lib3to2">http://bitbucket.org/amentajo/lib3to2</a></li>
<li><a class="reference external" href="http://wiki.python.org/moin/3to2">http://wiki.python.org/moin/3to2</a></li>
</ul>
</div>
</div>


          </div>
        </div>
      </div>
      <div class="sphinxsidebar">
        <div class="sphinxsidebarwrapper">
  <h3><a href="index.html">Table Of Contents</a></h3>
  <ul>
<li><a class="reference internal" href="#">Python 3 Porting Guide</a><ul>
<li><a class="reference internal" href="#introduction">Introduction</a></li>
<li><a class="reference internal" href="#organizational-changes">Organizational Changes</a><ul>
<li><a class="reference internal" href="#name-changes">Name Changes</a></li>
<li><a class="reference internal" href="#reorganization">Reorganization</a></li>
<li><a class="reference internal" href="#url-related-modules">URL-related modules</a><ul>
<li><a class="reference internal" href="#urllib">urllib</a></li>
<li><a class="reference internal" href="#urllib2">urllib2</a></li>
</ul>
</li>
<li><a class="reference internal" href="#optimized-modules">Optimized Modules</a></li>
</ul>
</li>
<li><a class="reference internal" href="#printing">Printing</a></li>
<li><a class="reference internal" href="#executing-arbitrary-code">Executing Arbitrary Code</a><ul>
<li><a class="reference internal" href="#exec-statement"><tt class="docutils literal"><span class="pre">exec</span></tt> Statement</a></li>
<li><a class="reference internal" href="#execfile-statement"><tt class="docutils literal"><span class="pre">execfile</span></tt> Statement</a></li>
</ul>
</li>
<li><a class="reference internal" href="#exceptions">Exceptions</a><ul>
<li><a class="reference internal" href="#raising-exceptions">Raising Exceptions</a></li>
<li><a class="reference internal" href="#handling-exceptions">Handling Exceptions</a></li>
<li><a class="reference internal" href="#exceptions-from-generators">Exceptions from Generators</a></li>
</ul>
</li>
<li><a class="reference internal" href="#division">Division</a><ul>
<li><a class="reference internal" href="#preparation-options">Preparation Options</a></li>
</ul>
</li>
<li><a class="reference internal" href="#long-integers">Long Integers</a></li>
<li><a class="reference internal" href="#iterators">Iterators</a><ul>
<li><a class="reference internal" href="#iterating">Iterating</a></li>
<li><a class="reference internal" href="#creating-iterators">Creating Iterators</a></li>
</ul>
</li>
<li><a class="reference internal" href="#dictionaries">Dictionaries</a><ul>
<li><a class="reference internal" href="#supporting-dictionary-views">Supporting Dictionary Views</a><ul>
<li><a class="reference internal" href="#supporting-2-7-and-3-x">Supporting 2.7 and 3.x</a></li>
<li><a class="reference internal" href="#supporting-pre-2-7-and-3-x">Supporting pre-2.7 and 3.x</a></li>
</ul>
</li>
<li><a class="reference internal" href="#replacing-iter-methods">Replacing <tt class="docutils literal"><span class="pre">iter*</span></tt> methods</a></li>
<li><a class="reference internal" href="#replacing-dict-has-key">Replacing <tt class="docutils literal"><span class="pre">dict.has_key()</span></tt></a></li>
</ul>
</li>
<li><a class="reference internal" href="#strategies">Strategies</a><ul>
<li><a class="reference internal" href="#single-codebase">Single Codebase</a><ul>
<li><a class="reference internal" href="#imports">Imports</a></li>
<li><a class="reference internal" href="#defeating-deprecation">Defeating Deprecation</a><ul>
<li><a class="reference internal" href="#introducing-six">Introducing <tt class="docutils literal"><span class="pre">six</span></tt></a></li>
</ul>
</li>
</ul>
</li>
<li><a class="reference internal" href="#pure-2-x-source">Pure 2.x Source</a><ul>
<li><a class="reference internal" href="#tests">Tests</a></li>
</ul>
</li>
<li><a class="reference internal" href="#pure-3-x-source">Pure 3.x Source</a></li>
</ul>
</li>
<li><a class="reference internal" href="#references">References</a></li>
</ul>
</li>
</ul>

  <h4>Previous topic</h4>
  <p class="topless"><a href="index.html"
                        title="previous chapter">Welcome to Porting to Python 3&#8217;s documentation!</a></p>
  <h4>Next topic</h4>
  <p class="topless"><a href="c-porting.html"
                        title="next chapter">Python 3 Extension Porting Guide</a></p>
  <h3>This Page</h3>
  <ul class="this-page-menu">
    <li><a href="_sources/py-porting.txt"
           rel="nofollow">Show Source</a></li>
  </ul>
<div id="searchbox" style="display: none">
  <h3>Quick search</h3>
    <form class="search" action="search.html" method="get">
      <input type="text" name="q" size="18" />
      <input type="submit" value="Go" />
      <input type="hidden" name="check_keywords" value="yes" />
      <input type="hidden" name="area" value="default" />
    </form>
    <p class="searchtip" style="font-size: 90%">
    Enter search terms or a module, class or function name.
    </p>
</div>
<script type="text/javascript">$('#searchbox').show(0);</script>
        </div>
      </div>
      <div class="clearer"></div>
    </div>
    <div class="related">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="genindex.html" title="General Index"
             >index</a></li>
        <li class="right" >
          <a href="c-porting.html" title="Python 3 Extension Porting Guide"
             >next</a> |</li>
        <li class="right" >
          <a href="index.html" title="Welcome to Porting to Python 3’s documentation!"
             >previous</a> |</li>
        <li><a href="index.html">Porting to Python 3 v1 documentation</a> &raquo;</li> 
      </ul>
    </div>
    <div class="footer">
        &copy; Copyright 2010, PSF Sprint Committee.
      Created using <a href="http://sphinx.pocoo.org/">Sphinx</a> 1.0b2+.
    </div>
  </body>
</html>