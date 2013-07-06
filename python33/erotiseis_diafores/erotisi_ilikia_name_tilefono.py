#rotaei kai ektiponei onoma kai ilikia
name=input("Πως σε λενε? ")
age=int(input("Ποια ειναι η ηλικια σου? "))
print ("Χαρηκα που σε γνωρισα ",name)
print (age, "χρονων δεν ειναι καθολου ασχημα!")
print ('*********************************************************')
#rotaei kai ektiponei ilikia me diki tou protasi
age=input("Ποσο χρονων εισαι?")
print (age,"χρονων? δεν ειναι και ασχημα.")
print ('---------------------------------------------------------------------------------------')
#rotaei kai ektiponei onoma me xairetismo
print ("Πως σε λενε?")
name=input()
print ("Γεια σου", name,('.'))
print ('---------------------------------------------------------------------------------------')
#rotaei ilikia me diafores apantiseis 
age=int(input("Ποσο χρονων εισαι?"))
if age > 70:
    print ("Είσαι μεγαλούτσικος")
if age < 10:
    print ("Είσαι νινί ακόμα")
if age < 70 and age > 10:
    print (age,"? Ε δεν ειναι και ασχημα")
print ('---------------------------------------------------------------------------------------')
#rotaei kai ektiponei onoma kai arithmo tilefonou
name=input('Δωσε ονομα. ')
a=int(input('Δωσε αριθμο τηλεφωνου. '))
print(name+' ο αριθμος τηλεφωνου ειναι ' + str(a))    
