mylist = [ "Kοτα", "Παιχνιδι", "Ρολοι", "Γατα" ]
print (mylist)
length = len(mylist)
for x in range(0, length):
            print("Στη θεση %s ειναι = %s" % (x, mylist[x]))
print ('----------------------------------------------------------------------------')
x=input ('Δωσε τιμη παιχνιδιου=')
#print (x)
toy_price= int(x)
print (toy_price,'?')
#toy_price = 1000
if toy_price > 1000:
    print("Aυτο το παιχνιδι ειναι πολυ ακριβο")
elif toy_price > 100:
    print("Tο παιχνιδι ειναι ακριβο")
else:
    print("Aυτο το παιχνιδι θα παρω")
