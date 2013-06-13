fin = open('words.txt')
#print (fin)
fin.readline()
line = fin.readline()
word = line.strip()
#print( word)
for line in fin:
    word = line.strip()
    #print (word)
#fin.close()
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            print( False)
    print( True)
def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True
def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True
def is_palindrome(word):
    i = 0
    j = len(word)-1

    while i<j:
        if word[i] != word[j]:
            print( False)
        i = i+1
        j = j-1

    print( True)
