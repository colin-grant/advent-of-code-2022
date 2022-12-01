
import common.filereader as fr 

def build_elf_totals():

    filelines = fr.readfile("input/input1.txt")
    elves = list() 
    cal = 0 

    for line in filelines: 

        if len(line.rstrip()) == 0 :
            elves.append(cal)
            cal = 0 
        else:
            cal = cal + int(line) 

    return elves 

def first(elves): 

    max_calories = max(elves) 

    print(f"Max Calories = {max_calories}")

def second(elves):

    elves.sort(reverse=True)

    cal = 0 
    for i in range(0,3):
        cal = cal + elves[i] 

    print(f"Total Max Calories = {cal}")
    

if __name__ == "__main__": 

    elves = build_elf_totals() 

    first(elves) 
    second(elves) 

