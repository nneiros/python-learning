# example of a small movie database using a list of class instances
# load, save, add, list, search, edit and delete
# similar to the previous movie database
# but I added edit and check movie ids for uniqueness
# tested with Python25      
#ανοιγουμε την βαση σαν 'w' kai meta san 'r' giati svinei ta palia dedomena
import operator   #for attrgetter()
import pickle      #to load and dump movie list

class Movie(object):
     """a structure class for movies, self refers to the instance"""
     def __init__(self, title, director, year, id):
        self.title = title
        self.director = director
        self.year = year
        self.id = id
def make_id_list(movie_list):
    """create the id_list to check if ids are unique"""
    id_list = []
    for movie in movie_list:
        id_list.append(movie.id)
    return id_list
def table_all(movie_list):
    """print a table of all movie attributes"""
    print ("-"*200)
    #print "%s %-25s %-2s | %-20s  %8s   %12s" % ("test", "Ταινια","", "Σκηνοθετης", "Ετος", "Αριθμος")
    #print "%-20s %s %s %s" % ("Ταινια", "Σκηνοθετης", "Ετος", "Αριθμος")
    #print "{1}\t{0}".format("test1", "testtesttttttttt2")
    print (("|\t{:30}\t|\t{:30}\t|\t{:20}\t|\t{:20}\t|").format("Ταινια", "Σκηνοθετης", "Ετος", "Αριθμος"))  
    print ("-"*200)
    for movie in movie_list:
        #print "%-25s  %-20s  %8s  %8s" % (movie.title, movie.director, movie.year, movie.id)
         print (("|\t{:30}\t|\t{:30}\t|\t{:20}\t|\t{:20}\t|").format(movie.title, movie.director, movie.year, movie.id))
    print ("-"*200)
    print
def sort_title(movie_list):
    #print "Sort the movie_list by title ..."
    movie_list.sort(key=operator.attrgetter('title'))
def search_title(file_list):
    found = False
    kw = input("Δωσε λεξη κλειδι τιτλου ταινιας: ").lower()
    print ("-"*70)
    for movie in movie_list:
        if kw in movie.title.lower():
            print (("%-25s  %-20s  %8s  %8s") % (movie.title, movie.director,
                                              movie.year, movie.id))
            found = True
    print ("-"*70)
    if not found:
        print (("Λεξη κλειδι '%s' δεν βρεθηκε!") % kw)
def search_director(file_list):
    found = False
    kw = input("Δωσε το ονομα του παραγωγου της ταινιας: ").lower()
    print ("-"*70)
    for movie in movie_list:
        if kw in movie.director.lower():
            print (("%-25s  %-20s  %8s  %8s") % (movie.title, movie.director,
                                              movie.year, movie.id))
            found = True
    print ("-"*70)
    if not found:
        print (("Λεξη κλειδι δεν βρεθηκε '%s' not found!") % kw)
        
def search_year(file_list):
    found = False
    year = input("Δωσε το ετος παραγωγης της ταινιας: ")
    print ("-"*70)    
    for movie in movie_list:
        if movie.year == year:
            print (("%-25s  %-20s  %8s  %8s") % (movie.title, movie.director,
                                              movie.year, movie.id))
            found = True
    print ("-"*70)
    if not found:
        print (("Ετος = %s δεν βρεθηκε!") % year)
        
def search_id(file_list):
    """search via the unique movie id"""
    found = False
    id = input("Δωσε id number της ταινιας: ")
    print ("-"*70)
    for movie in movie_list:
        if movie.id == id:
            print (("%-25s  %-20s  %8s  %8s") % (movie.title, movie.director,
                                              movie.year, movie.id))
            movie_found = movie
            found = True
    print ("-"*70)
    if not found:
        print (("ID = %s δεν βρεθηκε!") % id)
    # since the id is unique, you are given an edit option
    if found:
        edit_item(file_list, movie_found)
def edit_item(file_list, movie):
    """edit a title, director, or year -- selected via unique movie id search"""
    yn = input("Επιτρεπεις τη διορθωση αντικειμενων (y or n)? ").lower()
    if yn == 'y':
        print ("Δωσε επιλογη:")
        print ("t -- τιτλος")
        print ("d -- παραγωγος")
        print ("y -- ετος")
        print
        option = input("Δωσε επιλογη διορθωσης: ").lower()
        if option == 't':
            print ("Σημερινος τιτλος:", movie.title)
            movie.title = input("Δωσε νεο τιτλο: ")
        if option == 'd':
            print ("Σημερινος παραγωγος:", movie.director)
            movie.director = input("Δωσε νεο παραγωγο: ")
        if option == 'y':
            print ("Σημερινο ετος:", movie.year)
            movie.year = input("Δωσε νεο ετος: ")
