the_count = [1, 2, 3, 4, 5]
fruits = ['����', '����������', '��������', '�������']
change = [1, 'penes', 2, 'dekares', 3, 'tetarta']

# this first kind of for-loop goes through a list
for number in the_count:
    print "���� ����� � ������� %d" % number

# same as above
for fruit in fruits:
    print "��� ������ ��� �����: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "���� %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "� ��������  %d ��� �����." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "�������� ����: %d" % i
#print (fruits)
print('----------------------------------------------------------------------------------------------------------------------------')
hairs = ['�������', '�����', '�������' ]
eyes = ['����', '����', '�������']
weits = [1, 2, 3, 4]

for hair in hairs :
    print "����� ������� :  %s "  % hair
for eye in eyes :
    print "����� ������ :  %s" % eye
