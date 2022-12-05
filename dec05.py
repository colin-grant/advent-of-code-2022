import common.filereader as fr 
import collections 

def parse_input(filename):

    filelines = fr.readfile(filename, strip=False) 

    # To read in the stacks we know that the input is fixed width. 
    num_stacks = (len(filelines[0]) // 4) # this takes into account the final newline character 
    
    stacks = list() 

    for i in range(0,num_stacks):
        stacks.append(collections.deque()) 

    instructions = list() 

    state = 'READING_STACKS' 

    for line in filelines :
        if ( state == 'READING_STACKS' ):
            if not line.startswith(" 1 "):
                for i in range(1, len(line), 4):
                    if ( line[i] != ' ' ):
                        stacks[(i-1) // 4].appendleft(line[i])
            else: 
                state = 'LOADING_INSTRUCTIONS'
        else:
            if ( line.startswith("move") ):
                instruction_tuple = parse_instruction_line(line) 
                instructions.append(instruction_tuple) 

    return stacks, instructions 


def parse_instruction_line(line): 
    #take out the 'move ' start. 
    line = line[5:]     
    num_blocks, rest = line.split('from')
    num_blocks = int(num_blocks.strip()) 
    source, dest = rest.split('to') 
    source = int(source.strip())
    dest = int(dest.strip())

    return( source, dest, num_blocks )

def move_crates_1( stacks, inst ): 
    source, dest, num_crates = inst

    for i in range(0,num_crates): 
        popped = stacks[source-1].pop() 
        stacks[dest-1].append(popped) 

# Could do this by list slicing - but already invested in deques. 
def move_crates_2( stacks, inst ): 
    source, dest, num_crates = inst
    temp = collections.deque() 

    for i in range(0,num_crates): 
        popped = stacks[source-1].pop()
        temp.append(popped) 
    for i in range(0,num_crates): 
        popped = temp.pop() 
        stacks[dest-1].append(popped) 


def follow_instructions_1( stacks, instructions ):
    for inst in instructions:
        move_crates_1( stacks, inst ) 

def follow_instructions_2( stacks, instructions ):
    for inst in instructions:
        move_crates_2( stacks, inst ) 


def first(filename):

    stacks, instructions = parse_input(filename) 
    follow_instructions_1( stacks, instructions )

    result = "" 
    for i in range(0,len(stacks)):
        result += stacks[i].pop() 

    print(f"Result = [{result}]")

def second(filename):

    stacks, instructions = parse_input(filename) 
    follow_instructions_2( stacks, instructions )

    result = "" 
    for i in range(0,len(stacks)):
        result += stacks[i].pop() 

    print(f"Result = [{result}]")

if __name__ == '__main__':

    # Lets parse the data a bit first. 

    first("input/input05.txt")
    second("input/input05.txt")