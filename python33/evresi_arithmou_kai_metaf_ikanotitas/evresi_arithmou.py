# -*- coding: cp1253 -*-
import random
thenumber = random.randint(1,50)
print "��� ������� ��� ������ ��� �� 1 ��� �� 50.'
print "������� �� �� �����?"
guess = 0
while guess != thenumber:
  guess = input("���� ��� ������: ")
  if guess > thenumber:
    print "������ ���������� ������!"
  if guess < thenumber:
    print "������ ��������� ������!"
  if guess == thenumber:
    print "����� ��� ������!!!"
