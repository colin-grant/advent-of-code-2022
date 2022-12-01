
def readfile( filename ):

    filelines = list()

    with open(filename) as file:
        for line in file:
            filelines.append(line) 
    
    return filelines 
