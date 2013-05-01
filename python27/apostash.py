import math
xa=raw_input('Dose mou to Xa:')  #eisagoume to Xa
xa=float(xa)                     #metatrepoume to int se float 
ya=raw_input('Dose mou to Ya:')  #eisagoume to Ya
ya=float(ya)    
sab=raw_input('Dose mou tin apostasi AB:') #eisagoume to Sab
sab=float(sab)
aab=raw_input('Dose mou tin gonia diey8insis ab -se grad-:') #eisagoume to aAB se grad
aab=float(aab)
aabr=math.pi*aab/200   #metatropi tou aAB apo grad se rad
xb= xa+sab*math.sin(aabr) #ypologismos Xb
yb= ya+sab*math.cos(aabr) #ypologismos Xb
print 'To simeio B exei syntetagmenes Xb:', xb, ', Yb:' , yb   #epistrofi stin o8oni twn timwn Xb, Yb
