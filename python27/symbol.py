# search a dictionary for key or value
# using named functions or a class
# tested with Python25   by Ene Uran    01/19/2008
def find_key(dic, val):
    """return the key of dictionary dic given the value"""
    return [k for k, v in symbol_dic.iteritems() if v == val][0]
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
    def get_key(self, value):
        """find the key(s) as a list given a value"""
        return [item[0] for item in self.items() if item[1] == value]
    def get_value(self, key):
        """find the value given a key"""
        return self[key]
# test it out
if __name__ == '__main__':
    
    # dictionary of chemical symbols
    symbol_dic = {
    'C': 'carbon',
    'H': 'hydrogen',
    'N': 'nitrogen',
    'Li': 'lithium',
    'Be': 'beryllium',
    'B': 'boron'
    }
    print find_key(symbol_dic, 'boron')  # B
    print find_value(symbol_dic, 'B')    # boron
    print find_value(symbol_dic, 'H')    # hydrogen
    
    name = 'lithium'
    symbol = 'Li'
    # use a dictionary
    look = Lookup(symbol_dic)
    print look.get_key(name)      # [Li']
    print look.get_value(symbol)  # lithium
    
    # use a list of pairs instead of a dictionary
    # will be converted to a dictionary by the class internally
    age_list = [['Fred', 23], ['Larry', 28], ['Ene', 23]]
    look2 = Lookup(age_list)
    print look2.get_key(23)        # ['Ene', 'Fred']
    print look2.get_value('Fred')  # 23
