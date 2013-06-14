#open file for write
f=open("file1.txt","w")

#print (f)
f.write('αβγδεζηθικλμνξοπρστ\n')
f.write('υφχψω123456789');

#open file for read
f=open('file1.txt','r')#diavazei mono apo to arxeio

# pieces reading
z=f.read()
print ('Αυτο ειναι το αρχειο τωρα=',z)

f=open('file1.txt','r')
s1=f.read(5)
print ('Διαβασε 5 στοιχεια απο το αρχειο=',s1)
s2=f.read(19)
print ('Διαβασε τα επομενα 19 στοιχεια απο το αρχειο=',s2)
s2=f.read(25)
print ('Διαβασε τα επομενα 25 στοιχεια απο το αρχειο οσα υπαρχουν=',s2)
f.close()
#open file for read
f=open('file1.txt','r')

# pieces reading
s1=f.read(5)
print ('Διαβασε 5 στοιχεια απο το αρχειο=',s1)
print ('Διαβασε και επεστρεψε την τρεχουσα θεση=',f.tell())
s2=f.read(19)
print ('Διαβασε τα επομενα 19 στοιχεια απο το αρχειο=',s2)
print ('Διαβασε και επεστρεψε την τρεχουσα θεση=',f.tell())
s2=f.read(25)
print ('Διαβασε τα επομενα 25 στοιχεια απο το αρχειο οσα υπαρχουν=',s2)
print ('Διαβασε και επεστρεψε την τρεχουσα θεση =',f.tell())
f.close()

# seek
f=open('file1.txt','r+')#diavazei kai prosthetei sto arxeio r+
f.write('0123456789abcdef')
f.seek(0)
print('************************************************************************')
print('Αυτο εχει προστεθει στην αρχη του αρχειου=',f.read(16))
f.write('0123456789abcdef')
f.seek(5)     # Go to the 6th byte in the file
print ('Aπo το 5ο byte και μετα διαβαζω 2 στοιχεια=',f.read(2))        
f.seek(13) # Go to the 3rd byte before the end
print ('Aπο το 13ο byte και μετα διαβαζω 1 στοιχειο=',f.read(1))
print('************************************************************************')
#--------------------------------------------------------------------------------------------------------------------
#anoigma kai diavasma arxeiou
file = open ( 'words.dat' , 'w' )
word = ','
while word != 'END' :
      word = input ( 'Δωσε μια λεξη θα την βρεις στο αρχειο words.dat (γραψε END για εξοδο): ')
      file.write ( word + ',' )
file.close ( )
file=open('words.dat','r')
f=file.readlines()
print(f)
file.close()
