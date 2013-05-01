# -*- coding: cp1253 -*-
import random
thenumber = random.randint(1,50)
print "ΕΧΩ ΣΚΕΦΤΕΙ ΕΝΑ ΑΡΙΘΜΟ ΑΠΟ ΤΟ 1 ΩΣ ΤΟ 50."
print "ΜΠΟΡΕΙΣ ΝΑ ΤΟΝ ΒΡΕΙΣ?"
guess = 0
while guess != thenumber:
  guess = input("ΔΩΣΕ ΤΟΝ ΑΡΙΘΜΟ: ")
  if guess > thenumber:
    print "ΕΔΩΣΕΣ ΜΕΓΑΛΥΤΕΡΟ ΑΡΙΘΜΟ!"
  if guess < thenumber:
    print "ΕΔΩΣΕΣ ΜΙΚΡΟΤΕΡΟ ΑΡΙΘΜΟ!"
  if guess == thenumber:
    print "ΜΠΡΑΒΟ ΤΟΝ ΒΡΗΚΕΣ!!!"
