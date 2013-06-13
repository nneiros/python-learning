fin = open('words.txt')
the_dict = {}
greatest_length = 0

for line in fin:
    tuple_test = ()
    word = line.strip()
    tuple_test = tuple(sorted(word))
    if tuple_test in the_dict:
        the_dict[tuple_test].append(word)
        if len(the_dict[tuple_test]) >= greatest_length:
               greatest_length = len(the_dict[tuple_test])
    else:
        the_dict[tuple_test] = [word]

bingo_dict = {}
most_bingos = 0
for anagram in the_dict:
    if len(anagram) == 8 and len(the_dict[anagram]) >= 2:
        bingo_dict[anagram] = (the_dict[anagram])
        if len(the_dict[anagram]) >= most_bingos:
            most_bingos = len(the_dict[anagram])

for bingos in bingo_dict:
    if (len(bingo_dict[bingos])) == most_bingos:
        print (bingos,bingo_dict[bingos])

# ('a', 'e', 'g', 'i', 'n', 'r', 's', 't') forms the most bingos
# ['angriest', 'astringe', 'ganister', 'gantries', 'granites', 'ingrates', 'rangiest']
