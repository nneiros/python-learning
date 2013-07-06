# python λιστα,πινακας
x = [['a','b','c'],['4','5','6'],['7','8','9']]
print('H πρωτη στηλη λιστας.')
for i in x:
  print( i[0])
print ('Η λιστα σαν πινακας.')
for i in x:
  print (i)
print ('Η πρωτη σειρα.')
for i in x[0]:
  print (i)
print('Η τελευταια σειρα',x[-1])
print('**************************************************************')
#πινακας,λιστα
x = [['1','2','3'],['4','5','6'],['7','8','9']]
print('Λιστα',x)
print ('Oλη η λιστα πινακας')
for xlist in x:
    s = ""
    for n in xlist:
        s = "%s, %c" %(s,n)
    print (s[2:])
print ('2η και 3η στηλη.')
for xlist in x:
    s = ""
    for n in xlist:
        s = "%s, %c"%(s,n)
    print (s[4:])
print ('Η πρωτη στηλη.')
for xlist in x:
    s = ""
    for n in xlist:
        s = "%s, %c"%(s,n)
    print (s[1:3]) 


