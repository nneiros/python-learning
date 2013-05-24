import operator
import pickle
#anoigoume thn bash me "w" kai meta to alazoume se "r" giati svinei ta prota dedomena
class Movie(object):
     """a structure class for movies, self refers to the instance"""
     def __init__(self, name, ergasia, email, phone):
        self.name = name
        self.ergasia = ergasia
        self.email = email
        self.phone = phone

def make_id_list(movie_list):
    """create the id_list to check if ids are unique"""
    id_list = []
    for movie in movie_list:
        id_list.append(movie.phone)
    return id_list
def table_all(movie_list):
    """print a table of all movie attributes"""
    print ("-"*200)
    #print "%-25s  %-20s  %8s  %8s" % ("Name", "Ergasia", "Email", "Phone")
    print (("|\t{:30}\t|\t{:30}\t|\t{:20}\t|\t{:20}\t|").format("Ονομα", "Εργασια", "Email", "Tηλεφωνο"))  
    print ("-"*200)
    for movie in movie_list:
         #print "%-25s  %-20s  %8s  %8s" % (movie.name, movie.ergasia,
                                           #movie.email, movie.phone)
         print ("|\t{:30}\t|\t{:30}\t|\t{:15}\t|\t{:15}\t|".format(movie.name, movie.ergasia, movie.email, movie.phone))
    print ("-"*200)                           
    print
    
def sort_title(movie_list):
     print ("Ταξινομηση τηλεφωνων με ονομα ...")
     movie_list.sort(key=operator.attrgetter('name'))

def search_title(file_list):
    found = False
    kw = input("Δωσε λεξη κλειδι ονοματος τηλεφωνου: ").lower()
    print ("-"*70)
    for movie in movie_list:
        if kw in movie.name.lower():
            print ("%-25s  %-20s  %8s  %8s" % (movie.name, movie.ergasia,
                                              movie.email, movie.phone))
            found = True
    print ("-"*70)
    if not found:
        print ("Λεξη κλειδι  '%s' δεν βρεθηκε!" % kw)

def search_director(file_list):
    found = False
    kw = input("Δωσε εργασια: ").lower()
    print ("-"*70)
    for movie in movie_list:
        if kw in movie.ergasia.lower():
            print ("%-25s  %-20s  %8s  %8s" % (movie.name, movie.ergasia,
                                              movie.email, movie.phone))
            found = True
    print ("-"*70)
    if not found:
        print ("Λεξη κλειδι '%s' δεν βρεθηκε!" % kw)
def search_year(file_list):
    found = False
    year = input("Δωσε το email: ")
    print ("-"*70)    
    for movie in movie_list:
        if movie.email == year:
            print (("%-25s  %-20s  %8s  %8s") % (movie.name, movie.ergasia,
                                              movie.email, movie.phone))
            found = True
    print ("-"*70)
    if not found:
        print (("email = %s δεν βρεθηκε!") % year)

def search_id(file_list):#file_list
    """search via the unique movie id"""
    found = False
    phone = input("Δωσε αριθμο τηλεφωνου: ")
    print ("-"*700)
    for movie in movie_list:
        if movie.phone == phone:
            print ("%-25s  %-20s  %8s  %8s" % (movie.name, movie.ergasia,
                                              movie.email, movie.phone))
            movie_found = movie
            found = True
    print ("-"*70)
    if not found:
        print ("Τηλεφωνο = %s δεν βρεθηκε!" % phone)
    # since the id is unique, you are given an edit option
    if found:
        edit_item(file_list, movie_found)  #file_list

def edit_item(file_list, movie):
    """edit a title, director, or year -- selected via unique movie id search"""
    yn = input("Επιτρεπεις τη διορθωση αντικειμενων (y or n)? ").lower()
    if yn == 'y':
        print ("Δωσε επιλογη διορθωσης:")
        print ("n -- ονομα")
        print ("r -- εργασια")
        print ("e -- email")
        print ("p -- τηλεφωνο")
        option = input("Δωσε επιλογη διορθωσης: ").lower()
        if option == 'n':
            print ("Σημερινο ονομα:", movie.name)
            movie.name = input("Δωσε νεο ονομα: ")
        if option == 'r':
            print ("Σημερινη εργασια:", movie.ergasia)
            movie.ergasia = input("Δωσε νεα εργασια: ")
        if option == 'e':
            print ("Σημερινο email:", movie.email)
            movie.email = input("Δωσε νεο email: ")
        if option == 'p':
            print ("Σημερινο τηλεφωνο:", movie.phone)
            movie.phone = input("Δωσε νεο τηλεφωνο: ")
        
