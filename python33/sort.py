print (sorted([5,3,4,1,2]))#βαζει στη σειρα αριθμητικα
print(sorted("αυτο ειναι περι μωρο δηλαδη καθολου βαδιζω".split(), key=str.lower))#βαζει στη σειρα αλφαβητικα

a = ['λονδινο','ρωμη',1452,9]
print (a)
a.append(114)#προσθετει το 114 στο τελος
print(a)
a.insert(2,'παρισι')#προσθετει στη θεση 2 το παρισι
print (a)
a.remove('ρωμη')#αφαιρει την ρωμη
print (a)

student_tuples = [
       ('Γιαννης', 'A', 15),
       ('Τζινα', 'B', 12),
       ('Βρασιδας', 'B', 10),
        ]
print (sorted(student_tuples, key=lambda student: student[2]))   # sort με ηλικια
