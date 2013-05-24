#times = 0
#while True:
#      try:
#           x = int(input('Παρακαλω δωσε εναν αριθμο: '))
#           break
#      except ValueError:
#             print ('Δεν ειναι αριθμος.Προσπαθησε παλι....')
#      finally :
#            times += 1
#print ('Οι προσπαθειες σου ειναι...' ,  times)

print('****************************************************************')

import pickle

write_data = [1 , 2.0 , ' asdf ' , [None, True , False ] ]
with open( 'data.txt ' , 'wb' ) as f :
      pickle .dump( write_data , f )

with open( 'data.txt ' , 'rb' ) as f :
      read_data = pickle . load ( f )

print ( read_data )

print('***************************************************************')
g = open ('new_file' , 'w')
g.write('a new file begins')
g.write('....today!\n')
g.close()
g=open ('new_file' , 'r')
print (g)
print('...................................')
f= open('file.txt' , 'a')
f.write ('append a new line at the end the file \n')
f.close()
print (f)

f= open ('input_file.txt')
for line in f:
    print(line)
