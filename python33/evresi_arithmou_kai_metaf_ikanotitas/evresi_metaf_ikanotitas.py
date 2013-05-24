class car:
    def __init__(self,arky,kata,etky,kybi,arep):
        self.ak = arky
        self.ka = kata
        self.ek = etky
        self.ky = kybi
        self.ae = arep
c1 = car('AXA5674','Ford',2003,1600,5)
c2 = car('ΙΝΑ9481','FIAT',2001,1100,4)
print ( 'Το αυτοκίνητο με αριθμό κυκλοφορίας : ' + c1.ak + ' είναι κατασκευασμένο από την ' +  c1.ka )
print ( 'Το αυτοκίνητο με αριθμό κυκλοφορίας : ' + c2.ak + ' είναι κατασκευασμένο από την ' +  c2.ka )
class car:
    def __init__(self,arky,kata,etky,kybi,arep):
        self.ak = arky
        self.ka = kata
        self.ek = etky
        self.ky = kybi
        self.ae = arep

    def forologika(self):
        a = self.ak , str( self.ek ) , str( self.ky )# τo + εγινε , για διαχωρισμο
        return a

c1 = car('AXA5674','Ford',2003,1600,5)
print ('Εκτυπωση του Ford=', c1.forologika() )
c2 = car('INA9481','FIAT',2001,1100,4)
print ('Εκτυπωση του FIAT=', c2.forologika() )
print ( 'H μεταφορική ικανότητα των ' + c1.ak + '  + ' + c2.ak + '  ' + str( c1.ae + c2.ae ) + ' ατομα ' )
