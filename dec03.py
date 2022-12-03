
import common.filereader as fr 

def split_input( input_string ):
    half = int(len(input_string) / 2) 
    set1 = set(input_string[0:half])
    set2 = set(input_string[half:]) 

    return set1, set2 

def get_priority( letter ):

    priority = 0  

    if ( letter.isupper() ):
        priority = (ord(letter) - ord('A')) + 27 
    else:
        priority = (ord(letter) - ord('a')) + 1 

    return priority 

def first(filepath): 

    total_priority = 0 

    inputlines = fr.readfile(filepath)

    for line in inputlines: 
        set1, set2 = split_input(line) 
        common = set1.intersection(set2) 
        for item in common: 
            total_priority += get_priority(item) 
    
    print(f"Total priority = {total_priority}")

def second(filepath): 

    total_priority = 0 

    inputlines = fr.readfile(filepath) 

    for i in range(0, len(inputlines), 3): 
        set1 = set(inputlines[i])
        set2 = set(inputlines[i+1])
        set3 = set(inputlines[i+2])

        common = set1.intersection(set2).intersection(set3) 

        for item in common: 
            total_priority += get_priority(item) 

    print(f"Total priority = {total_priority}")
        

if __name__ == "__main__":

    first("input/input03.txt") 
    second("input/input03.txt")