class mammal:
     def __init__(self):
         self.legs=4
     def speak(self):
          print("Τα θηλαστικα εχουν ομιλια...μπλα μπλα!")
     def setName(self,name):
           self.name = name
     def getName(self):
         return self.name

class cat(mammal):
     def __init__(self):
        #super(cat,self)._init_()
         mammal.__init__(self)
         self.color=("ασπρο")
     def speak(self):
         print ('Η γατα κανει μιαου!')
animal=mammal()
thecat = cat()
animal.speak()
thecat.speak()
print ('Eχει χρωμα',thecat.color)
print ('Kαι εχει',thecat.legs,'ποδια.')           
