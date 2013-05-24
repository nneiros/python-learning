import pickle
picklelist = ['one',2,'three','four',5,'can you count?']
file = open('filename', 'wb')
pickle.dump(picklelist,file)
file.close()

unpicklefile = open('filename', 'rb')
unpickledlist = pickle.load(unpicklefile)
unpicklefile.close()
for item in unpickledlist:
    print (item)
