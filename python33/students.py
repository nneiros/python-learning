max_points = [25, 25, 50, 25, 100]
assignments = ['hw ch 1', 'hw ch 2', 'quiz   ', 'hw ch 3', 'test']
students = {'#Max': max_points}
 
def print_menu():
    print("1. Προσθεσε σπουδαστη...")
    print("2. Αφαιρεσε σπουδαστη....")
    print("3. Εκτυπωσε βαθμους.......")
    print("4. Εγγραφη βαθμολογιας..")
    print("5. Εκτυπωσε μενου...........")
    print("6. Eξοδος........................")
 
def print_all_grades():
    print('\t', end=' ')
    for i in range(len(assignments)):
        print(assignments[i], '\t', end=' ')
    print()
    keys = list(students.keys())
    keys.sort()
    for x in keys:
        print(x, '\t', end=' ')
        grades = students[x]
        print_grades(grades)
 
def print_grades(grades):
    for i in range(len(grades)):
        print(grades[i], '\t', end=' ')
    print()
 
print_menu()
menu_choice = 0
while menu_choice != 6:
    print()
    menu_choice = int(input("Δωσε επιλογη μενου (1-6): "))
    if menu_choice == 1:
        name = input("Σπουδαστης για εγγραφη: ")
        students[name] = [0] * len(max_points)
    elif menu_choice == 2:
        name = input("Αφαιρεση σπουδαστη: ")
        if name in students:
            del students[name]
        else:
            print("Σπουδαστης:", name, "δεν βρεθηκε")
    elif menu_choice == 3:
        print_all_grades()
    elif menu_choice == 4:
        print("Eγγραφη βαθμολογιας")
        name = input("Σπουδαστης: ")
        if name in students:
            grades = students[name]
            print("Γραψε αριθμο στην εγγραφη βαθμολογιας..")
            print("Γραψε 0 (zero) για εξοδο.")
            for i in range(len(assignments)):
                print(i + 1, assignments[i], '\t', end=' ')
            print()
            print_grades(grades)
            which = 1234
            while which != -1:
                which = int(input("Εγγραφη βαθμου(1-5): "))
                which -= 1    #same as which = which - 1
                if 0 <= which < len(grades):
                    grade = int(input("Βαθμος: "))
                    grades[which] = grade
                elif which != -1:
                    print("Λαθος αριθμος βαθμολογιας")
        else:
            print("Σπουδαστης δεν βρεθηκε")
    elif menu_choice != 6:
        print_menu()
