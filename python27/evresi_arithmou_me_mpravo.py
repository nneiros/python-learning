import random
thenumber = random.randint(1,50)
name = raw_input("���� �� ����� ���")
print "��� ������� ��� ������ ��� �� 1 �� �� 50."
print "������� �� ��� �����?"
guess = 0
tries = 0
while guess != thenumber:
  tries=tries + 1
  guess = input("���� ��� ������: ")
  if guess > thenumber:
    print "������ ���������� ������!"
  if guess < thenumber:
    print "������ ��������� ������!"
  if guess == thenumber:
    print "������������", name, "��� ������ ��", tries, "�����������!"
