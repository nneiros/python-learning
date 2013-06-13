print('---------------------------------------------------------------------------------------')

import pickle
# το αρχειο που θα αποθηκευτουν τα δεδομενα
shoplistfile = 'shoplist.data'

# λιστα με τα πραγματα που θα αγορασω 
shoplist = 'μηλο', 'πορτοκαλι', 'καροτο'
                
               
# Write to the file
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) # dump the object to a file
f.close()

del shoplist # destroy the shoplist variable

# Read back from the storage
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # load the object from the file
#for line in storedlist:
print('....Η λιστα εχει',storedlist) 
f.close()
#(storedlist)
