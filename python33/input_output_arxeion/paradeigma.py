#exclude_class = [ 'not ' , ' negation ' ]
#with open( ' infile ' , 'r' ) as f1 , open( ' outfile ' , 'w' ) as f2 :
     # for each line in the input file
#     for line in f1 . readlines ( ) :
         # by defaul t write a line to the out file unless
         # it doesn ' t contain one of the excluded words
#         write_to_file = True
         # for each word in a line of the input file
#         for word in line . split () :
              # if this word doesn ' t belong to closed_class
#              if word.rstrip ( ) in exclude_class :
#                   write_to_file = False
#                   break
#         if write_to_file :
#             f2 . write ( line )
print ( ' value = {0:2d} ' . format (12) ) # value = 12   
print ( ' value = {0:2b} ' . format (12) )
print('----------------------------------------------------------------------')
a = complex(1 , 1)
b = complex(1 , 2)
print (a)
print (b)
print ( a+b)#migadikoi
print ( a*b)# migadikoi me meion
print('-------------------------------------------------------------------------')
def add(a,b):
    c=a+b
    return c
print(add(2,3))
print('---------------------------------------------------------------------------')
a='python'
print (a.upper())
print(a)
print('--------------------------------------------------------------------------')
b=['a','b','c','d',]
print(b.count('a'))
print(b)
print(b.reverse())
print(b)
print('-------------------------------------------------------------------------------')
z = { 'a ' :2 , 'c ' :3, 'd ' :5, 'b ' :1}
print (z)
def print_variables ( a , b, c , d ) :
     print ( 'a: {}'.format (a))
     print ( 'b: {}'.format (b))
     print ( 'c: {}'.format (c))
     print ( 'd: {}'.format (d))
print_variables (*z)
print (z)
print('_____________________________________________')
a=(1,2,3,4)
def add(a,b,c,d):
    return a+b+c+d

add(*a)
print (add(*a))
print('__________________________________________________')

d = dict ( [ ( ' milk ' , 3.67) ,
                ( ' butter ' , 1.95) ,
                ( ' bread ' , 1.67) ,
                ( ' cheese ' , 4.67) ] )
print (d)
f= {
'milk' : 3.67,
'butter' : 1.95
}
print (f)
print('--------------------------------------------------------')
def increaseValue(d, key, value):
    if key not in d:
        d[key] = 0
    d[key] += value

def increaseValue2(d, key, value):
    d[key] = d.get(key, 0) + value
d={}
increaseValue2(d, 'dimitris' , 5)
print (d)
