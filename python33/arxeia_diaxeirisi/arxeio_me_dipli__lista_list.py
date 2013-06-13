#def generator():
nums = ['09', '98', '87', '76', '65', '54', '43']
s_chars = ['*', '&', '^', '%', '$', '#', '@',]

data = open("list.txt", "w")
for c in s_chars:
   for n in nums:
       data.write(c + n)
       data.write(" ")
data.close()

data = open('list.txt','r')
line = data.readlines()
print('Λιστα πρωτη',nums)
print('Λιστα δευτερη',s_chars)
print('Προσθετει στην δευτερη λιστα την πρωτη,τοσες φορες οσα στοιχεια εχει η δευτερη λιστα.')
print()
while line: 
    print(line) 
    line = data.readline() 
data.close()
#def generator():
 #    nums = ['09', '98', '87', '76', '65', '54', '43']
  #   s_chars = ['*', '&', '^', '%', '$', '#', '@',]

   #  data = open("list.txt", "w")
    # for c in s_chars:
     #   for n in nums:
      #     data.write(c + n + "\n")
     #data.close()     
