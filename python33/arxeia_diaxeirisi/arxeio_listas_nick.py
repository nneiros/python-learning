#***************Dimiourgia kai epeksergasia arxeiou*******************
def print_nik(arxeio_list):
    print('Aυτη ειναι η λιστα:',arxeio_list)
    print()    

def add_keimeno(nik,item):
    nik.append(item)
    print()
    
def look_keimeno(nik,item):
    if item in arxeio_list:
        return 'Τo κειμενo εχει θεση:',arxeio_list.index(item)
    else:
        return item + 'δεν βρεθηκε'
        print()
        
def remove_keimeno(nik, item):
     print('Εχει διαγραφει το κειμενο στη θεση:',y)
     arxeio_list.pop(y)
     print()
    #if y in arxeio_list:
        #print('Εχει διαγραφει το κειμενο στη θεση:',y) 
        #arxeio_list.pop(y)
         #del nik[item]
    #else:
        #print( y, 'δεν βρεθηκε...')

def load_nik(nik,filename):
     in_file = open(filename,'rt')
     keimeno=in_file.read()
     arxeio_list=keimeno.split()
     in_file.close()
     print('Tα δεδομενα του αρχειου ειναι:',keimeno)
     return arxeio_list
     print()

def save_nik(nik,filename):
     out_file=open(filename, 'w')
     for k in nik:
         out_file.write(k + '\n')#me \n sozei se next grammi,me (,)sozei me keno koma.
     out_file.close()     
     print()
     
def print_menu():
    print('.........................................................')
    print('....1.Eκτυπωσε κειμενο........................')
    print('....2.Προσθεσε κειμενο.........................')
    print('....3.Βρες ενα κειμενο...........................')     
    print('....4.Διεγραψε απο το αρχειο................')
    print('....5.Φορτωσε αρχειο ..nik.txt................')
    print('....6.Σωσε αρχειο........nik.txt................')
    print('....7.Exit.............................................')
    print('..........................................................')

z=0
arxeio_list= []#lista
print_menu()
while True:
    z = input('Δωσε επιλογη (1-7):')
    if z == '1':
       print_nik(arxeio_list)

    elif z == '2':   
         print('Προσθεσε κειμενο:')
         item=input('Κειμενο:')
         add_keimeno(arxeio_list, item)

    elif z == '3':
        print('Βρες ενα κειμενο:')
        item = input('Δωσε το κειμενο:')
        print(look_keimeno(arxeio_list, item))  

    elif z == '4':
         print('Αφαιρεσε κειμενο:')
         y=int(input('Δωσε θεση κειμενου:'))
         remove_keimeno(arxeio_list, y)
         
    elif z == '5':
         filename = input('Αρχειο που θα φορτωθει:')
         arxeio_list=load_nik(arxeio_list, filename)

    elif z == '6':
         filename = input('Aρχειο που θα σωθει:')
         save_nik(arxeio_list,filename)

    

    elif z == '7':
         print ('Τελος μαθηματος αντε γεια....')
         break
    else:
         print_menu()
         print('Λαθος επιλογη επανελαβε...')
         
