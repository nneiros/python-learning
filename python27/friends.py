import pickle

ans = "y"
friends={}
file = open("friends.txt", "a")#ανοιγει και γραφει στο αρχειο
while ans == "y":
      name = raw_input("Δωσε ονομα : ")
      ergasia = raw_input("Δωσε εργασια: ")
      email = raw_input("Δωσε email : ")
      phone = raw_input("Δωσε τηλεφωνο : ")

      friends[name] = {"Name": name, "Ergasia": ergasia,"Email": email, "Phone": phone}

      ans = raw_input("Θελεις να προσθεσεις αλλη εγγραφη (y/n) ? :")
pickle.dump(friends, file)
file.close()

import pickle

friend = {}
with open('friends.txt') as f: #ανοιγει για να εκτυπωσει
    while 1:
        try:
            friend.update(pickle.load(f))
        except EOFError:
            break # no more data in the file

for person in friend.values():
    print '{Name}\t{Ergasia}\t{Email}\t{Phone}'.format(**person)
