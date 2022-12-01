
def readfile( filename ):

    filelines = list()

    with open(filename) as file:
        print("opened file")
        for line in file:
            filelines.append(line) 
    
    return filelines 
