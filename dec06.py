
import common.filereader as fr 

def find_marker(data, window_size): 

    chars_received = window_size 

    for i in range(0, len(data) - window_size):
        window_set = set(data[i:i+window_size]) 
        if ( len(window_set) == window_size ):
            break 
        chars_received += 1 
    
    return chars_received 


def first(filename): 

    # Should only be one line - but processing multiple allows us to throw all the examples into a single 
    # file and test for the correct results. 
    filelines = fr.readfile(filename) 

    for line in filelines:

        marker_position = find_marker(line, 4) 

        print(f"Marker Received at position {marker_position}") 

def second(filename):
    
    filelines = fr.readfile(filename) 

    for line in filelines:

        marker_position = find_marker(line, 14) 

        print(f"Marker Received at position {marker_position}") 



if __name__ == '__main__': 

    print("--- first ---")
    first("input/input06.txt")
    print("--- second ---") 
    second("input/input06.txt") 
     