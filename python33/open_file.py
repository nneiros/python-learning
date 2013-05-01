print ("Δημιουργια ενος txt αρχειου με την write() μεθοδο........")
text_file = open("foo.txt", "w")
text_file.write("Αυτη ειναι γραμμη 1\n")
text_file.write("Αυτη ειναι γραμμη 2\n")
text_file.write("Αυτη ειναι γραμμη 3\n")
text_file.close()
print('---------------------------------------------------------------------------------------')  

print ("\nΔιαβασε το αρχειο γραμμη,γραμμη..........")
text_file = open("foo.txt", "r")
print (text_file.readline())
print (text_file.readline())
print (text_file.readline())
text_file.close()
print('---------------------------------------------------------------------------------------')

print ("\nΔιαβασε το αρχειο σε οριζοντια γραμμη και σε καθετη...........")
text_file = open("foo.txt", "r")
lines = text_file.readlines()
print (lines)# δινει το αρχειο σε οριζοντια γραμμη
print('---------------------------------------------------------------------')
x=(len(lines))# δινει το συνολο σε αριθμο των γραμμων
print('To συνολο των γραμμων ειναι=',x)
print('-----------------------------------------------------------------------')
for line in lines:# δινει το αρχειο σε κατακορυφη γραμμη
    print (line)
text_file.close()
print('---------------------------------------------------------------------------------------')

f = open('somefile.txt', 'w')
f.write('Γεια σου, ')
f.write('Κοσμε!')
f.close()
print ("\nLooping με το περιεχομενο ενος αρχειου, γραμμη,γραμμη...............")
text_file = open("somefile.txt", "r")
for line in text_file:
    print (line)
text_file.close()
print('---------------------------------------------------------------------------------------')

print ("\n Διαβασε χαρακτηρες απο το αρχειο...............")
text_file = open("somefile.txt", "r")
print (text_file.read(1))
print (text_file.read(5))
text_file.close()
print('---------------------------------------------------------------------------------------')

print ("\nΔιαβαζοντας ολοκληρο το αρχειο................")
text_file = open("somefile.txt", "r")
whole_thing = text_file.read()
print (whole_thing)
text_file.close()
print('---------------------------------------------------------------------------------------')

print ("\n Κατασκευη ενος txt αρχειου με την writelines() μεθοδο...............")
text_file = open("write_it.txt", "w")
#x=text_file
lines = ["Line 1\n",
         "This is line 2\n",
         "That makes this line 3\n"]
text_file.writelines(lines)
#print(text_file)
text_file.close()
print('---------------------------------------------------------------------------------------')

ilikia= 20
onoma = "Βρασιδας"
print ("Ο {1}, ειναι τωρα {0} χρονων και πολυ ψηλος.................".format (ilikia, onoma))
print('---------------------------------------------------------------------------------------')

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)
something = input('Δωσε τη λεξη: ')
if (is_palindrome(something)):
    print("Ναι, αυτη η λεξη την διαβαζουν και απο τις δυο κατευθυνσεις")
else:
    print("Οχι, αυτη η λεξη δεν την διαβαζουν και απο τις δυο κατευθυνσεις")
#.......
#.......
print('---------------------------------------------------------------------------------------')

import pickle
# το αρχειο που θα αποθηκευτουν τα δεδομενα
shoplistfile = 'shoplist.data'

# λιστα με τα πραγματα που θα αγορασω 
shoplist = 'μηλο', 'πορτοκαλι', 'καροτο'
                
               
# Write to the file
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) # dump the object to a file
f.close()

del shoplist # destroy the shoplist variable

# Read back from the storage
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # load the object from the file
#for line in storedlist:
print('....Η λιστα εχει',storedlist) 
f.close()
#(storedlist)
