#������� ��� ������ ball:
class ball:
      def bounce(self):
          if self.direction==�down�:
             self.direction=�up�
my_ball=ball() #���������� ������������
#������� ����� ��� ��������� ����� ���:
my_ball.direction=�down�
my_ball.color=�green�
my_ball.size=�middle�
print ������ ����������� ��� ����� ��:�
print �����������:�,my_ball.direction
print ������:�,my_ball.color
print ��������:�,my_ball.size
print ����� ��� ���� ���������!�
my_ball.bounce()
print ���� ����������:�,my_ball.direction
