# Caesar Cipher

MAX_KEY_SIZE = 26
print('Θελεις να κρυπτογραφησεις ή να αποκρυπτογραφησεις ενα μηνυμα? πατα εντερ.')
      
def getMode():
        
    while True:
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Δωσε "encrypt" ή "e" για κρυπτογραφηση,'
                   ' ή δωσε "decrypt" ή "d" για αποκρυπτογραφηση')

def getMessage():
    print('Δωσε το μηνυμα:')
    return input()

def getKey():
    key = 0
    while True:
        print('Δωσε το κλειδι του κρυπτογραφου και να το θυμασαι(1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = getMode()
message = getMessage()
key = getKey()

print('H μεταφραση του μηνυματος ειναι:')
print(getTranslatedMessage(mode, message, key))
