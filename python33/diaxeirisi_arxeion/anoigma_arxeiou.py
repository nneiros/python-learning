a = open("sample.txt", "w") 
a.write("This is a sample line.\n") 
a.close()

a = open("sample.txt", "r") 
line = a.readline() 
while line: 
    print(line) 
    line = a.readline() # Note that the content of line changes 
# here, resetting the loop 
a.close()


