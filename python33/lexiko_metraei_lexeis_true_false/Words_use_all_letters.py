fin = open('words.txt')
for line in fin:
    word = line.strip()
    def uses_all(word,letters):
        x = 0
        total = 0
        global total_words
        for i in range(len(letters)):
            letter = letters[x]
            x+=1
            if letter in word:
                total +=1
        if total == len(letters):
            return True
        else:
            return False
    
    
    print (uses_all(word,'aeiou'))#


# there are 598 words that use aeiou
# there are 42 words that use aeiouy
