#***************Dimiourgia kai epeksergasia arxeiou*******************
def print_nik(nik):
    print('Κειμενο:')
    for j in arxeio_list:
        print('Λιστα:',j)
    print()    

def add_keimeno(nik,keimeno):#,number
    arxeio_list.append(keimeno)#number
   
def look_keimeno(nik,keimeno):
    if keimeno in nik:
        print(( 'To κειμενο ειναι:'),nik[keimeno])
    else:
        return keimeno,'..' + 'δεν βρεθηκε...'
    
def remove_keimeno(nik,keimeno):
     if keimeno in nik:
         del nik[keimeno]
     else:
         print(keimeno, 'δεν βρεθηκε...')

def load_nik(nik,filename):
     in_file = open(filename,'rt')
     while True:
         in_line = in_file.readline()
         if not in_line:
             break
         in_line = in_line[:-1]
         keimeno =in_line.split(',')#number
         print(keimeno)
     in_file.close()  

def save_nik(nik,filename):
              out_file=open(filename, 'a')
              for j in arxeio_list:
                  #out_file.write(j)
              #for k in nik.items():
                  out_file.write(j+',')
              out_file.close     
def print_menu():
    print('.........................................................')
    print('....1.Eκτυπωσε κειμενο........................')
    print('....2.Προσθεσε κειμενο.........................')
    print('....3.Διεγραψε απο το αρχειο................')     
    print('....4.Φορτωσε αρχειο ..nik.txt................')
    print('....5.Σωσε αρχειο........nik.txt................')
    print('....6.Βρες ενα κειμενο...........................')
    print('....7.Exit.............................................')
    print('.........................................................')

#text_file = open('nik.txt' , 'a')
y=0
arxeio_list= []
print_menu()
while True:
    #print_menu()
   #text_file.write('αυτη ειναι η πρωτη εγγραφη')
    y= input('Δωσε επιλογη (1-7):')
    if y== '1':
       print_nik(arxeio_list)

    elif y == '2':   
         print('Προσθεσε κειμενο:')
         keimeno=input('Κειμενο:')
         add_keimeno(arxeio_list,keimeno)#p
        
    elif y=='3':
         print('Αφαιρεσε κειμενο:')
         keimeno=input('Δωσε κειμενο:')
         remove_keimeno(arxeio_list,keimeno)
         #file.close()
    elif y=='4':
         filename = input('Αρχειο που θα φορτωθει:')
         load_nik(arxeio_list, filename)
    elif y=='5':
         filename = input('Aρχειο που θα σωθει:')
         save_nik(arxeio_list,filename)
    elif y=='6':
        print('Βρες ενα κειμενο')
        keimeno = input('Δωσε το κειμενο:')
        print(look_keimeno(arxeio_list,keimeno))
    elif y=='7':
         print ('Τελος μαθηματος αντε γεια....')
         break
    else:
         print_menu()
         print('Λαθος επιλογη επανελαβε...')
         
