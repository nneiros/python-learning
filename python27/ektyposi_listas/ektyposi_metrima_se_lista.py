# Μια λίστα για ψώνια:
shoplist = ['*μήλα*', '*πορτοκάλια*', '*καρότα*', '*μπανάνες*']
 
print 'Έχω ν\' αγοράσω', len(shoplist), 'πράγματα.'#μετραει τα πραγματα
 
print 'Τα ψώνια μου είναι:', # Παρατηρήστε το κόμμα στο τέλος της συμβολοσειράς
for item in shoplist:
  print item,
print ('*************************************') 
print '\nΕπίσης θέλω να αγοράσω ,ρύζι.'
shoplist.append('ρύζι')
print 'Τα ψώνια μου τώρα είναι:',
for item in shoplist:
  print item,
print ('*************************')
print '\nΤώρα θα ταξινομήσω τη λίστα μου.'
shoplist.sort()
print 'Η ταξινομημένη λίστα είναι:',
for item in shoplist:
  print item,
print ('*************************')
print '\nΤο πρώτο πράγμα που θ\' αγοράσω είναι:', shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print 'Τώρα που αγόρασα τα', olditem, 'η λίστα μου είναι:',
for item in shoplist:
  print item,
