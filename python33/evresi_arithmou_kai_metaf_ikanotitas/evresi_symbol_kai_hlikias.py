# search a dictionary for key or value
# using named functions or a class

def find_key(dic, val):
    """return the key of dictionary dic given the value"""
    return (k for k, v in dic.iteritems() if v == val)[0]
def find_value(dic, key):
    """return the value of dictionary dic given the key"""
    return dic[key]
class Lookup(dict):
    """
    a dictionary which can lookup value by key, or keys by value
    """
    def __init__(self, items=[]):
        """items can be a list of pair_lists or a dictionary"""
        dict.__init__(self, items)
    def get_keys(self, value):
        """find the key(s) as a list given a value"""
        return [item[0] for item in self.items() if item[1] == value]
    def get_key(self, value):
         """
         find the key associated to the given a value. If several keys exist,
         only the first is given. To get the whole list, use get_keys instead.
         """
         list = self.get_keys(value)
         if len(list) == 0:
             return None
         return list[0]
    def get_value(self, key):
        """find the value given a key"""
        return self[key]
# Use cases and unit tests
if __name__ == '__main__':    
    # dictionary of chemical symbols
   # symbol_dic={}
    symbol_dic = {
    'C': 'ανθρακας',
    'H': 'υδρογονο',
    'N': 'αζωτο',
    'Li': 'λιθιο',
    'Be': 'βιριλιο',
    'B': 'βοριο'
    }

print ('Λιστα=',symbol_dic)
x= input('Δωσε ενα χημικο στοιχειο απο το λεξικο:')
if x in symbol_dic:
    print ((x),('ειναι στο λεξικο.Εχει oνομασια'),\
           symbol_dic[x])
else:
    print ((x), ('δεν ειναι στο λεξικο'))
print()
keys = list(symbol_dic.keys())
values=list(symbol_dic.values())
print('To λεξικο εχει στοιχεια',list(keys))
print('Aυτα εχουν αντιστοιχα ονομασια',list(values))
print()
print('To λεξικo εχει στοιχεια=',(keys))
print('Tα βαζω αλφαβητικα=',sorted(keys))
print ('Τo λεξικο εχει ονομασιες=',(values))
print('Τo λεξικo περιεχει',len(symbol_dic),'στοιχεια.')
print()
look=Lookup(symbol_dic)
print ('Ευρεση συμβολου του στοιχειου βοριον=',look.get_keys('βοριο')) # B
print ('Ευρεση ονομασιας του συμβολου Β=',look.get_value( 'B'))  # boron
print ('Ευρεση ονομασιας του συμβολου Η=',look.get_value( 'H'))    # hydrogen

name =( 'λιθιο')
symbol =( 'Li')
    # use a dictionary
look = Lookup(symbol_dic)
print ('Κοιτα τον συμβολισμο του στοιχειου',(name),'=',look.get_keys(name))      # [Li']
print ('Κοιτα την ονομασια του στοιχειου',(symbol),'=',look.get_value(symbol))  # lithium
    
    # use a list of pairs instead of a dictionary
print('----------------------------------------------------------------------------')
age_list = [['Fred', 23], ['Larry', 28], ['Ene', 23]]
look2 = Lookup(age_list)
print ('Eκτυπωση λιστας=',age_list)
print ('Κοιτα ποιοι εχουν ηλικια 23=',look2.get_keys(23) )       # ['Ene', 'Fred']
print ('Κοιτα την ηλικια του Larry=',look2.get_value('Larry') ) # 23

