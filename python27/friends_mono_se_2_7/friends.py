import pickle#leitourgei mono se  python 2.7
friend= 'friend.txt'  
ans = "y"
friends={}
file = open('friends.txt', "a")#������� ��� ������ ��� ������
while ans == "y":
      name = raw_input("dose onoma : ")
      ergasia = raw_input("dose ergasia: ")
      email = raw_input("���� email : ")
      phone = raw_input("���� thlefono : ")

      friends[name] = {("Name"): name, ("Ergasia"): ergasia,("Email"): email, ("Phone"): phone}

      ans = raw_input("������ �� ���������� ���� ������� (y/n) ? :")
pickle.dump(friends, file)
file.close()

import pickle

friend = {}
with open('friends.txt') as f: #������� ��� �� ���������
    while 1: 
        try:
            friend.update(pickle.load(f))
        except EOFError:
            break # no more data in the file

for person in friend.values():
    print (('{Name}\t{Ergasia}\t{Email}\t{Phone}').format(**person))
