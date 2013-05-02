class mammal(object):
    def _init_(self):
        self.legs=4
    def speak(self):
         print"mpla mpla!"
    def setName(self,name):
          self.name = name
    def getName(self):
        return self.name

class cat(mammal):
    def _init_(self):
        super(cat,self)._init_()
        self.color="black"
    def speak(self):
        print "meow!"
thecat = cat()
print thecat.color
print thecat.legs           
