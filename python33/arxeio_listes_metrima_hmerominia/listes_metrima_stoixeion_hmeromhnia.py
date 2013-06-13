
print ( ' τιμη = {0:2d} ' . format (12) ) # value = 12   
print ( ' τιμη = {0:2b} ' . format (12) )
print('----------------------------------------------------------------------')
a = complex(1 , 1)
b = complex(1 , 2)
print ('Πινακας μιγαδικων,a(1,1)..a=',a)
print ('Πινακας μιγαδικων,a(1,2)..b=',b)
print ('Πινακας μιγαδικων,a+b=', a+b)#migadikoi
print ('Πινακας μιγαδικων,a*b=', a*b)# migadikoi me meion
print('-------------------------------------------------------------------------')
def add(a,b):
    c=a+b
    return c
print('Εκτυπωνω c=a,b και προσθετω c=a+b=2+3=.....',add(2,3))
print('---------------------------------------------------------------------------')
a='python'
print ('Εκτυπωνω τη λιστα με κεφαλαια=',a.upper())
print('Εκτυπωνω τη λιστα=',a)
print('--------------------------------------------------------------------------')
b=['a','b','c','a','d']
print('Eκτυπωνω τη λιστα',b)
print('Μετραω τα a=', b.count('a'))
print('Φτιαχνω τη λιστα αναποδα=',b.reverse())
print('Εκτυπωνω τη λιστα αναποδα',b)
print('-------------------------------------------------------------------------------')

a=(1,2,3,4)
def add(a,b,c,d):
    return a+b+c+d

add(*a)
print ('Προσθετω πινακα με στοιχεια 1,2,3,4=', add(*a))
print('__________________________________________________')
#! python
# dates are easily constructed and formatted

from datetime import date
now = date.today()
print (now)
datetime=date(2003, 12, 2)

print (now.strftime( "%d-%m-%y ή %d%b %Y ειναι %d ημερα %A του %B"))

# dates support calendar arithmetic

birthday = date(1964, 7, 31)
age = now - birthday
print ('Ημερες απο γενηση=',age.days)
print('---------------------------------------------------------------------------------------')
# Measure some strings:
a = ['γατα', 'παραθυρο', 'Εκπαραθυρώσει']
for x in a:
    print( 'Mετραω τα γραμματα της καθε λεξης:', x,'=' , len(x))


