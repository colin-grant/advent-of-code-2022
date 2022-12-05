
def readfile( filename, strip=True ):

    filelines = list()

    with open(filename) as file:
        for line in file:
            if ( strip ):
                filelines.append(line.strip()) 
            else:
                filelines.append(line)
    
    return filelines 

