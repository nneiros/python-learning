class mammal:
    def __init__(self):
        self.legs=4
    def speak(self):
        print "���� ����"
    def setName(self, name):
        self.name = name
    def getName(self):
         return self.name
        
class cat(mammal):
    def __init__(self):
        #super(cat,self).__init__()#neos tropos
        mammal.__init__(self)#palaios tropos
        self.color="�����,�����,����"
    def speak(self):
        print "�� ������ ��� ����� ����,����"

class dog(mammal):
      def __init__(self):
           mammal.__init__(self)
           self.color="����"
      def speak(self):
          print "�� ������� ��� ����� ���,���"

animal = mammal()

thecat = cat()

thedog = dog()

animal.speak()
thecat.speak()
thedog.speak()		
thedog.name="�����"
print ('�� ������� �� ����' ),thedog.name
print ('���� ����� '),thedog.color
print ('��� ���� '),thedog.legs,('�����')
thecat.name="����"
print ('�� ������ �� ���� '),thecat.name
print ('���� �����'),thecat.color
print ('��� ����'),thecat.legs,('�����')
