import math
xa=raw_input('���� ��� �� Xa:')  #eisagoume to Xa
xa=float(xa)                     #metatrepoume to int se float 
ya=raw_input('���� ��� �� Ya:')  #eisagoume to Ya
ya=float(ya)    
sab=raw_input('���� ��� ��� �������� AB:') #eisagoume to Sab
sab=float(sab)
aab=raw_input('���� ��� ��� ����� ���������� ab -�� grad-:') #eisagoume to aAB se grad
aab=float(aab)
aabr=math.pi*aab/200   #metatropi tou aAB apo grad se rad
xb= xa+sab*math.sin(aabr) #ypologismos Xb
yb= ya+sab*math.cos(aabr) #ypologismos Xb
print 'To ������ B ���� ������������� Xb:', xb, ', Yb:' , yb   #epistrofi stin othoni twn timwn Xb, Yb
