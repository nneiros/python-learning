# ��� ����� ��� �����:
shoplist = ['����', '����������', '������', '��������']
 
print '��� �\' �������', len(shoplist), '��������.'
 
print '�� ����� ��� �����:', # ����������� �� ����� ��� ����� ��� �������������
for item in shoplist:
  print item,
 
print '\n������ ���� �� ������� ����.'
shoplist.append('����')
print '�� ����� ��� ���� �����:',
for item in shoplist:
  print item,
 
print '\n���� �� ���������� �� ����� ���.'
shoplist.sort()
print '� ������������ ����� �����:',
for item in shoplist:
  print item,
 
print '\n�� ����� ������ ��� �\' ������� �����:', shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print '���� ��� ������� ��', olditem, '� ����� ��� �����:',
for item in shoplist:
  print item,
