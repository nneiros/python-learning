print('Λιστα=5,3,4,1,2')
print ('Λιστα με ταξινομηση αριθμητικα=',sorted([5,3,4,1,2]))#βαζει στη σειρα αριθμητικα
print('******************************************************************************')
print('Λιστα=αυτο ειναι περι μωρο δηλαδη καθολου βαδιζω')
print('Λιστα με ταξινομηση αλφαβητικα=',sorted("αυτο ειναι περι μωρο δηλαδη καθολου βαδιζω".split(), key=str.lower))#βαζει στη σειρα αλφαβητικα
print('******************************************************************************')
a = ['Λονδινο','Ρωμη',1452,9]
print ('Λιστα=',a)
a.append(114)#προσθετει το 114 στο τελος
print('Προσθεσαμε το 114 στο τελος=',a)
a.insert(2,'Παρισι')#προσθετει στη θεση 2 το παρισι
print ('Προσθεσαμε το Παρισι στη θεση 2=',a)
a.remove('Ρωμη')#αφαιρει την ρωμη
print ('Αφαιρεσαμε την Ρωμη=',a)
print('******************************************************************************')
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
