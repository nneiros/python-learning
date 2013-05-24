import random
headcount = tailcount = 0
userinput = ''
print ("Τωρα στριψε ένα νόμισμα ...")
while userinput.lower() != "q":
    flip = random.choice(['heads', 'tails'])
    if flip == 'heads':
        headcount += 1
        print ("κεφαλι! αριθμός των κεφαλιων ειναι τωρα %d" % headcount)
    else:
            tailcount += 1
print ("γραμματα! αριθμός των γραμματων ειναι τωρα %d" % tailcount)
print ("Πατα 'q' για εξοδο",
userinput = input("ή πατα ενα αλλο κουμπι για στριψιμο παλι:"))
print ("ο συνολικός αριθμός των κεφαλιων ειναι:", headcount)
print ("ο συνολικός αριθμός των γραμματων ειναι:", tailcount)
