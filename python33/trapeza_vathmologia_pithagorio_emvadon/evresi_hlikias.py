def print_menu():
    print ()#kataskeyh menu
    print ('---------------------------------------------------------------------------')
    print ()
    print ('---------1.Dose tin hlikia sou------------------------------------')
    print ('---------2.Dose tin hlikia tou filou h ths filis sou----------')
    print ('---------3.Poios einai megaliteros?---------------------------')
    print ('---------4.Typose to etos pou genithika---------------------')
    print ('---------5.Poia einai h diafora hlikias mas -----------------')
    print ('---------6.Exit---------------------------------------------------------')
    print ()
    print ('-------Oi diathesimes epiloges einai :1,2,3,4,5,6-------')
    print()
while True:
    print_menu()
    print('Dose epilogi:')#eisagogi epilogis
    hlikia=input()

    if hlikia=='1':
        hlikia_sou=int(input('Dose tin hlikia sou:'))#eisagogi hlikias xrhsth
        print('H hlikia pou ethoses einai:',hlikia_sou)#typonei thn hlikia pou edoses

    elif hlikia == '2':
        hlikia_tou=int(input('Dose tin hlikia tou/tis filou/filis sou:'))#eisagogi hlikias filou sou
        print ('H hlikia pou ethoses einai:',hlikia_tou)#typonei thn hlikia tou filou

    elif hlikia == '3':
        esy=hlikia_sou#pairnei h metavliti (esy) thn hlikia mou 
        filos=hlikia_tou#pairnei h metavliti (filos)thn hlikia tou
        if hlikia_sou>hlikia_tou:#ean h hlikia sou megalyterh apo thn hlikia tou
            print('O megalyteros eisai esy.')
        if hlikia_sou<hlikia_tou:#ean h hlikia tou megalyterh apo thn hlikia sou
            print('O megalyteros einai o filos sou.')
        if hlikia_sou==hlikia_tou:#ean ish hlikia 
            print('Exete thn idia hlikia.')

    elif hlikia == '4':
        simerino_etos=int(input('Dose simerini xronologia:'))#eisago xronologia gia na exei xrisi kai allh xronia
        etos_geniseos=simerino_etos-hlikia_sou#afairo to shmerino etos apo thn hlikia mou
        print ('To etos pou genithikes einai:',etos_geniseos)#evresi etous genisis 
            
    elif  hlikia == '5':      
        diafora=hlikia_sou - hlikia_tou#diafora hlikias
        if  diafora<0:#ean einai megalyterh h hlikia tou filou
            diafora=hlikia_tou - hlikia_sou#kanei antistrofh ton hlikion gia na mhn exo arnitiko arithmo
        print('H diafora hlikias mas einai ', diafora ,' xronia')#diafora hlikias

    elif hlikia == '6':
         print ('Telos evresis hlikias..')#exodos
         break

    else:
          print('Wrong option.Try again.')# ean ginei lathos epilogh     
