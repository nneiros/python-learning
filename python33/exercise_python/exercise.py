def numberList(items):
    '''Print each item in a list items, numbered in order.'''
    number = 1
    for item in items:
        print(number, item)
        number = number + 1

def main():
    numberList(['red', 'orange', 'yellow', 'green'])
    print()
    numberList(['apples', 'pears', 'bananas'])

main()
print('------------------------------------')

print(sum([5, 2, 4, 7]))
print('------------------------------------')
for count in [1, 2, 3]:
    print(count)
    print('Yes' * count)
print('Done counting.')
for color in ['red', 'blue', 'green']:
    print(color)
print('------------------------------------')
print(list(range(4)))
print(list(range(10)) ) 
print('------------------------------------')
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
print('------------------------------------')
list = [4, 5, 7, 8, 9, 1,0,7,10]
print('lista=',list)
list.sort()
prev = list[0]
del list[0]
print('sort kai afiresh toy 0 stoixeioy',list)
for item in list:
    if prev == item:
        print ("Duplicate of ",prev," Found")
    prev = item
print('--------------')
l = [4, 5, 7, 8, 9, 1,0,7,10]
print ("l = [4, 5, 7, 8, 9, 1,0,7,10]","\tl:",l)
l.sort()
print ("l.sort()","\tl:",l)
prev = l[0]
print ("prev = l[0]","\tprev:",prev)
del l[0]
print ("del l[0]","\tl:",l)
for item in l:
    if prev == item:
        print ("Duplicate of ",prev," Found")
    print ("if prev == item:","\tprev:",prev,"\titem:",item)
    prev = item
    print ("prev = item","\t\tprev:",prev,"\titem:",item)
