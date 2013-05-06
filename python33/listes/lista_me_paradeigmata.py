# Εδώ θα βρείτε τα παραδείγματα που παρουσιαστηκαν στο 7ο
# μέρος του οδηγου "Μαθαινοντας την Python" όπως δημοσιεύθηκε
# στο www.GreekTuts.net.
# Λίστες
# Δηλώνονται σε τετραγωνικές αγκύλες [ ... ] και μπορούν να περιέχουν οποιονδήποτε τύπο
# δεδομενων που υποστηρίζεται από την Python

myList = ['monty', 'γατι', 999, 222]
print ('....Εμφανίζει την λίστα στην κονσόλα...')
print('Ολη η λιστα=', myList )         # Εμφανίζει την λίστα στην κονσόλα
print( 'Εμφανιση του στοιχειου "0" της λιστας=',myList[0] ) # Εμφανίζει το πρώτο στοιχειο της λίστας
print('Εμφανιση του στοιχειου "-1"=', myList[-1] )     # Εμφανίζει το τελευταίο στοιχείο της λίστας
print('Ολα εκτος του 1ου και του τελευταιου', myList[1:-1] )   # Εμφανίζει όλα τα στοιχεια εκτός του πρώτου και του τελευταίου
print('---------------------------------------------------------------------------------------')
print('....Εισαγωγή, διαγραφή και τροποποίηση στοιχειων λιστών...' )
# Εισαγωγή, διαγραφή και τροποποίηση στοιχειων λιστών
myList[1:1] = ['λιαν', 'τρελο']   # Εισαγωγή στοιχείων
print('Εισαγωγη του "λιαν" και του "τρελο"=', myList )

myList[0:2] = []                # Διαγραφή στοιχειων
print('Διαγραφη στοιχειων=', myList )

myList[0:2] = [1, 12]           # Τροποποίηση στοιχείων
print('Τα στοιχεια 0:2 γινονται 1,2=', myList )

myList[:0] = myList             # Εισαγωγή ενός αντιγράφου της λίστας στην αρχή της
print('Εισαγωγη αντιγραφου της λιστας=', myList )

myList[:] = []                  # Καθαρισμός της λίστας
print( 'Καθαρισμος της λιστας=',myList )
#print()
print('---------------------------------------------------------------------------------------')
myList = [1, 2, 3, 4, 5]
x=( len( myList ) )          # Επιστρέφει το μέγεθος της λίστας
print('H νεα λιστα ειναι=',myList)
print('Το μεγεθος της λιστας ειναι len=',x)
print('---------------------------------------------------------------------------------------')

# Εμφωλευμένες Λίστες
myNestedList = ["γιορτη", "παρων"]
myList = [myNestedList, "οκ", "monty", "κεραια"]    # Μια λίστα μπορεί να ειναι μελος μιας άλλης λίστας
print( 'Mια λιστα μεσα σε αλλη=',myList )
print()
print('--- ΠΡΟΧΩΡΗΜΕΝΕΣ ΕΝΝΟΙΕΣ ΣΤΗΝ ΧΡΗΣΗ ΛΙΣΤΩΝ ---')
print()
# Προσθήκη στοιχείου στο τέλος της λίστας
print( 'Η λιστα ειναι=',myList )
print()

# Προσθέτει ένα στοιχειο στο τέλος της λίστας
myList.append('μωρο')
print('Προσθετει το "μωρο"=', myList )
print()

anotherList = ['κερι', 'μελι']
print ('Aλλη λιστα=',anotherList)
# Επεκτείνει μια λίστα προσθέτοντας στο τέλος τα στοιχεια μιας άλλης λίστας
myList.extend( anotherList )
print('Προσθετει στο τελος την αλλη λιστα=', myList )
print()

# Εισάγει το στοιχείο 'inserted' στη θέση 0 (δηλαδή την πρώτη)
myList.insert(0, 'kalos ton')
print('Εισαγωγη στη θεση 0 το kalos ton=', myList )
print()

# Αφαιρει το στοιχειο με τιμή 'inserted'
myList.remove('kalos ton')
print('Aφαιρεση του στοιχειου kalos ton', myList )
print()

# Επιστρέφει το τελευταιο στοιχειο της λιστας διαγράφοντάς το από την λίστα
print('Επιστροφη του τελευταιου στοιχειου και το διαγραφει=',myList.pop())
print( 'Λιστα =',myList ) 
print()

# Επιστρέφει το στοιχειο στη θέση 0 διαγράφοντάς το από τη λίστα
print('Διαγραφη του στοιχειου 0[γιορτη,παρων]=',myList.pop(0))
print('Απομενει η λιστα=', myList ) 
print()

# Επιστρέφει την θέση του στοιχείου με τιμή 'Monty'
print('το στοιχειο monty ειναι στη θεση=',myList.index('monty'))
print( myList ) 
print()

numList = [1, 15, 25, 2, 8, 19, 1012, 3]
print('Η λιστα ειναι=', numList )
print()

# Ταξινομει τα στοιχεια της λίστας σε αύξουσα σειρά
numList.sort()
print('ταξινομηση λιστας=', numList ) 
print()

# Αντιστρέφει την λίστα σε επίπεδο στοιχειων
numList.reverse()
print( 'αντιστροφη λιστας=',numList ) 
print()