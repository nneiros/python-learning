class mammal:
     def __init__(self):
         self.legs=4
     def speak(self):
          print"mpla mpla!"
     def setName(self,name):
           self.name = name
     def getName(self):
         return self.name

class cat(mammal):
     def __init__(self):
        #super(cat,self)._init_()
         mammal.__init__(self)
         self.color="�����"
     def speak(self):
         print '� ���� ����� meow!'
animal=mammal()
thecat = cat()
animal.speak()
thecat.speak()
print ('� ���� ���� �����'),thecat.color
print ('� ���� ����'),thecat.legs,('�����')           
