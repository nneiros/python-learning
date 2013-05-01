fo = open("foo.txt", "wb")
fo.write( "Ο πυθωνας ειναι η καλυτερη γλωσσα.\nΝαι ειναι η καλυτερη!!\n");
#str = fo.read(10);
#print ("Read String is : "), str
fo.close()
fo = open("foo.txt", "r+")
print "Διαβαζω ολο το αρχειο=", fo.read()
fo = open("foo.txt", "r+")
str = fo.read(20);#διαβαζει απο το αρχειο 20 στοιχεια
print "Διαβαζω απο το αρχειο μονο τα 20 στοιχεια : ", str
fo.close()
