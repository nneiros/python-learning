class car:
    def __init__(self,arky,kata,etky,kybi,arep):
        self.ak = arky
        self.ka = kata
        self.ek = etky
        self.ky = kybi
        self.ae = arep
c1 = car('AXA5674','Ford',2003,1600,5)
c2 = car('���9481','FIAT',2001,1100,4)
print ( '�� ���������� �� ������ ����������� : ' + c1.ak + ' ����� �������������� ��� ��� ' +  c1.ka )
print ( '�� ���������� �� ������ ����������� : ' + c2.ak + ' ����� �������������� ��� ��� ' +  c2.ka )
class car:
    def __init__(self,arky,kata,etky,kybi,arep):
        self.ak = arky
        self.ka = kata
        self.ek = etky
        self.ky = kybi
        self.ae = arep

    def forologika(self):
        a = self.ak + str( self.ek ) + str( self.ky )
        return a

c1 = car('AXA5674','Ford',2003,1600,5)
print ( c1.forologika() )
c2 = car('���9481','FIAT',2001,1100,4)
print ( c2.forologika() )
print ( '���������� ��������� ��� ' + c1.ak + '  + ' + c2.ak + '  ' + str( c1.ae + c2.ae ) + ' ����� ' )
