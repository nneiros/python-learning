

print('--------------------------------------------------------------------------------------------------')
#----------------------------------------------------------------------------------------------------------------------------
print ("Εισαγωγη αντικειμενου")
name= input ("Δωσε το ονομα σου:")
number= int(input("Αριθμος:"))
onomasia = input("Ονομασια:")
print (name,'\n', "Αριθμος", number,"Ονομασια", onomasia, ) 

print('--------------------------------------------------------------------------------------------------')
#----------------------------------------------------------------------------------------------------------------------------
import math
def ask_ok(prompt, retries=4, complaint='Παρακαλώ Ν)αί,n,ν / Ο)χι,ο,ο' ):
    while True:
        ok = input(prompt)
        if ok in ['ν', 'Ν', 'n', 'N']: return True   # έλεγχος αν η απάντηση αντιστοιχεί σε μία
        if ok in ['o', 'O', 'o', 'O']: return False  #  απ’ τις τιμές
        retries = retries - 1
        if retries < 0: raise IOError  ('Απογόρευση πρόσβασης ')
        print(complaint)# Θα εμφανίσει το ενημερωτικό μήνυμα...
z=ask_ok('Eξοδος???')
if z==False :
	print ("Kακως")
print('--------------------------------------------------------------------------------------------------')
#----------------------------------------------------------------------------------------------------------------------------
#evresi logarithmou me def
def printMultiples(x):
   x=1.0
   print('Ευρεση λογαριθμου απο το 1 εως το 10 με ορισμο.')
   while x<=10:
      print( x, '\t',math.log(x))
      x=x+1 
i=1
while i <= 1:
    printMultiples(i)
    i=i+1
print('-----------------------------------------------------------------------------------------------')
#----------------------------------------------------------------------------------------------------------------------------
#tipose diaforous arithmous
i = 5
def f(arg=i):
   print('Tυπωσε τoν αριθμο',arg)
i = 6
f()
f(i)
i=18
f(i)
#---------------------------------------------------------------------------------------------------------------------------
print('---------------------------------------------------------------------------------------------')
#kataskevi listas me tria meli kai def
def f(a, L=[]):
   L.append(a)
   return L
print('Aρχη λιστας',f(1))
print('Προσθετω μελος',f(2))
print('Προσθετω δευτερο μελος',f(3))
print ('--------------------------------------------------------------------------------------------')
#---------------------------------------------------------------------------------------------------------------------------
#kataskevi listas me tria meli kai def
def f(a, L=[ ]):
    if L is [ ]:
        L = [ ]
    L.append(a)
    return L
    f(1)
    f(2)
    f(3)
print('Aρχη λιστας',f(1))
print('Προσθετω μελος', f(2))
print('Προσθετω δευτερο μελος', f(3))
#-------------------------------------------------------------------------------------------------------------------------
print('-----------------------------------------------------------------------------------------')
#lista gia statistiki
n = [1, 2, 3, 4, 5]
def stats(x):
    mx = max(x)
    mn = min(x)
    ln = len(x)
    sm = sum(x)
    return mx, mn, ln, sm    
mx, mn, ln, sm = stats(n)
print( 'Λιστα',n)
print ('Μεγιστο=',mx,'Ελαχιστο=' ,mn,'Μεγεθος λιστας=' ,ln,'Αθροισμα=', sm)
print('-------------------------------------------------------------------------------------------')
#-------------------------------------------------------------------------------------------------------------------------
#lista me anadiataxi
def perm(l):
        # Compute the list of all permutations of l
    if len(l) <= 1:
                  return [l]
    r = []  # here is new list with all permutations!
    for i in range(len(l)):
             s = l[:i] + l[i+1:]
             p = perm(s)
             for x in p:
              r.append(l[i:i+1] + x)
    return r
a=[1,2,3]
print('Λιστα',a)
print('Aναδιαταξη της λιστας',perm(a))
#---------------------------------------------------------------------------------------------------------------------------
print('--------------------------------------------------------------------------------------')
#grapse kati kai telos gia na figeis
while True:
    s=input('Γραψε κατι(με τελος φευγεις):')
    print(s)
    if s == 'τελος':
        break
#---------------------------------------------------------------------------------------------------------------------------
print ('--------------------------------------------------------------------------------------------')
#σε καθε στοιχειο προσθετω το 42
# Lambda Forms
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
print ('Στοιχειο 0=',f(0))
print ('Στοιχειο 1=',f(1))
print ('Στοιχειο 15=',f(15))
print('Στοιχειο 42=',f(42))
#---------------------------------------------------------------------------------------------------------------------------
print ('--------------------------------------------------------------------------------------------------')
#grapse kati tris fores
st = input("Δωσε στοιχειο να το γραψω 3 φορες:")
print (st)
st=st*3  # triple the string
print (st)
#---------------------------------------------------------------------------------------------------------------------------
print ('--------------------------------------------------------------------------------------------------')
#evresi pragmatikou kai fantastikou arithmou
import math
a=2+3j
b=2-3j
print('a=',a)
print('b=',b)
print ('a*a=',a*a)
print ('a*b=',a*b)
print ('Πραγματικος του a=',a.real)
print ('Φανταστικος του b=',b.imag)
#---------------------------------------------------------------------------------------------------------------------------
print ('------------------------------------------------------------------------------------------------')
#apli evresi logarithmou
x=1.0
print('Ευρεση λογαριθμου απο το 1 εως το 10')
while x<=10:
    print( x, '\t',math.log(x))
    x=x+1
print ('-----------------------------------------------------------------------------------------------')
#----------------------------------------------------------------------------------------------------------------------------
#polaplasia tou 2
print('Κατασκευη πινακα με πολλαπλασια του 2')
i=1
while i<=6:
    print(2*i,'\t', end=' ')
    i=i+1
print()
print('------------------------------------------------------------------------------------------------')
#----------------------------------------------------------------------------------------------------------------------------
#polapalsia apo 1 eos 6
print('Πολλαπλασια απο 1 εως 6')
def printMultiples(n):
    i = 1
    while i <= 6:
        print(n*i, '\t', end=' ')
        i=i+1
    print()
i=1
while i <= 6:
    printMultiples(i)
    i=i+1
print('-----------------------------------------------------------------------------------------------')
#----------------------------------------------------------------------------------------------------------------------------
#tetragona tou 2,apo 0 eos 5 ana 0,5
x=0.0
print('Tα τετραγωνα του 2,απο 0 εως το 5.')
while  x<=5:
    print(x, '\t', x**2)
    x=x+0.5
#----------------------------------------------------------------------------------------------------------------------------
print ('------------------------------------------------------------------------------------------')
#tetragoniki riza apo 1 eos 10 ana 2
import math
x=1.0
print('H τετραγωνικη ριζα αριθμων απο 1 εως 10 ανα 2 αριθμους.')
while x<=10:
    print(x, '\t', math.sqrt(x))
    x=x+2
print ('-----------------------------------------------------------------------------------------')
#----------------------------------------------------------------------------------------------------------------------------
