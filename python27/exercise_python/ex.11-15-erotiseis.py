print "ποια ειναι η ηλικια σου?",
age = raw_input()
print "ποσο υψος εχεις?",
height = raw_input()
print "ποσο ειναι το βαρος σου?",
weight = raw_input()

print "εσυ εισαι %r χρονων, εχεις %r υψος και  %r κιλα βαρος." % (
    age, height, weight)
print('--------------------------------------------------------------------------------------------')
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tτον υπεροχο κοσμο
with logic so firmly planted
δεν μπορει να διακρινει \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\t,οπου δεν υπαρχει κανεις.
"""
print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "αυτο θα πρεπει να ειναι πεντε: %s" % five
def secret_formula(started):
      jelly_beans = started * 500
      jars = jelly_beans / 1000
      crates = jars / 100
      return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
