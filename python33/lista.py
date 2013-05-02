#Python Εύρεση τιμών από list,μέσα σε κείμενο
def check_k(lista,keimeno):
    i=0
    if i <len (lista):
        if  lista[i] in keimeno:
            return True
        else:
            return False
        i+=1
        if i<len(piato):
            if piato[i] in keimeno:
                #i+=1
                return True
            else:
                return False
            i+=1
            if i<len(lista):
                if lista[i] in keimeno:
                    #i+=1
                    return True
                else:
                    return False
                                        #return True

                                    
                                    #else:
                                        #return False
                                

                                #else:
                                    #return True
                                
                            #else:
                                #return False
                        #else:
                            #return True
                        
                    #else:
                        #return False

                #else:
                    #return True

kreas= ['Χοιρινο','Κοτοπουλο']
piato= ['Δευτερο','Αλλο']
garnitoura= ['Πατατες', 'Ρυζι','Αλλο']
file ='lista2.txt'#->Διεύθυνση αρχείου  (Σαν dir_sin,έχω ορίσει πιο πριν το φάκελο του αρχείου,και σαν arxeio,την ονομασία του)
f=open(file, "r", encoding="utf8")
keimeno=f.read()
#print (kreas,piato,garnitoura)
print(keimeno)
f.close()
a=keimeno.split("\n")
#print(a)
gar=check_k(garnitoura, a[-3])
pia=check_k(piato, a[-2])
kre=check_k(kreas, a[-1])
#print(garnitoura,a[-3])
#print (piato,a[-2])
#print (kreas,a[-1])
print("garnitoura = ", gar)
print("piato=",pia)
print("kreas=",kre)
if gar==True and pia==True and kre==True:
    #for i in range(b) :
       print("done!")
	
