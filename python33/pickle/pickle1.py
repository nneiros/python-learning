import pickle

def main():

    # Creating objects we want to pickle, write, to a file.
    pickleObjects = ["home", "library", "garage", "garden", "pool", "car"]
    print (pickleObjects)

    # Pickling, writing, to a file.
    outFile = open('pickleExample.txt', 'wb')
    pickle.dump(pickleObjects, outFile)
    outFile.close()

    # Un-pickling, reading, from a file.
    inFile = open('pickleExample.txt', 'rb')
    unPickledObjects = pickle.load(inFile)
    print (unPickledObjects)
    inFile.close()

if __name__ == '__main__':
    main()
