#A few examples of a dictionary
#First we define the dictionary
#it will have nothing in it this time
ages = {}#λεξικο

#Add a couple of names to the dictionary
ages['Sue'] = 23
ages['Peter'] = 19
ages['Andrew'] = 78
ages['Karren'] = 45

#Use the function has_key() - 
#This function takes this form:
#function_name.has_key(key-name)
#It returns TRUE
#if the dictionary has key-name in it
#but returns FALSE if it doesn't.
#Remember - this is how 'if' statements work -
#they run if something is true
#and they don't when something is false.
if ages.has_key('Sue'):
     print ("Sue ειναι στο λεξικο. Αυτη ειναι"), \
   ages['Sue'], "χρονων."

else:
    print ("Sue δεν ειναι στο λεξικο")

#Use the function keys() - 
#This function returns a list
#of all the names of the keys.
#E.g.
print ("Επισης ειναι στο λεξικο:")
print (ages.keys())

#You could use this function to
#put all the key names in a list:
keys = ages.keys()

#You can also get a list
#of all the values in a dictionary.
#You use the values() function:
print ("Αυτοι εχουν ηλικια αντιστοιχα:"), \
ages.values()

#Put it in a list:
values = ages.values()

#You can sort lists, with the sort() function
#It will sort all values in a list
#alphabetically, numerically, etc...
#You can't sort dictionaries - 
#they are in no particular order
print 'Το λεξικο εχει ονοματα=',(keys)
keys.sort()
print 'Τα βαζω σε αλφαβητικη σειρα=',(keys)

print 'Το λεξικο εχει ηλικιες=',(values)
values.sort()
print 'Βαζω τις ηλικιες σε αυξουσα σειρα=',(values)

#You can find the number of entries
#with the len() function:
print ("Tο λεξικο περιεχει"), \
len(ages), "καταχωρησεις."
