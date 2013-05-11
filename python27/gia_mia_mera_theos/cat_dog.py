class mammal:
    def __init__(self):
        self.legs=4
    def speak(self):
        print "Τα θηλαστικα εχουν ομιλια μπλα μπλα."
    def setName(self, name):
        self.name = name
    def getName(self):
         return self.name
        
class cat(mammal):
    def __init__(self):
        #super(cat,self).__init__()#neos tropos
        mammal.__init__(self)#palaios tropos
        self.color="μαυρο,ασπρο,καφε"
    def speak(self):
        print "Το γατακι μας κανει μιαρ,μιαρ."

class dog(mammal):
      def __init__(self):
           mammal.__init__(self)
           self.color="καφε"
      def speak(self):
          print "Το σκυλακι μας κανει γαβ,γαβ."

animal = mammal()

thecat = cat()

thedog = dog()

animal.speak()
thecat.speak()
thedog.speak()		
thedog.name="Λαιδη"
print 'Το σκυλακι το λενε',thedog.name,',εχει χρωμα',thedog.color,'και εχει ',thedog.legs,'ποδια.'
#print ('εχει χρωμα '),thedog.color
#print ('και εχει '),thedog.legs,('ποδια')
thecat.name="Ψικι"
print 'Το γατακι το λενε ',thecat.name,',εχει χρωμα',thecat.color,'και εχει',thecat.legs,'ποδια.'


