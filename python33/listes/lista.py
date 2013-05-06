#Python Εύρεση τιμών από list,μέσα σε κείμενο
#lista
kreas= ['Χοιρινο','Κοτοπουλο']
piato= ['Δευτερο','Αλλο']
garnitoura= ['Πατατες', 'Ρυζι','Αλλο']

def check_k(lista,keimeno):
    i=0
    if i <len (lista):
        if  lista[i] in keimeno:
           i+=1
           if i<len(lista):
                if lista[i] in keimeno:
                    i+=1
                    if i<len(lista):
                        if lista[i] in keimeno:
                            return True
                        else:
                            return False
                    else:
                        return True
                else:                                             
                  return False       
        else:                                             
            return True                 
                                  
file ='lista2.txt'#->Διεύθυνση αρχείου  (Σαν dir_sin,έχω ορίσει πιο πριν το φάκελο του αρχείου,και σαν arxeio,την ονομασία του)
f=open(file, "r", encoding="utf8")
keimeno=f.read()
f.close()
a=keimeno.split("\n")
print(keimeno)
#print(kreas)
#print(piato)
#print(garnitoura)
gar=check_k(garnitoura, a[-1])
pia=check_k(piato, a[-2])
kre=check_k(kreas, a[-3])
#print (a[-5])#πρωτα κανεις εκτυπωση του a για να δεις την θεση του καθενος(piato κ,λ,π)
#print (a[-4])
#print (a[-3])
print("garnitoura = ", gar)
print("piato=",pia)
print("kreas=",kre)
if gar==True and pia==True and kre==True:
    #for i in range(b) :
       print("done!")
	
