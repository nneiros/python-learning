import math
xa=raw_input('Δωσε μου το Xa:')  #eisagoume to Xa
xa=float(xa)                     #metatrepoume to int se float 
ya=raw_input('Δωσε μου το Ya:')  #eisagoume to Ya
ya=float(ya)    
sab=raw_input('Δωσε μου την αποσταση AB:') #eisagoume to Sab
sab=float(sab)
aab=raw_input('Δωσε μου την γωνια διευθυνσης ab -σε grad-:') #eisagoume to aAB se grad
aab=float(aab)
aabr=math.pi*aab/200   #metatropi tou aAB apo grad se rad
xb= xa+sab*math.sin(aabr) #ypologismos Xb
yb= ya+sab*math.cos(aabr) #ypologismos Xb
print 'To σημειο B εχει συντεταγμενες Xb:', xb, ', Yb:' , yb   #epistrofi stin o8oni twn timwn Xb, Yb
