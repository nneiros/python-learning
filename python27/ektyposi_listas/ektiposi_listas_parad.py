a=['London','Rome',1452,9]# ��������� ������
print '����� =',(a)
print '���� 0=',(a[0])#�������� ��� ����� 0 ��� ������=london,[0,1,2,3,4....] � [....-3,-2,-1]
print '���� 2=',(a[2])#�������� ��� ����� 2 ��� ������
print '�������� ����� 0 ��� 1=', (a[0 ] + a[1]) # ��������� ��� ��� ������ ��� ��� ����� [0+1]
print '�������� ����� 2 ��� 3(�������)=',(a[2] + a[3])# ��������� ��� ��� ������ ��� ��� ����� [2+3],������� ���� ����� ��� �� ��� ����� �������
print '�������� ���� 0 ��� 2(������� ���� 2 �������)=',a[0],+a[2]# ������ ������ ������ ����� ��� �� ��� ��� ����� ����=strings
print '���� 3=',(a[3])
print '���� -2=',(a[-2])
print '���� 1 ��� 3=',a[1:3]# �������� ��� ������ 1 ��� 3 ����� �� ���� �� 3.
print '���� 1 ��� -1=',(a[1:-1])# �������� ��� ������ �� ���������� ��������
print '���� 0 ��� 3=',(a[:3])  # �������� ��� ������ 0 ��� 3, �� 0 �� ������.
a.append(114)# �������� �o 114 ��� �����
print '����������� �� 114=',(a)
a.insert(2,'Paris')# ��������� ��� ����� �� ������������ ����
print '����������� Paris �� ���� 2=',(a)
a.extend(['Milano',1812])#��������� ��� ����� ��� ������
print '�����������,Milano ��� 1812 ��� ����� ��� ������=',(a)
a.remove(9)#��������� ��� �� ����� ��� ������ �����[0,1,2....]
print '�������� ��� 9 ���������=',(a)
c=a.pop()# ������� �� ��������� ����� ��� ������ ��� �� ����������
print '�������� ��� ���������� ������=',(c) # �������� ��� ���������� ������ ��� �� �������
print '�������� ��� ���������� ������=',(a) # �������� ��� ����������
print '���� ���� ������� ���������-1452,=',(a.index(1452)) # �� ��� ������ �������� ��� ������ ��� ���������� ��� (���� ���) ��� �����
print '���� ���� ���� � �����=',len (a)# ���� ���� ���� ��� �����
# �� ����� ������� ������ �� �������� ���� a=[1,2,3,4]->sum(a)=10
print '�������� ���� �������=', range (8)# �������� ���� ������� �������
print '�������� ��� ����� ����� ����=', range (5,15)#�������� ���� ������� �������
print '�������� ��� 0 ��� 30 �� ���� 5=', range (0,30,5) #�o 5 ����� ����,�� ���� ���� ��� ����� ��������� ��� ��� ���� ������ ����
print '�������� ��� 100 ��� 0 �� ���� -20=', range (100,0,-20)
