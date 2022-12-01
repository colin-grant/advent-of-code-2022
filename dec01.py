
import common.filereader as fr 

def first(): 

    filelines = fr.readfile("input1.txt")
    elves = list() 
    cal = 0 

    for line in filelines: 

        if len(line.rstrip()) == 0 :
            print("adding elf cal count") 
            elves.append(cal)
            cal = 0 
        else:
            cal = cal + int(line) 

    max_calories = max(elves) 

    print(f"Max Calories = {max_calories}")

def second():

    filelines = fr.readfile("input1.txt")
    elves = list() 
    cal = 0 

    for line in filelines: 

        if len(line.rstrip()) == 0 :
            elves.append(cal)
            cal = 0 
        else:
            cal = cal + int(line) 

    elves.sort(reverse=True)

    cal = 0 
    for i in range(0,3):
        cal = cal + elves[i] 

    print(f"Total Max Calories = {cal}")
    

if __name__ == "__main__": 

    first() 
    second() 

