upoloipo_logariasmou=10000


print("*********************************************************")
print("*********************************************************")
print("************Trapeza Logariasmou********************")
print(" ")
print("Oi diathesimes epiloges einai: A, K, E, X")
print(" ")

while True: 
    print("Dose epilogi:")
    entoli_tamia=input()

    if entoli_tamia=="A":
        poso=int(input("Dwse poso analipshs:"))
        upoloipo_logariasmou=upoloipo_logariasmou-poso
        print("To ipolipo tou logariasmou sas einai:",upoloipo_logariasmou)
    elif entoli_tamia=="K":
        poso=int(input("Dwse poso katatheshs:"))
        upoloipo_logariasmou=upoloipo_logariasmou+poso
        print("To ipolipo tou logariasmou sas einai:",upoloipo_logariasmou)
    elif entoli_tamia=="E":
        print("To ipolipo tou logariasmou sas einai:",upoloipo_logariasmou)
    elif entoli_tamia=="X":
        print("Telos sinallaghs")
        break
    else:
        print("Lathos epilogi")
    
