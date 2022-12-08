
import common.filereader as fr 
import numpy as np 

class Tree():

    def __init__(self, height): 
        self.height = int(height) 
        self.counted = False 

def load_data_into_array(filelines, datatype):

    data = list() 

    for line in filelines:
        dataline = list(map(datatype, line)) 
        data.append(dataline) 

    return np.array(data) 

def count_visible_trees(tree_array):

    tree_count = 0 

    for row in tree_array:
        tallest_tree = -1 
        for tree in row: 
            if tree.height > tallest_tree:
                if ( not tree.counted ): 
                    tree_count += 1
                    tree.counted = True 
                     
                tallest_tree = tree.height 

    return tree_count 

def get_scenic_score(height, view): 
    scenic_score = 0 
    for i in view: 
        scenic_score += 1 
        if ( i >= height ):
            break 

    return scenic_score  

def first(filename): 

    filelines = fr.readfile(filename) 
    tree_array = load_data_into_array(filelines, Tree) 

    tree_count = 0  
    for _ in range(0,4): 
        tree_count += count_visible_trees(tree_array) 
        # By rotating the array we can count from the left, right, top and bottom with the same function. 
        tree_array = np.rot90(tree_array) 

    print(f"Num visible trees = {tree_count}")


def second(filename):

    filelines = fr.readfile(filename) 
    tree_array = load_data_into_array(filelines, int)
    max_scenic_score = 0 
    # go through the rows and columns - ignore the edges, since they always have a score of zero. 
    for r in range(1,tree_array.shape[0]-1):
        for c in range(1,tree_array.shape[1]-1): 
            scenic_score = 1 
            height = tree_array[r,c] 
            # look left
            scenic_score *= get_scenic_score(height, tree_array[r][c-1::-1]) 
            # look right
            scenic_score *= get_scenic_score(height, tree_array[r][c+1:])
            # look up
            scenic_score *= get_scenic_score(height, tree_array[r-1::-1,c])
            # look down  
            scenic_score *= get_scenic_score(height, tree_array[r+1:,c])

            print(f"[{r},{c}] : {scenic_score}")

            if ( scenic_score > max_scenic_score ):
                max_scenic_score = scenic_score 

    print(f"Max scenic score = {max_scenic_score}")   

    
    pass 

if __name__ == '__main__': 

    first("input/input08.txt")
    second("input/input08.txt") 