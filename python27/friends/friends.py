import pickle
  
ans = "y"
friends={}
file = open("friends.txt", "a")#������� ��� ������ ��� ������
while ans == "y":
      name = raw_input("���� ����� : ")
      ergasia = raw_input("���� �������: ")
      email = raw_input("���� email : ")
      phone = raw_input("���� �������� : ")

      friends[name] = {"Name": name, "Ergasia": ergasia,"Email": email, "Phone": phone}

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
    print '{Name}\t{Ergasia}\t{Email}\t{Phone}'.format(**person)
