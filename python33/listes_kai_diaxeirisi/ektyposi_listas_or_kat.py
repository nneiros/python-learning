def main():
    print('Knuth 1.4.2, ex. 7')
    print('string: 2A0B345CDE67F1G1H0I5JK.')
    n = e = d = 0
    while 1:
        print("""
    1. Set Public Key
    2. Encode
    3. Decode
    0. Quit
    Your choice? """, end = "")
        choice = int(input())
        if not choice:
            return
        if choice == 1:
            n, e, d = set_keys()
        if choice == 2:
            if not n:
                n = int(input("Public Key: "))
                e = int(input("e: "))
            encode(n, e)
        if choice == 3:
            if not d:
                n, e, d = set_keys()
            decode(d, n)
 
def set_keys():
    """This fuction asks for 2 primes.
    It sets a public key and an encoding number, 'e'."""
    p = int(input("p: "))
    q = int(input("q: "))
    n = p * q
    m = (p - 1) * (q - 1)
    e = get_e(m)
    print("N = ", n, "\ne = ", e)
    d = get_d(e, m)
    while d < 0:
         d += m
    return [n, e, d]
 
def encode(n, e):
    
      """This function asks for a number and encodes it using 'n' and 'e'."""
      while 1:
        c = int(input("Number to encode: "))
        if not c :
             return
        print(pow(c, e, n))
def decode(d, n):
      """This function asks for a number and decodes it using 'd' and 'n'."""
      while 1:
         c = int(input("Number to decode: "))
         if not c:
             return
         else:
             print(pow(c, d, n))
      
def even(x):
     """True if x is even."""
     return x % 2 == 0
 
def get_e(m):
     """Finds an e coprime with m."""
     e = 2
     while gcd(e, m) != 1:
         e += 1
     return e
 
def gcd(a,b):
     """Euclid's Algorithm: Takes two integers and returns gcd."""
     while b > 0:
        a, b = b, a % b
     return a
 
def get_d(e, m):
    """Takes encoding number, 'e' and the value for 'm' (p-1) * (q-1).
    Returns a decoding number."""
    x = lasty = 0
    lastx = y = 1
    while m != 0:
        q = e // m
        e, m = m, e % m
        x, lastx = lastx - q*x, x
        y, lasty = lasty - q*y, y
    return lastx
 
if __name__ == "__main__":
    main()



class o_k_print:
    def __init__(self,items):
        self.items=items
    def o_print(self):
          print('Oλη η λιστα',self.items)
          print('Moνο οι δυο πρωτες θεσεις,οριζοντια.',self.items[:2])         
    def k_printall(self):
          for i in range(5):
              print(self.items[i])
    def k_print(self):
          for i in range(2):
              print(self.items[i])
s=o_k_print([1,2,3,4,5])
s.o_print()
print('Ολη η λιστα κατακορυφα.')
s.k_printall()
print('Μονο οι δυο θεσεις,κατακορυφα.')
s.k_print()
print('------------------------------------------------')
class Person:

    '''\nΝα παμε βημα βημα μεσα στην κλαση '''

    def __init__(self, name):
        '''Kατασκευη κλασης'''
        self.n_name = name        

    def show(self, n1, n2):
        '''Μεσα στην εμφανιση της κλασης\n'''
        
        print('Εχουμε ενα ονομα:', self.n_name)
        n1=int(input('Δωσε πρωτο αριθμο.'))
        n2=int(input('Δωσε δευτερο αριθμο.'))
        print ('Εχουμε την προσθεση δυο αριθμων.',(n1,n2), '=',  (n1 + n2), '\n')

    def __del__(self):
       
        print( self.n_name)

a=input('Δωσε το ονομα σου.')
p=Person (a)
print( p.__doc__)
print (p.__init__.__doc__)
print (p.show.__doc__)
p.show(2, 3)
print('Διαγραφη κατασκευης αντικειμενου.')
print(p.__del__.__doc__)
print('------------------------------------------------')
class list():
    def __init__(self,items):
        self.items=items
    def kat_print(self):
        return ( self.items)
    def ori_print(self):
         print('Η λιστα σε κατακορυφη εκτυπωση:')
         for i in range(5):#απο εδω του λες ποσες θεσεις θελεις για εκτυπωση
             print (self.items[i])
    def sum_arithmon(self):
         return sum(self.items)
lista3=list([1,2,3,4,5,6,7,8,9])
print('Λιστα3=%s' %lista3.kat_print())
print ('Προσθεση αριθμων λιστας =%s' %lista3.sum_arithmon())
print('-----------------------------------------------------------------------')
lista1=list([1,2,3,4,5])    
lista2=list(['A','B','C','D','E'])
print('Η λιστα1 σε οριζοντια εκτυπωση: %s' %lista1.kat_print())
print('Η λιστα2 σε οριζοντια εκτυπωση: %s' %lista2.kat_print())
print('-----------------------------------------------------------------------------------------------')
print('Η θεση 3 στη λιστα1 ειναι το:',lista1.items[3])#ektypose thn thesi (3)
print('-----------------------------------------------------------------------')
lista1.ori_print()
print('----------------------------------------------------------------------------------------------')
print ('Η θεση 2,3,4 στη λιστα2 ειναι=',lista2.items[1:4])
print ('Εκτυπωση μεχρι τη θεση 2 στη λιστα2=',lista2.items[:2])
print ('Εκτυπωση απο 2 θεση και πανω στη λιστα2=',lista2.items[2:])
print ('Η θεση 4 στη λιστα2=',lista2.items[4])
print('-----------------------------------------------------------------------------------------------')
lista4=list(['a',2,3,4,5,0])
lista4.ori_print()
print('----------------------------------------------------------------------------------------------')

