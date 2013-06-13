a = open("sample.txt", "a") 
a.write("This is a sample line.\n") 
x=input('Δωσε μια προταση για εγγραφη:')
a.write(x)
a.close()

a = open("sample.txt", "r") 
line = a.readline() 
while line: 
    print(line) 
    line = a.readline() # Note that the content of line changes 
# here, resetting the loop 
a.close()


