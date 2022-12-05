import common.filereader as fr 

def extract_ranges( line ):
    
    range_list = list() 
    
    range_strings = line.split(',')

    for range_string in range_strings:

        lower_str, upper_str = range_string.split('-')
        range_lower_upper = (int(lower_str), int(upper_str))
        range_list.append(range_lower_upper) 

    # should just have 2 ranges 
    return range_list[0], range_list[1] 

def is_contained(range1, range2):

    low1, upp1 = range1 
    low2, upp2 = range2 

    if ( ((low1 <= low2) and (upp1 >= upp2))
        or ((low2 <= low1) and (upp2 >= upp1)) ):
        return True 

    return False 

def is_overlap(range1, range2):

    low1, upp1 = range1 
    low2, upp2 = range2 

    if (    ((low2 >= low1) and (low2 <= upp1)) 
        or  ((upp2 >= low1) and (upp2 <= upp1)) ): 

        return True 

    return False 

def first(filename): 

    contained_count = 0 

    filelines = fr.readfile(filename) 

    for line in filelines:

        range1, range2 = extract_ranges(line) 

        if is_contained(range1, range2):
            contained_count += 1 

    print(f"Total number of contained ranges = {contained_count}")

def second(filename): 

    overlap_count = 0 

    filelines = fr.readfile(filename) 

    for line in filelines:

        range1, range2 = extract_ranges(line) 

        if is_overlap(range1, range2) or is_overlap(range2, range1):
            overlap_count += 1 

    print(f"Total number of overlapping ranges = {overlap_count}")



if __name__ == "__main__":

    first("input/input04.txt") 
    second("input/input04.txt")
    