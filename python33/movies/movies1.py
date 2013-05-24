import operator  # for attrgetter()
import pickle    # to load and dump movie list
#anoigoume san 'w' kai meta san 'r' giati svinei ta palia dedomena
#trexei mono se python 2.7
 
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
    print "-"*70
    print "%-25s  %-20s  %8s  %8s" % ("Title", "Director", "Year", "ID")
    for movie in movie_list:
         print "%-25s  %-20s  %8s  %8s" % (movie.title, movie.director,
                                                              movie.year, movie.id)
    print "-"*70
    print

def sort_title(movie_list):
     #print "Sort the movie_list by title ..."
     movie_list.sort(key=operator.attrgetter('title'))

def search_title(file_list):
    found = False
    kw = raw_input("Enter keyword in movie's title: ").lower()
    print "-"*70
    for movie in movie_list:
        if kw in movie.title.lower():
            print "%-25s  %-20s  %8s  %8s" % (movie.title, movie.director,
                                              movie.year, movie.id)
            found = True
    print "-"*70
    if not found:
        print "Keyword '%s' not found!" % kw

def search_director(file_list):
    found = False
    kw = raw_input("Enter name of movie's director: ").lower()
    print "-"*70
    for movie in movie_list:
        if kw in movie.director.lower():
            print "%-25s  %-20s  %8s  %8s" % (movie.title, movie.director,
                                              movie.year, movie.id)
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
            print "%-25s  %-20s  %8s  %8s" % (movie.title, movie.director,
                                              movie.year, movie.id)
            found = True
    print "-"*70
    if not found:
        print "Year = %s not found!" % year

def search_id(file_list):#file_list
    """search via the unique movie id"""
    found = False
    id = raw_input("Enter id number of movie: ")
    print "-"*70
    for movie in movie_list:
        if movie.id == id:
            print "%-25s  %-20s  %8s  %8s" % (movie.title, movie.director,
                                              movie.year, movie.id)
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
        print "t -- title"
        print "d -- director"
        print "y -- year"
        print
        option = raw_input("Enter edit option: ").lower()
        if option == 't':
            print "Present title:", movie.title
            movie.title = raw_input("Enter new title: ")
        if option == 'd':
            print "Present director:", movie.director
            movie.director = raw_input("Enter new director: ")
        if option == 'y':
            print "Present year:", movie.year
            movie.year = raw_input("Enter new year: ")

def delete_movie(movie_list):
    found = False
    id = raw_input("Enter id number of movie: ")
    for index, movie in enumerate(movie_list):
        if movie.id == id:
            print "-"*70
            print "%-25s  %-20s  %8s  %8s" % (movie.title, movie.director,
                                              movie.year, movie.id)
            print "-"*70
            found = True
            delete = raw_input("Do you want to delete this movie (y/n)? ").lower()
            if delete in 'yes':
                del movie_list[index]
    if not found:
        print "ID = %s not found!" % id

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
    fin = open(movie_file, "r")
    movie_list = pickle.load(fin)
    fin.close()
    print "Movie database file %s has been loaded!" % movie_file
    # create a list of the unique movie ids
    id_list = make_id_list(movie_list)
    print id_list  # for testing only!!!

except IOError:
    print "Cannot find movie database file %s" % movie_file
    movie_list = []
    #movie_list = preload(movie_list)  # for testing only!!!
while True:
    #display menu
    print
    print "     Movie Database"
    print "---------------------------------"
    print "1 -- Add a movie"
    print "2 -- List all movies"
    print "3 -- Search (edit) specific movie"
    print "4 -- Delete a movie"
    print "0 -- Save data and Exit"
    print "---------------------------------"
    print len(movie_list),"movies in database"
    print
    option = raw_input("Enter option: ")
      # add one item
    if option == '1':
        title = raw_input("Enter the movie's title: ")
        director = raw_input("Enter the movie's director: ")
        year = raw_input("Enter year movie was produced: ")
        id = raw_input("Enter a unique identification number: ")
 #       while True:
              #this could be a stock or order number
#              id = raw_input("Enter a unique identification number: ")
#             if id in id_list:
#                 print ("This id already exists, try again!")
#              else:
#                    id_list.append(id)
#                    break
        movie_list.append(Movie(title, director, year, id))
        
    # show all items
    if option == '2':
        if len(movie_list) == 0:
             print ("No movies in database yet!")
        else:
             #sort  the movie_list ("by title ...")
             sort_title(movie_list)
             #now show a table of the movie_list
             print
             print ("The movie_list sorted by title ...")
             table_all(movie_list)
    
      #find one item
    if option == '3':
        if len(movie_list) == 0:
            print ("No movies in database yet!")
        else:
            print ("Search by:")
            print ("t -- title")
            print ("d -- director")
            print ("y -- year")
            print ("i == ID (allows editing items)")
            print
            option = raw_input("Enter option: ").lower()
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
        fout = open(movie_file, "w")
        pickle.dump(movie_list, fout)
        fout.close()
        print ("Movie database saved to file %s") % movie_file
        raise SystemExit
  
   
