#kanontas ena leksiko pio aplo
print('Κανοντας ενα λεξικο πιο απλο')
from collections import defaultdict
#s={('red' , 1),( 'blue' , 2),( 'red' , 3),('red' , 5)}
s=[('red',1),('blue',3),
     ('red',4),('blue',2),
     ('yellow',1),('yellow',1)]
print('Λεξικο:',s)
d = defaultdict(list)# set=add
keys=d.keys()
values=d.values()
for k,v in s:
     d[k].append(v)
print('Aπλοποιηση των διπλων:',list(d.items()))
print('Προσθετω τα διπλα:',({k:sum(v) for k, v in d.items()}))
print('------------------------------------------------------------')
#------------------------------------------------------------------
#leksiko me onoma kai noumero
print('Λεξικο με ονομα και νουμερο')
tel = {'Λακης': 4098, 'Σταματης': 4139}
tel['Βρασιδας'] = 4127
keys=list(tel.keys())#prepei prota na ta oriseis san keys
values=list(tel.values())#prepei prota na ta oriseis san values
print ('Λεξικο=',tel)
print ('Το τηλεφωνο του Λακης ειναι:',tel['Λακης'])
print('Διαγραφη του Σταματης.')
del tel['Σταματης']
tel['Δημητρης'] = 4127
print('Προσθετουμε το ονομα Δημητρης με νουμερο 4127.')
print ('Τωρα το λεξικο ειναι:',tel)
print ('To λεξικο εχει ονοματα:',list(keys))#ta ektiponeis san keys
print('Το λεξικο εχει αριθμους:', list(values))#ta ektiponeis san values
if ('Βρασιδας') in tel :
    print ('Το τηλεφωνο του Βρασιδας ειναι:',tel['Βρασιδας'])
print('------------------------------------------------------------')
#------------------------------------------------------------------
print('Λεξικο με ονοματα,τηλεφωνα και αγωνες ποδοσφαιρου.')
table1 = {'Nικος': 2105643127, 'Μαιρη': 2103454098, 'Ελενη': 6726737678}
print('Ονοματα'+'\t\tΤηλεφωνα')
for name,phone in table1.items():
    print('{0:10} ==> {1:10d}'.format(name,phone))
print('Aγωνες'+'\t\tΑποτελεσματα')
table={'agiax-milan': '3-2', 'torino-fiorentina': '1-2'}
for name, phone in table.items():
    print( '{0:10} =\t {1:10s}'.format(name, phone))
print('------------------------------------------------------------')
#------------------------------------------------------------------
print('Λεξικο με αγωνες ποδοσφαιρου.')
#lexiko me agones kai apotelesmata
# teams.py
teams = { #ομαδες
      0: ("Ajax Amsterdam", "Inter Milano"),
      1: ("Real Madrid", "AC Milano"),
      2: ("Dortmund", "Sparta Praha")
}
results = ("2-3", "3-3", "2-1")#αποτελεσματα
for i in teams:
   print (teams[i][0].ljust(16) + "-".ljust(5) + \
       teams[i][1].ljust(16) + results[i].ljust(3))
print('------------------------------------------------------------')
teams=[]
result=[]
a=input('Δωσε 1ο αγωνα.')
teams.append(a)
b=input('Δωσε αποτελεσμα.')
result.append(b)
a=input('Δωσε 2ο αγωνα.')
teams.append(a)
b=input('Δωσε αποτελεσμα.')
result.append(b)
print(teams[0]+'\t=>',result[0])
print(teams[1]+'\t=>',result[1])
print('------------------------------------------------------------')
#------------------------------------------------------------------
#paradigma lexikou kai ergasies se afto
ages = {}#λεξικο
#Add a couple of names to the dictionary
#ages['Sue'] = 23
#ages['Peter'] = 19
#ages['Andrew'] = 78
#ages['Karren'] = 45
ages={'Σια':23, 'Πετρος':19, 'Αντρεας':78, 'Κατερινα':45}
print ('Λεξικο=',ages)
print()
x=input('Δωσε ενα ονομα απο το λεξικο:')
if x in ages:
     print ((x), ('ειναι στο λεξικο.Ειναι') ,\
     ages [x], ('χρονων.'))
else:
     print ((x), " δεν ειναι στο λεξικο")
print()
keys=list(ages.keys())
values=list(ages.values())
print ("Στο λεξικο υπαρχουν:" ,list(keys))
print ()
print ('Αυτοι εχουν ηλικια αντιστοιχα:', list(values))
print()
#Put it in a list:
print ('Το λεξικο εχει ονοματα=',list(keys))
print ()
print ('Τα βαζω σε αλφαβητικη σειρα=',sorted(keys))
print()
print ('Το λεξικο εχει ηλικιες=',list(values))
print()
print ('Βαζω τις ηλικιες σε αυξουσα σειρα=',sorted(values))
print()
#You can find the number of entries
#with the len() function:
print (("Tο λεξικο περιεχει"), \
len(ages), ("καταχωρησεις."))
#---------------------------------------------------------------------
print('-----------------Αλλο λεξικο----------------------')
D = {'b': 2, 'c': 3, 'a': 1, 'd': 4}
keys=list(D.keys())
values=list(D.values())
items=list(D.items())
print('Λεξικο=',items)                        
print('Λεξικο θεση 1=',items[1])
print('Τιμη θεση 0 =',values[0])
print('Κλειδι θεση 3=',keys[3])
print ('Κλειδια,χωρις σειρα.',list(keys))# Unordered keys list
print('Τιμες χωρις σειρα.',list(values))                            
print ('Κλειδια με σειρα.',sorted(keys)) # Sorted keys list 
print ('Τιμες με σειρα.',sorted(values)) # Sorted values list 
print('Λεξικο κατακορυφα χωρις σειρα')
for keys in D:                       # Iterate though sorted keys
    print (keys, '=>', D[keys] )
print('Λεξικο κατακορυφα με σειρα κλειδιων.')
for keys in sorted(D):
    print (keys, '=>', D[keys])
