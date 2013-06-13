ten_things = 'μηλα πορτοκαλια κορακια τηλεφωνο φωτα ζαχαρη'
print('Λιστα=',ten_things)

print ("Περιμένετε δεν υπάρχουν 10 πράγματα στον εν λόγω κατάλογο, ας διορθώσουμε.")

stuff = ten_things.split( )
more_stuff = ["ημερα", "νυχτα", "τραγουδι", "Frisbee", "καλαμποκι", "μπανανα", "κοριτσι", "αγορι"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print ("Προσθέτοντας: ", next_one)
    stuff.append(next_one)
    print(stuff)
    print ("Υπάρχουν % d πραγματα τώρα." % len(stuff))

print ("Τωρα ειναι σωστα: "), stuff

print ("Ας δουμε κάποια πράγματα .")

print ('Θεση 1=',stuff[1])
print ('Θεση -1(τελευταια στην αρχικη λιστα)=',stuff[-1]) # whoa! fancy
print ('Διαγραφη τελευταιας θεσης=',stuff.pop())
print('Τωρα εμειναν=',' '.join(stuff)) # what? cool!
print ('Εκτυπωση θεση 3 εως 5=', '#'.join(stuff[3:5])) # super stellar!
print('---------------------------------------------------------------------------------------------------------------')

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print ("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print ("Adding: ", next_one)
    stuff.append(next_one)
    print ("There's %d items now." % len(stuff))

print ("There we go: ", stuff)

print ("Let's do some things with stuff.")

print (stuff[1])
print (stuff[-1]) # whoa! fancy
print (stuff.pop())
print (' '.join(stuff)) # what? cool!
print ('#'.join(stuff[3:5])) # super stellar!
