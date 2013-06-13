from random import randint
print ("The Coin Flip Νο 1 Game,ρωταει ποσες φορες.\n")
num = int(input("Ποσες φορες θα στριψω το νομισμα?: "))
flips = [randint(0,1) for r in range(num)]
results=[]   
for object in flips:
       if object == 0:
           results.append("Κορωνα")
       elif object == 1:
           results.append("Γραμματα")
x=results.count('Κορωνα')
y=results.count('Γραμματα')
print(results)
print()
print(x,'φορες Κορωνα.')
print(y,'φορες Γραμματα')
print('---------------------------------------------------------------------------------------------------')  
print()
import random
print ("The Coin Flip Νο 2 Game,για 50 φορες.\n")
# set the coin
headsCount = 0
tailsCount = 0
count = 0
# the loop
while count < 50:
    coin = random.randrange(2)
    if coin == 0:
        headsCount += 1
    else:
        tailsCount += 1
    count += 1
print (headsCount,"φορες βγηκε κορωνα.")
print (tailsCount,"φορες βγηκε γραμματα.")
input("\n\nΠατα enter για εξοδο.")
print('-------------------------------------------------------------------------------------------------------')
print()
import random
print ("The Coin Flip Νο 3 Game,για 100 φορες.\n")
heads = 0
tails = 0
count = 0
while count < 100:
    coin = random.randrange(2)
    if coin == 0:
        heads = heads + 1
    else:
        tails = tails + 1
    count += 1
print ("Κορωνα: ", heads,'φορες')
print ("Γραμματα: ", tails,'φορες')
input("\nΠατα enter για εξοδο.")
