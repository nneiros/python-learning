x=1
while x <= 3:
    password=raw_input('���� ������:')
    if password.endswith('1234'):
        print '����� ������'
        break  
    else:
        print '� ������� ����� �����'
        x=x+1
else: 
    print '������ ����� ����� ����� ���� ����.'
