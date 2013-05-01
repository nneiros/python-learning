ten_things = "milo portokali kota thlefono fota zaxari"

print ("Περιμένετε δεν υπάρχουν 10 πράγματα στον εν λόγω κατάλογο, ας διορθώσουμε.")

stuff = ten_things.split(' ')
more_stuff = ["day", "night", "song", "Frisbee", "kalampoki", "banana", "koritsi", "agori"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print ("Προσθέτοντας: "), next_one
    stuff.append(next_one)
    print ("Υπάρχουν % d πραγματα τώρα." % len(stuff))

print ("τωρα ειναι σωστα: "), stuff

print ("Ας δουμε κάποια πράγματα .")

print (stuff[1])
print (stuff[-1]) # whoa! fancy
print (stuff.pop())
print(' '.join(stuff)) # what? cool!
print ('#'.join(stuff[3:5])) # super stellar!
print('---------------------------------------------------------------------------------------------------------------')

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print ("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print ("Adding: "), next_one
    stuff.append(next_one)
    print ("There's %d items now." % len(stuff))

print ("There we go: "), stuff

print ("Let's do some things with stuff.")

print (stuff[1])
print (stuff[-1]) # whoa! fancy
print (stuff.pop())
print (' '.join(stuff)) # what? cool!
print ('#'.join(stuff[3:5])) # super stellar!
