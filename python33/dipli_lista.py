#def generator():
nums = ['09', '98', '87', '76', '65', '54', '43']
s_chars = ['*', '&', '^', '%', '$', '#', '@',]

data = open("list.txt", "w")
for c in s_chars:
   for n in nums:
       data.write(c + n)
       data.write("\n")
data.close()

#def generator():
 #    nums = ['09', '98', '87', '76', '65', '54', '43']
  #   s_chars = ['*', '&', '^', '%', '$', '#', '@',]

   #  data = open("list.txt", "w")
    # for c in s_chars:
     #   for n in nums:
      #     data.write(c + n + "\n")
     #data.close()     
