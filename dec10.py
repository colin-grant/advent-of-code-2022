import common.filereader as fr 

def first(filename):
    
    cycle_marker = 20
    cycle_count = 0 
    signal_strength = 0
    x = 1 

    lines = fr.readfile(filename) 

    for line in lines: 
        if line.startswith('noop'): 
            cycle_count += 1 
        else:
            cycle_count += 2 
        
        if cycle_count >= cycle_marker: 
            cycle_signal_strength = (cycle_marker * x)
            signal_strength += cycle_signal_strength 
            cycle_marker += 40 
            if cycle_marker > 220: 
                break 
        
        if line.startswith('addx'):
            _,num = line.split(' ')
            num = int(num) 
            x += num 

    print(f"Signal Strength = {signal_strength}")


def second(filename):

    cycle_marker = 20
    cycle_count = 0 
    signal_strength = 0
    x = 1 

    lines = fr.readfile(filename)
    current_instr = 0
    instr_count = 0  
    crt = [' '] * 240  
    
    while current_instr < len(lines):
        for crt_pos in range(0,240): 

            horizontal_pos = crt_pos % 40 
            if ( horizontal_pos >= x-1 and horizontal_pos <= x+1 ): 
                crt[crt_pos] = '#' 

            instr = lines[current_instr] 
            if instr.startswith('noop'): 
                # move to next instruction
                current_instr += 1 
                instr_count = 0 
            elif instr.startswith('addx'):
                instr_count += 1 # num cycles this command has been running for.  
                if ( instr_count > 1 ): 
                    _,num = instr.split(' ')
                    num = int(num) 
                    x += num

                    current_instr += 1
                    instr_count = 0  

    for i in range(0,240, 40): 
        print("".join(crt[i:i+40]))

# stopped using if __name__ == "main" from now on since this file will never be imported 

first("input/input10.txt")
second("input/input10.txt")