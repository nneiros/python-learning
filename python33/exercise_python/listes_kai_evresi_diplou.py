def numberList(items):
    '''Print each item in a list items, numbered in order.'''
    number = 1
    for item in items:
        print(number, item)
        number = number + 1

def main():
    numberList(['κοκκινο', 'πορτοκαλι', 'κιτρινο', 'πρασινο'])
    print()
    numberList(['μηλα', 'αχλαδια', 'μπανανες'])

main()
print('-------------------------------------------------------------------------------------------------------------')

print('προσθεση:5+2+4+7=',sum([5, 2, 4, 7]))
print('-----------------------------------------------------------------------------------------------------------')
print('Μετρωντας Nαι.')
for count in [1, 2, 3]:
    print(count)
    print('Ναι' * count)
print('--------------------------------------------------------------------------------------------------------')
color=['κοκκινο', 'μπλε', 'πρασινο']
print('Xρωμα οριζοντια:',color)
print('Xρωμα κατακορυφα:')
for d in color:
    print(d)
print('------------------------------------')
print('Λιστα με μεγεθος 4=',list(range(4)))
print('Λιστα με μεγεθος 10=',list(range(10)))  
print('-------------------------------------------------------------------------------------------------------')
a = 1
s = 0
print ('Δωσε αριθμο για προσθεση.')
print ('Δωσε 0 για εξοδο.')
while a != 0:
    print ('Υπολογισε αθροισμα: ', s)
    a = input('Αριθμος? ')
    a = float(a)
    s += a
print ('Συνολικο αθροισμα = ',s)
print('---------------------------------------------------------------------------------------------------------')
list = [4, 5, 7, 8, 9, 1,0,7,10]
print('Λιστα=',list)
list.sort()
print('Ταξινομηση λιστας',list)
prev = list[2]
print ("Επεστρεψε το στοιχειο στη θεση 2:",prev)
del list[0]
print('Aφαιρεση του 0 στοιχειου',list)

for item in list:
    if prev == item:
        print ("Διπλο ",prev," βρηκα.")
    prev = item
print('-------------------------------------------------------------------------------------------------------')
d = [4, 5, 7, 8, 9, 1,0,7,10]
print ('Λιστα:,\td:',d)
d.sort()
print ('Ταξινoμηση: \td:',d)
prev = d[0]
print ("Επεστρεψε το στοιχειο στη θεση 0:","\tστοιχειο:",prev)
del d[0]
print ('Αφαιρεση του 0 στοιχειου: , \td: ',d)
print('Επεξεργασια της λιστας για να βρει τα διπλα:')
for item in d:
    if prev == item:
        print ("Διπλο",prev," βρηκα")
    print ("αν προηγουμενο == στοιχειο:","\t:",prev,"\t==",item)
    prev = item
    print ("προηγουμενο = στοιχειο","\t\t:",prev,"\t=",item)
print('--------------------------------------------------------------------------------------------------------')
list = ['α','δ','γ','κ','λ','ο','π','υ','α','δ','ξ','ε','τ','λ','φο']
list.sort()
prev = list[0]
del list[0]
for item in list:
    if prev == item:
        print ("Διπλο ",prev," βρηκα")
    prev = item
