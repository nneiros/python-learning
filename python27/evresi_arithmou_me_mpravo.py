import random
thenumber = random.randint(1,50)
name = raw_input("ДЫСЕ ТО ОМОЛА СОУ")
print "евы сйежтеи ема аяихло апо то 1 ыс то 50."
print "лпояеис ма том бяеис?"
guess = 0
tries = 0
while guess != thenumber:
  tries=tries + 1
  guess = input("дысе том аяихло: ")
  if guess > thenumber:
    print "едысес лецакутеяо аяихло!"
  if guess < thenumber:
    print "едысес лийяотеяо аяихло!"
  if guess == thenumber:
    print "СУЦВАЯГТГЯИА", name, "том бягйес се", tries, "ПЯОСПАХЕИЕР!"
