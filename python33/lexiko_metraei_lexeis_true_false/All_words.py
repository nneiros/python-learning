fin = open('words.txt')
total_words = 0
for line in fin:
    word = line.strip()
   
    def check(word):
        global total_words
        x = 0
        old_letter = ord('a')
        total = 0
        for i in range (len(word)):
            letter = ord(word[x])
            if letter >= old_letter:
                x +=1
                old_letter = letter
                total +=1
            if total == len(word):
                #print word
                total_words+=1

    check(word)
print (total_words)
# there are 596 words in alphabetical order
