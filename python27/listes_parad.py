a=['london','rome',1452,9] # κατασκευη λιστας
print (a)
print (a[0])#εκτυπωση της θεσης 0 της λιστας=london,[0,1,2,3,4....] ή [....-3,-2,-1]
print (a[2])#εκτυπωση της θεσης 2 της λιστας
print (a[0 ] + a[1])# προσθετει τις δυο θεσεις απο την λιστα [0+1]
print (a[2] + a[3])# προσθετει τις δυο θεσεις απο την λιστα [2+3],προσοχη ομως γιατι 2=rome=strings
#print (a[0] + a[2])# βγαζει μηνυμα λαθους γιατι και τα δυο εχουν μελη=strings
print (a[3])
print (a[-1])
print (a[1:3])# εκτυπωση των θεσεων 1 εως 3 χωρις να εχει το 3.
print (a[1:-1])# εκτυπωση των θεσεων με αρνητικους αριθμους
print (a[:3])  # εκτυπωση των θεσεων 0 εως 3, το 0 το εννοει.
a.append(114)# προσθεσε τo 114 στη λιστα
print (a)
a.insert(2,'paris')# προσθετει νεο μελος σε συγκεκριμενη θεση
print (a)
a.extend(['milano',1812])#προσθετει στο τελος της λιστας
print (a)
a.remove(9)#αφαιρουμε απο τη λιστα ενα γνωστο μελος[0,1,2....]
print (a)
c=a.pop()# αφαιρει το τελευταιο μελος της λιστας και το επιστρεφει
print (c) # εκτυπωση του τελευταιου μελους για να ξερουμε
print (a) # εκτυπωση για επαληθευση
print (a.index(1452)) # σε ενα γνωστο στοιχειο της λιστας μας επιστρεφει την (θεση του) στη λιστα
print (len (a))# παιρνω το αθροισμα των μελων μιας λιστας
# αν ειναι αριθμοι παιρνω το αθροισμα τους a=[1,2,3,4]->sum(a)=10
print range (8)# εκτυπωση ενος συνολου αριθμων
print range (5,15)#εκτυπωση ενος συνολου αριθμων
print range (0,30,5) #to 5 einai vima
print range (100,0,-20)
