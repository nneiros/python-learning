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
    print "-"*200
    #print "%-25s  %-20s  %8s  %8s" % ("Name", "Ergasia", "Email", "Phone")
    print "|\t{:30}\t|\t{:30}\t|\t{:20}\t|\t{:20}\t|".format("Ονομα", "Εργασια", "Email", "Tηλεφωνο")  
    print "-"*200
    for movie in movie_list:
         #print "%-25s  %-20s  %8s  %8s" % (movie.name, movie.ergasia,
                                           #movie.email, movie.phone)
         print "|\t{:30}\t|\t{:30}\t|\t{:15}\t|\t{:15}\t|".format(movie.name, movie.ergasia, movie.email, movie.phone)
    print "-"*200                           
    print
    
def sort_title(movie_list):
     #print "Sort the movie_list by title ..."
     movie_list.sort(key=operator.attrgetter('name'))

def search_title(file_list):
    found = False
    kw = raw_input("Enter keyword in movie's title: ").lower()
    print "-"*70
    for movie in movie_list:
        if kw in movie.name.lower():
            print "%-25s  %-20s  %8s  %8s" % (movie.name, movie.ergasia,
                                              movie.email, movie.phone)
            found = True
    print "-"*70
    if not found:
        print "Keyword '%s' not found!" % kw

def search_director(file_list):
    found = False
    kw = raw_input("Enter name of movie's director: ").lower()
    print "-"*70
    for movie in movie_list:
        if kw in movie.ergasia.lower():
            print "%-25s  %-20s  %8s  %8s" % (movie.name, movie.ergasia,
                                              movie.email, movie.phone)
            found = True
    print "-"*70
    if not found:
        print "Keyword '%s' not found!" % kw
def search_year(file_list):
    found = False
    year = raw_input("Enter production year of movie: ")
    print "-"*70    
    for movie in movie_list:
        if movie.year == year:
            print "%-25s  %-20s  %8s  %8s" % (movie.name, movie.ergasia,
                                              movie.email, movie.phone)
            found = True
    print "-"*70
    if not found:
        print "Year = %s not found!" % year

def search_id(file_list):#file_list
    """search via the unique movie id"""
    found = False
    phone = raw_input("Enter phone of friend: ")
    print "-"*70
    for movie in movie_list:
        if movie.phone == phone:
            print "%-25s  %-20s  %8s  %8s" % (movie.name, movie.ergasia,
                                              movie.email, movie.phone)
            movie_found = movie
            found = True
    print "-"*70
    if not found:
        print "ID = %s not found!" % id
    # since the id is unique, you are given an edit option
    if found:
        edit_item(file_list, movie_found)  #file_list

def edit_item(file_list, movie):
    """edit a title, director, or year -- selected via unique movie id search"""
    yn = raw_input("Do want to edit an item (y or n)? ").lower()
    if yn == 'y':
        print "Edit choices:"
        print "n -- name"
        print "r -- ergasia"
        print "e -- email"
        print "p -- phone"
        option = raw_input("Enter edit option: ").lower()
        if option == 'n':
            print "Present name:", movie.name
            movie.name = raw_input("Enter new name: ")
        if option == 'r':
            print "Present ergasia:", movie.ergasia
            movie.ergasia = raw_input("Enter new ergasia: ")
        if option == 'e':
            print "Present email:", movie.email
            movie.email = raw_input("Enter new email: ")
        if option == 'p':
            print "Present email:", movie.phone
            movie.phone = raw_input("Δωσε νεο τηλεφωνο: ")
        
def delete_movie(movie_list):
    found = False
    phone = raw_input("Dose phone number of friend: ")
    for index, movie in enumerate(movie_list):
        if movie.phone == phone:
            print "-"*70
            print "%-25s  %-20s  %8s  %8s" % (movie.name, movie.ergasia,
                                              movie.email, movie.phone)
            print "-"*70
            found = True
            delete = raw_input("Do you want to delete this movie (y/n)? ").lower()
            if delete in 'yes':
                del movie_list[index]
    if not found:
        print "Phone = %s not found!" % id

movie_file = "friends1.txt"
try:
    # try to autoload existing movie database file
    fin = open(movie_file, "r")
    movie_list = pickle.load(fin)
    fin.close()
    print "Τηλεφωνα απο βαση δεδομενων %s εχουν φορτωθει!" % movie_file
    # create a list of the unique movie ids
    id_list = make_id_list(movie_list)
    print id_list  # for testing only!!!

except IOError:
    print "Cannot find friends database file %s" % movie_file
    movie_list = []
    #movie_list = preload(movie_list)  # for testing only!!!
         
while True:
    #display menu
    print
    print "     Tηλεφωνα      "
    print "---------------------------------"
    print "1 -- Προσθεσε τηλεφωνα"
    print "2 -- Λιστα με ολα τα τηλεφωνα"
    print "3 -- Διορθωσε τηλεφωνα"
    print "4 -- Διεγραψε τηλεφωνα"
    print "0 -- Σωσε τηλεφωνα-ΕΞΟΔΟΣ"
    print "---------------------------------"
    print len(movie_list),"τηλεφωνα στη βαση δεδομενων"
    print
    option = raw_input("Enter option: ")
      # add one item
    if option == '1':
        name = raw_input("Dose onoma: ")
        ergasia = raw_input("Dose ergasia: ")
        email = raw_input("Dose email: ")
        phone = raw_input("Dose thlefono: ")
#        while True:
              #this could be a stock or order number
#              id = raw_input("Enter a unique identification number: ")
#              if id in id_list:
#                 print ("This id already exists, try again!")
#              else:
#                    id_list.append(id)
#                    break
        movie_list.append(Movie(name, ergasia, email, phone))
        
    # show all items
    if option == '2':
        if len(movie_list) == 0:
             print ("No movies in database yet!")
        else:
             #sort  the movie_list ("by title ...")
             sort_title(movie_list)
             #now show a table of the movie_list
             print
             print ("The friends_list sorted by name ...")
             table_all(movie_list)
    
      #find one item
    if option == '3':
        if len(movie_list) == 0:
            print ("No movies in database yet!")
        else:
            print ("Search by:")
            print ("n -- name")
            print ("r -- ergasia")
            print ("e -- email")
            print ("p == phone")
            print
            option = raw_input("Enter option: ").lower()
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
        fout = open(movie_file, "w")
        pickle.dump(movie_list, fout)
        fout.close()
        print ("Movie database saved to file %s") % movie_file
        raise SystemExit
