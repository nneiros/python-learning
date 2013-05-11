vathmoi=[]#kataskeyh listas(vathmologia)

print  #kataskeyh menu
print ('--------------------Vathmologia Theologikou-------------------')
print ()
print ('---------1.Dose vathmo mathimatos pou perases--------')
print ('---------2.Ektipose sinolo mathimaton pou perases----')
print ('---------3.Ektiposh mesou orou mathimaton--------------')
print ('---------4.Exit---------------------------------------------------------')
print ()
print ('--------Oi diathesimes epiloges einai :1,2,3,4------------')
print()

while True:
    print('Dose epilogi:')
    vathmologia=input()#eisagogi epilogis

    if vathmologia== '1':
        vathmos=int(input('Dose vathmo mathimatos:'))#eisagogi vathmologias
        vathmoi.append(vathmos)#prosthetei kainourgia vathmologia sth lista
        print ('O vathmos einai :', vathmos)#ektyposi vathmologias          

    elif vathmologia == '2':
        y=len(vathmoi)#epistrefei ton arithmo ton stoixeion ths listas sth metavliti (y).
        print('Ta mathimata pou perases einai:',y)#ektiposi tou arithmou ton stoixeion

    elif vathmologia == '3':
        x=sum(vathmoi)#prosthetei thn vathmologia
        print('O mesos oros ths vathmologias sou einai:',x/y)#diairei to athrisma ths vathmologias dia ton arithmo stoixeion(M.O.)
        
    elif vathmologia == '4':
        print('Telos vathmologias')#exodos
        break

    else:
        print('Wrong option. Try again.')#ean ginei lathos epilogh
        
