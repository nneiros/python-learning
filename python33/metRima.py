era = 5
for x in range(1, 6):
    print("μετραω %s" % x)
    if x == era:
       print("τελος μετρηματος")
       break
for z in range(0,5):
    print ("x = %s" % z)
    if z==4:
      print ("τελος")
      break
shopping_list = [ "αυγα", "γαλα", "τυρι" ]
print (shopping_list)
if "γαλα" in shopping_list:#βρες αν γαλα ειναι στη λιστα
    print("Ειναι μεσα στη λιστα")#εαν ναι "ειναι στη λιστα"
else:
    print("Δεν υπαρχει στη λιστα")#αλλοιως "δεν υπαρχει στη λιστα"

age=6
if age == 1:
     print("1 is not an important age")
elif age == 2:
      print("2 is not an important age")
elif age == 3:
      print("3 is not an important age")
elif age == 4:
     print("4 is not an important age")
elif age == 5:
     print("5 is not an important age")
elif age == 6:
     print("6 χρονων ειναι η ηλικια σου")

a = 12
if a < 5  or a > 10:
    print("%s is not an important age"%a )
else:
    print ("εισαι  6 χρονων" )

b = 8
if not b == 10:
    print("%s is not an important age" % b)

import random
import sys
num = random.randint(1, 100)
while True:
      print("δωσε ενα αριθμο μεταξυ 1 και 100")
      chk = sys.stdin.readline()
      i = int(chk)
      if i == num:
         print("βρηκες τον σωστο αριθμο")
         break
      elif i < num:
         print("δωσε μεγαλυτερο αριθμο")
      elif i > num:
          print("δωσε μικροτερο αριθμο")

import time
#print(time.asctime())
print(time.strftime("%d %b %Y"))#ημερομηνια-ημερα μηνας(ονομασια) ετος
print(time.strftime("%d %m %Y"))#ημερομηνια-ημερα μηνας(αριθμος) ετος
          
