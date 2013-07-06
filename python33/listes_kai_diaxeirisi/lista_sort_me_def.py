#φτιαχνει λεξικο με επικεφαλιδα το πρωτο γραμμα
from itertools import groupby
from operator import itemgetter
somelist = ['About', 'Absolutely','Βοδι', 'Alabama',  'Aunt', 'Behind', 'Biblical', 'Ωραιος','Αρχειο']
for letter, words in groupby(sorted(somelist), key=itemgetter(0)):
        print('-',letter,'-')
        for word in words:
            print (word)
        print
print('******************************************************************************')
#--------------------------------------------------
#diaxeirisi listas me class kai def
class lista:
        def __init__(self,items):
                self.items=items
        def print(self):
                return self.items
        def sortnumber(self):
                return sorted(self.items)
        def listalfa(self):
                return sorted(self.items.split(), key=str.lower)#βαζει στη σειρα αλφαβητικα
listnumber=lista([5,3,4,1,2])       
print('Λιστα=',listnumber.print())
print('Λιστα με ταξινομηση αριθμητικα=',listnumber.sortnumber())#βαζει στη σειρα αριθμητικα        
print('******************************************************************************')
listalfarithm=lista('αυτο ειναι περι μωρο δηλαδη καθολου βαδιζω' )
print('Λιστα=',listalfarithm.print())
#a=listalfarithm.split()#to kano prota lista
print('Λιστα με ταξινομηση αλφαβητικα=',listalfarithm.listalfa())
print('******************************************************************************')
listmix=['Λονδινο','Ρωμη',1452,9]
print ('Λιστα=',listmix)
def  append_list(x):
        listmix.append(x)
def insert_list(y,x):
        listmix.insert(y,x)
def remove_list(x):
        listmix.remove(x)
append_list(114)#προσθετει το 114 στο τελος
print('Προσθεσαμε το 114 στο τελος=',listmix)
insert_list(2,'Παρισι')#προσθετει στη θεση 2 το Παρισι
print ('Προσθεσαμε το Παρισι στη θεση 2=',listmix)
remove_list('Ρωμη')
print ('Αφαιρεσαμε την Ρωμη=',listmix)
print('******************************************************************************')
#ταξινομηση λεξικου με τρια στοιχεια(ονομα,βαθμο και ηλικια)
class Student:
        def __init__(self, name, grade, age):
            self.name = name
            self.grade = grade
            self.age = age
        def __repr__(self):
            return repr((self.name, self.grade, self.age))
student_objects = [
Student ('Γιαννης' ,'A', 15),
Student ('Τζινα', 'B', 12),
Student ('Βρασιδας', 'B', 10),
        ]
print ('Λιστα=',student_objects)
print('Λιστα με ταξινομηση oνοματος=',sorted(student_objects, key=lambda student:student.name))
print('Λιστα με ταξινομηση βαθμου=',sorted(student_objects, key=lambda student:student.grade))
print ('Λιστα με ταξινομηση ηλικιας=',sorted(student_objects, key=lambda student: student.age))#sort με ηλικια
#print('Λιστα με ταξινομηση oνοματος=',list(student_objects,student:student.name))
#print(sorted(students, key=name.__getitem__))
