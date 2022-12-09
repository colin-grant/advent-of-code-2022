
import common.filereader as fr 

def do_move_1(line, headpos, tailpos, visited_set):

    dir, num = line.split(" ")

    num = int(num) 
    dir = dir.strip() 

    tx, ty = tailpos 
    hx, hy = headpos 
    dx = 0 # delta x
    dy = 0 # delta y 

    if ( dir == 'D' ):
        dy = -1 
    elif ( dir == 'U' ):
        dy = 1 
    elif ( dir == 'L' ):
        dx = -1 
    elif ( dir == 'R' ):
        dx = 1 

    for _ in range(0,num):
        hx += dx 
        hy += dy 

        if ( abs(tx-hx) > 1 or abs(ty-hy) > 1 ):
            # need to move the tail 
            if ( abs(tx-hx) > 0 ): 
                if ( tx > hx ):
                    tx -= 1 
                else: 
                    tx += 1
            if ( abs(ty-hy) > 0 ):
                if ( ty > hy ):
                    ty -= 1 
                else: 
                    ty += 1 
            visited_set.add((tx,ty)) 

    return (hx,hy), (tx,ty) 

# this version takes a rope with multiple knots (could use to solve part1 - may clean up when have time)
def do_move_2(line, headpos, rope, visited_set):

    dir, num = line.split(" ")

    num = int(num) 
    dir = dir.strip() 

    hx, hy = headpos 
    dx = 0 # delta x
    dy = 0 # delta y 

    if ( dir == 'D' ):
        dy = -1 
    elif ( dir == 'U' ):
        dy = 1 
    elif ( dir == 'L' ):
        dx = -1 
    elif ( dir == 'R' ):
        dx = 1 

    for _ in range(0,num):
        hx += dx 
        hy += dy 

        # need to move all the knots in the rope. 
        x,y = hx,hy 

        for i in range(0,len(rope)): 

            tx,ty = rope[i] 
            if ( abs(tx-x) > 1 or abs(ty-y) > 1 ):
                # need to move the knot  
                if ( abs(tx-x) > 0 ): 
                    if ( tx > x ):
                        tx -= 1 
                    else: 
                        tx += 1
                if ( abs(ty-y) > 0 ):
                    if ( ty > y ):
                        ty -= 1 
                    else: 
                        ty += 1 
                if ( i == len(rope) - 1 ):
                    # This is the tail
                    visited_set.add((tx,ty))
            rope[i] = (tx,ty) 
            x, y = tx, ty # follow the knot just moved. 

    return (hx,hy) 
        
    
def first(filename):

    lines = fr.readfile(filename)

    headpos = (0,0) 
    tailpos = (0,0) 
    visited_set = set() 
    visited_set.add(tailpos) # add the starting location 

    for line in lines: 

        headpos, tailpos = do_move_1(line, headpos, tailpos, visited_set)

    print(f"1: Num positions visited = {len(visited_set)}")

def second(filename):

    lines = fr.readfile(filename)

    rope = list()
    for _ in range(0,9):
        rope.append((0,0))

    headpos = (0,0) 
    visited_set = set() 
    visited_set.add((0,0))
    update_set = True  

    for line in lines:

        headpos = do_move_2(line, headpos, rope, visited_set )

    
    print(f"2: Num positions visited = {len(visited_set)}")


if __name__ == '__main__':

    first("input/input09.txt")
    second("input/input09.txt") 