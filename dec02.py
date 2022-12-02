
import common.filereader as fr 

def calc_score( opp, you ):
    
    score = 0 

    if ( opp == 'A'): # rock
        if ( you == 'X' ):
            score = 1 + 3  
        elif ( you == 'Y' ):
            score = 2 + 6  
        else: 
            score = 3 + 0 

    if ( opp == 'B'): # paper
        if ( you == 'X' ):
            score = 1 + 0  
        elif ( you == 'Y' ):
            score = 2 + 3  
        else: 
            score = 3 + 6 

    if ( opp == 'C'): # scissors
        if ( you == 'X' ):
            score = 1 + 6  
        elif ( you == 'Y' ):
            score = 2 + 0  
        else: 
            score = 3 + 3

    return score  



def first(): 

    score = 0 

    filelines = fr.readfile("input/input02.txt") 

    for line in filelines:
        if ( len(line) > 0 ):
            opp, you = line.split() 

            score += calc_score(opp, you)

    print(f"Total Score = {score}")


def second():

    score = 0 

    filelines = fr.readfile("input/input02.txt") 

    for line in filelines:
        if ( len(line) > 0 ):
            opp, result = line.split() 

            if ( result == 'X' ):
                # need to lose
                if ( opp == 'A' ):
                    you = 'Z' 
                elif ( opp == 'B' ):
                    you = 'X' 
                else:
                    you = 'Y' 
            if ( result == 'Y' ):
                # need to draw
                if ( opp == 'A' ):
                    you = 'X' 
                elif ( opp == 'B' ):
                    you = 'Y' 
                else:
                    you = 'Z' 
            if ( result == 'Z' ):
                # need to win
                if ( opp == 'A' ):
                    you = 'Y' 
                elif ( opp == 'B' ):
                    you = 'Z' 
                else:
                    you = 'X' 

            score += calc_score(opp, you)

    print(f"Total Score = {score}")
    

if __name__ == "__main__": 

    first() 
    second() 