def delete_movie(movie_list):
    found = False
    phone = input("Δωσε αριθμο τηλεφωνου: ")
    for index, movie in enumerate(movie_list):
        if movie.phone == phone:
            print ("-"*70)
            print ("%-25s  %-20s  %8s  %8s" % (movie.name, movie.ergasia,
                                              movie.email, movie.phone))
            print ("-"*70)
            found = True
            delete = input("Θελεις να διαγραψω το τηλεφωνο (y/n)? ").lower()
            if delete in 'yes':
                del movie_list[index]
    if not found:
        print ("Τηλεφωνο = %s δεν βρεθηκε!" % id)

movie_file = "friends1.txt"
try:
    # try to autoload existing movie database file
    fin = open(movie_file, "rb")
    movie_list=[]
    movie_list = pickle.load(fin)
    #pickle.dump(movie_list,fin)
    fin.close()
    print (("Τηλεφωνα απο βαση δεδομενων---%s---εχουν φορτωθει!") % (movie_file))
    # create a list of the unique movie ids
    id_list = make_id_list(movie_list)
    print (id_list)  # for testing only!!!

except IOError:
    print (("Δεν μπορω να βρω τη βαση δεδομενων %s") % (movie_file))
    movie_list = []
    #movie_list = preload(movie_list)  # for testing only!!!
         
while True:
    #display menu
    print ('--------------------------------------------------')
    print ('               Tηλεφωνα                     ')
    print ('--------------------------------------------------')
    print (' 1 -- Προσθεσε τηλεφωνα--------------')
    print (' 2 -- Λιστα με ολα τα τηλεφωνα-----')
    print (' 3 -- Βρες ή διορθωσε τηλεφωνα----')
    print (' 4 -- Διεγραψε τηλεφωνα---------------')
    print (' 0 -- Σωσε τηλεφωνα-Εξοδος---------')
    print ('--------------------------------------------------')
    print (len(movie_list),"τηλεφωνα στη βαση δεδομενων")
    print ()
    option = input("Δωσε επιλογη: ")
      # add one item
    if option == '1':
        name = input("Δωσε ονομα: ")
        ergasia = input("Δωσε εργασια: ")
        email = input("Δωσε email: ")
        phone = input("Δωσε τηλεφωνο: ")
        while True:
              #this could be a stock or order number
              id = input("Δωσε διαφορετικο νουμερο: ")
              if id in id_list:
                 print ("Αυτο το τηλεφωνο υπαρχει,δοκιμασε παλι!")
              else:
                    id_list.append(id)
                    break
        movie_list.append(Movie(name, ergasia, email, phone))
        
    # show all items
    if option == '2':
        if len(movie_list) == 0:
             print ("Δεν υπαρχουν τηλεφωνα στη βαση δεδομενων!")
        else:
             #sort  the movie_list ("by title ...")
             sort_title(movie_list)
             #now show a table of the movie_list
             print
             print ("Η λιστα τηλεφωνων ταξινομηθηκε με το ονομα ...")
             table_all(movie_list)
    
      #find one item
    if option == '3':
        if len(movie_list) == 0:
            print ("Δεν υπαρχουν τηλεφωνα στη βαση δεδομενων!")
        else:
            print ("Ψαξε με:")
            print ("n -- ονομα")
            print ("r -- εργασια")
            print ("e -- email")
            print ("p == τηλεφωνο(Επιτρεπει την διορθωση στοιχειων)")
            print
            option = input("Δωσε επιλογη: ").lower()
            if option == 'n':
                search_title(movie_list)
            elif option == 'r':
                search_director(movie_list)
            elif option == 'e':
                search_year(movie_list)
            else:
                search_id(movie_list)
                
    # delete one item by unique id number
    if option == '4':
        delete_movie(movie_list)
        
    # save data and exit
    if option == '0':
        # auto save the whole movie list
        fout = open(movie_file, "wb")
        pickle.dump(movie_list, fout)
        fout.close()
        print (("Τα τηλεφωνα σωθηκαν στο αρχειο %s") % movie_file)
        break
        #raise SystemExit
