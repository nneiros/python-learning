fo = open("foo.txt", "w")
fo.write( "Ο πυθωνας ειναι η καλυτερη γλωσσα.\nΝαι ειναι η καλυτερη!!\n");
#str = fo.read(10);
#print ("Read String is : "), str
fo.close()
fo = open("foo.txt", "r+")
print (("Διαβαζω ολο το αρχειο="), fo.read())
fo = open("foo.txt", "r+")
str = fo.read(40);#διαβαζει απο το αρχειο 40 στοιχεια
print (("Διαβαζω απο το αρχειο μονο τα 40 στοιχεια : "), str)
fo.close()
