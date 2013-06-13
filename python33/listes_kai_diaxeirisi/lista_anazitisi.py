''' bisect_search.py
If a list is long and sorted, then a binary search is faster
than a list index() search.
works with Python27 and Python32  HiHe
'''
import bisect
def linear_search(names, search):
    """
    a standard linear search
    """
    ix = names.index(search)
    sf = "Με διαδοχικη αναζητηση το ονομα {}, βρεθηκε στην διευθυνση {}"
    print(sf.format(search, ix))
    
def bisect_search(names, search):
    """
    search using bisect()
    no-match gives closest index (no index error)
    """
    ix = bisect.bisect(names, search) - 1
    sf = "Με διχοτομημενη αναζητηση το ονομα {}, βρεθηκε στη διευθυνση {}"
    # this will trap the no-match situation
    if names[ix] == search:
        print(sf.format(search, ix))
    else:
        print("Το ονομα {} δεν βρεθηκε!".format(search))
names = [
'Ανδρεας', 'Θοδωρης', 'Βαγγελης', 'Ευα', 'Βρασιδας', 'Θανασης', 'Γιαννης', 'Μαιρη', 'Δημητρα'
]
# bisect search needs a sorted list
names.sort()
print('Λιστα=',names)
print('-'*70)
search = ('Γιαννης')
linear_search(names, search)
print('-'*70)
bisect_search(names, search)
print('-'*70)
# search for a name not in the list
search = 'Λιζα'
bisect_search(names, search) 
print('-'*70)
# you can insert a name into the sorted name list at the proper spot
new_name = 'Μαρια'
print ('Νεο ονομα στη λιστα=',new_name)
print('-'*70)
bisect.insort_left(names, new_name)
print('Νεα λιστα=',names)   # testing
''' output >>>
['ανδρεας', '', 'Eva', 'Gin', 'Ivy', 'γιαννης', 'Moe', 'Pam', 'Zoe']
----------------------------------------------------------------------
Linear search for γιαννης, found it at index 3
----------------------------------------------------------------------
Bisect search for γιαννης, found it at index 3
----------------------------------------------------------------------
λιζα δεν βρεθηκε!
----------------------------------------------------------------------
['Amy', 'Dee', 'Eva', 'Gin', 'Ivy', 'Kay', 'Mae', 'Moe', 'Pam', 'Zoe']
'''
