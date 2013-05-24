x=1
while x <= 3:
    password=input('Δωσε κωδικο:')
    if password.endswith('1234'):
        print ('Καλως ορισες')
        break  
    else:
        print ('Ο κωδικος ειναι λαθος')
        x=x+1
else: 
    print ('Εκανες λαθος τρεις φορες αντε γεια.')
