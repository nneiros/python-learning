my_lista=[1 , 2 , 3 , 4 , 5]
print ('Η λιστα σε οριζοντια εκτυπωση:',my_lista)#ektypose thn lista orizontia
print('-----------------------------------------------------------------------------------------------')
print ('Η θεση 3 ειναι το:',my_lista[3])#ektypose thn thesi (3)
print('-----------------------------------------------------------------------------------------------')
print ('Η λιστα σε κατακορυφη εκτυπωση:')#ektypose thn lista katakorifa
for i in range(5):
    print(my_lista[i])
print('----------------------------------------------------------------------------------------------')
my_list=['A','B','C','D','E']
print ('Εκτυπωση ολης της λιστας',my_list[:])
print ('Εκτυπωση της θεσης 2,3,4=',my_list[1:4])
print ('Εκτυπωση μεχρι τη θεση 2=',my_list[:2])
print ('Εκτυπωση απο 2 θεση και πανω=',my_list[2:])
print ('Εκτυπωση της θεσης 5=',my_list[4])
print('----------------------------------------------------------------------------------------------')
sum=0
list=[1,2,3,4,5,6,7,8,9]
print('Λιστα=', list)
for counter in list:
    sum=sum+counter
print('Προσθετει τη λιστα=',sum)   