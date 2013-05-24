# -*- coding: cp1253 -*-
import random
thenumber = random.randint(1,50)
print "Εχω σκεφτει ενα αριθμο απο το 1 εως το 50.'
print "Μπορεις να το βρεις?"
guess = 0
while guess != thenumber:
  guess = input("Δωσε τον αριθμο: ")
  if guess > thenumber:
    print "Εδωσες μεγαλυτερο αριθμο!"
  if guess < thenumber:
    print "Εδωσες μικροτερο αριθμο!"
  if guess == thenumber:
    print "Μραβο τον βρηκες!!!"
