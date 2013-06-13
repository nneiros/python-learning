z = { 'a ' :2 , 'c ' :3, 'd ' :5, 'b ' :1}
print ('Εκτυπωνω λεξικο',z)
def print_variables ( a , b, c , d ) :
     print ( 'Εκτυπωνω a με τη 1η θεση στο λεξικο=a: {}'.format (a))
     print ( 'Εκτυπωνω b με τη 2η θεση στο λεξικο=b: {}'.format (b))
     print ( 'Εκτυπωνω c με τη 3η θεση στο λεξικο=c: {}'.format (c))
     print ( 'Εκτυπωνω d με τη 4η θεση στο λεξικο=d: {}'.format (d))
print_variables (*z)
#print (print_variables (*z))
print('_____________________________________________')
d = dict ( [ ( ' γαλα ' , 3.67) ,
                ( ' βουτυρο ' , 1.95) ,
                ( ' ψωμι ' , 1.67) ,
                ( ' τυρι ' , 4.67) ] )
print ('Εκτυπωνω λεξικο=',d)
f= {
'γαλα' : 3.67,
'βουτυρο' : 1.95
}
print ('Εκτυπωνω λεξικο=',f)
print('--------------------------------------------------------')
def increaseValue(d, key, value):
    if key not in d:
        d[key] = 0
    d[key] += value
d={}
increaseValue (d,'Bαγγελης' ,9)
increaseValue (d,'Βρασιδας',8)
print('Eκτυπωνω λεξικο=' ,d)

def increaseValue2(d, key, value):
    d[key] = d.get(key, 0) + value
d={}
increaseValue2(d, 'Δημητρης' , 5)
increaseValue2(d, 'Ριρικα' ,15)
print ('Εκτυπωνω λεξικο=',d)
print('--------------------------------------------------------------------------------------')
