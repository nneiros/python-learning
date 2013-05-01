mylist = [ "κοτα", "παιχνιδι", "ρολοι", "γατα" ]
length = len(mylist)
for x in range(0, length):
            print("στη θεση %s ειναι %s" % (x, mylist[x]))

toy_price = 1000
if toy_price > 1000:
    print("αυτο το παιχνιδι ειναι πολυ ακριβο")
elif toy_price > 100:
    print("το παιχνιδι ειναι ακριβο")
else:
    print("αυτο το παιχνιδι θα παρω")
