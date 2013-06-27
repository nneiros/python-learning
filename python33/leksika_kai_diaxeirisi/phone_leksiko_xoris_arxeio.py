def print_menu():
    print('1. Εκτυπωσε τηλεφωνα...')
    print('2. Προσθεσε τηλεφωνα...')
    print('3. Αφαιρεσε τηλεφωνα...')
    print('4. Βρες τηλεφωνα..........')
    print('5. Εξοδος.....................')
    print()
 
numbers = {}#leksiko
menu_choice = 0
print_menu()
while True :
    menu_choice = int(input("Δωσε την επιλογη σου (1-5): "))
    if menu_choice == 1:
        print("Tηλεφωνα:")
        for x in numbers.keys():
            print("Ονομα: ", x, "\tΤηλεφωνα:", numbers[x])
        print()
    elif menu_choice == 2:
        print("Προσθεσε ονομα και τηλεφωνο")
        name = input("Ονομα: ")
        phone = input("Τηλεφωνο: ")
        numbers[name] = phone
    elif menu_choice == 3:
        print("Αφαιρεσε Ονομα και Τηλεφωνο")
        name = input("Ονομα: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "δεν βρεθηκε")
    elif menu_choice == 4:
        print("Βρες τηλεφωνο")
        name = input("Ονομα: ")
        if name in numbers:
            print("Tο τηλεφωνο ειναι:", numbers[name])
        else:
            print(name, "δεν βρεθηκε")
    elif menu_choice ==  5:
        break
        #print_menu()
    else:
        print('Eπανελαβε...')
        print_menu()
