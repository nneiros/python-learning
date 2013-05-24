import random
thenumber = random.randint(1,50)
name = input("Δωσε το ονομα σου:")
print ("Εχω σκεφτει ενα αριθμο απο το 1 εως το 50.")
print ("Μπορεις να τον βρεις?")
guess = 0
tries = 0
while guess != thenumber:
  tries=tries + 1
  guess = int(input("Δωσε τον αριθμο: "))
  if guess > thenumber:
    print ("Εδωσες μεγαλυτερο αριθμο!")
  if guess < thenumber:
    print ("Εδωσες μικροτερο αριθμο!")
  if guess == thenumber:
    print ("Συγχαρητηρια", name, "τον βρηκες σε", tries, "προσπαθειες!")
