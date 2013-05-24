def print_numbers(numbers):
    print("Αριθμοι τηλεφωνων:")
    for k, v in numbers.items():
        print("Ονομα:", k, "\tΑριθμος:", v)
    print()
 
def add_number(numbers, name, number):
    numbers[name] = number
 
def lookup_number(numbers, name):
    if name in numbers:
        return "Ο αριθμος ειναι " + numbers[name]
    else:
        return name + " δεν βρεθηκε"
 
def remove_number(numbers, name):
    if name in numbers:
        del numbers[name]
    else:
        print(name," δεν βρεθηκε")
 
def load_numbers(numbers, filename):
    in_file = open(filename, "rt")
    while True:
        in_line = in_file.readline()
        if not in_line:
            break
        in_line = in_line[:-1]
        name, number = in_line.split(",")
        numbers[name] = number
    in_file.close()
 
def save_numbers(numbers, filename):
    out_file = open(filename, "wt")
    for k, v in numbers.items():
        out_file.write(k + "," + v + "\n")
    out_file.close()
 
def print_menu():
    print('1. Εκτυπωσε τηλεφωνα..............................')
    print('2. Προσθεσε ενα τηλεφωνο.........................')
    print('3. Αφαιρεσε ενα τηλεφωνο..........................')
    print('4. Βρες ενα τηλεφωνο................................')
    print('5. Φορτωσε τηλεφωνα-Aρχειο=numbers.txt..')
    print('6. Σωσε τηλεφωνα-Aρχειο=numbers.txt.......')
    print('7.  Εξοδος................................................')
    print('...............................................................')
    print()
 
phone_list = {}
menu_choice = 0
print_menu()
while True:
    #print_menu()
    menu_choice = input("Δωσε την  επιλογη σου (1-7): ")
    if menu_choice == '1':
        print_numbers(phone_list)
    elif menu_choice == '2':
        print("Προσθεσε ονομα και τηλεφωνο")
        name = input("Ονομα: ")
        phone = input("Τηλεφωνο: ")
        add_number(phone_list, name, phone)
    elif menu_choice == '3':
        print("Αφαιρεσε ονομα και τηλεφωνο")
        name = input("Ονομα: ")
        remove_number(phone_list, name)
    elif menu_choice == '4':
        print("Bρες ενα τηλεφωνο")
        name = input("Ονομα: ")
        print(lookup_number(phone_list, name))
    elif menu_choice == '5':
        filename = input("Αρχειο που θα φορτωθει: ")
        load_numbers(phone_list, filename)
    elif menu_choice == '6':
        filename = input("Αρχειο που θα σωθει: ")
        save_numbers(phone_list, filename)
    elif menu_choice == '7':
        break
    else:
        print_menu()
        print("Λαθος επιλογη επανελαβε.....")