def delete_movie(movie_list):
    found = False
    id = input("Δωσε τον κωδικο της ταινιας: ")
    for index, movie in enumerate(movie_list):
        if movie.id == id:
            print ("-"*70)
            print (("%-25s  %-20s  %8s  %8s") % (movie.title, movie.director,
                                              movie.year, movie.id))
            print ("-"*70)
            found = True
            delete = input("Θελεις να διαγραψω την ταινια (y/n)? ").lower()
            if delete in 'yes':
                del movie_list[index]
    if not found:
        print ("ID = %s δεν βρεθηκε!" % id)
def preload(movie_list):
     # some fictitious movies for testing only!!!
     #call movie_list = preload(movie_list) right after line movie_list = [] in 'except IOError'
     #order is movie_list.append(Movie("title", "director", "year", "id"))
     movie_list.append(Movie("Murder in the Dark", "Frank Carpo", '1978', '1234'))
     movie_list.append(Movie("Kim does Dallas", "Hank Strong", '1993', '1235'))
     movie_list.append(Movie("Kaboom II", "Jaron Morgan", '1977', '1236'))
     movie_list.append(Movie("Soldiers of Fortune", "Loren Dickoff", '1967', '1237'))
     return movie_list
# this will be your movie database file each time
# you start your program (auto-loads) or exit it (auto-saves)
movie_file = "Movies1.dat"

try:
    # try to autoload existing movie database file
    fin = open(movie_file, "rb")
    movie_list = []
    print ('Γεια σου')
    movie_list = pickle.load(fin)
    #pickle.dump(movie_list,fin)
    print ('Εδω ειμαστε')
    fin.close()
    print (("H ταινιοθηκη......%s.......εχει φορτωθει!") % movie_file)
    # create a list of the unique movie ids
    id_list = make_id_list(movie_list)
    print (id_list)  # for testing only!!!
except IOError:
    print (("Δεν μπορω να βρω τη βαση δεδομενων %s") % movie_file)
    movie_list = []
    movie_list = preload(movie_list)  # for testing only!!!
while True:
    #display menu
    print ('---------------------------------------------------------------------------------')
    print ("                           Ταινιοθηκη                                     ")
    print ("-------------------------------------------------------------------------------")
    print ("              1 .         Προσθεσε ταινια                             ")
    print ("              2 .         Λιστα ταινιων                                  ")
    print ("              3 .         Βρες ή διορθωσε στοιχεια ταινιας     ")
    print ("              4 .         Διεγραψε ταινια                              ")
    print ("              0 .         Σωσε ταινια-Εξοδος                        ")
    print ("-------------------------------------------------------------------------------")
    print (len(movie_list),"ταινιες στη βαση δεδομενων")
    print
    option = input("Δωσε επιλογη: ")
    
    # add one item
    if option == '1':
        title = input("Δωσε τον τιτλο της ταινιας: ")
        director = input("Δωσε τον σκηνοθετη της ταινιας: ")
        year = input("Δωσε το ετος παραγωγης: ")
        id = input("Δωσε τον κωδικο της ταινιας: ")
        id_list.append(id)
        while True:
              # this could be a stock or order number
              id = input("Δωσε διαφορετικο κωδικο: ")      
              if id in id_list:
                  print ("Αυτο το id υπαρχει, δοκιμασε παλι!")
              else:
                   id_list.append(id)
                   break
        movie_list.append(Movie(title, director, year, id))
        
    # show all items
    if option == '2':
        if len(movie_list) == 0:
            print ("Δεν υπαρχουν ταινιες στη βαση δεδομενων ακομη!")
        else:
            # sort the movie_list by title ..."
            sort_title(movie_list)
            # now show a table of the movie_list
            print
            print ("Η ταινιοθηκη ταξινομηθηκε με τιτλο ...")
            table_all(movie_list)
    
    # find one item
    if option == '3':
        if len(movie_list) == 0:
            print ("Δεν υπαρχουν ταινιες στη βαση δεδομενων ακομη!")
        else:
            print ("Θα ψαξω με:")
            print ("t -- τιτλο")
            print ("d -- σκηθετη")
            print ("y -- ετος")
            print ("i == ID (Επιτρεπει την διορθωση στοιχειων)")
            print
            option = input("Δωσε την επιλογη σου: ").lower()
            if option == 't':
                search_title(movie_list)
            elif option == 'd':
                search_director(movie_list)
            elif option == 'y':
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
        print (("Η ταινια σωθηκε στο αρχειο %s") % movie_file)
        break
        #raise SystemExit
