import common.filereader as fr 

# normally I'd use a class to hold the monkeys - but I'll try a python dictionary this time. 
def load_monkeys(filename):

    current_monkey = None 
    monkeys = list() 
    lines = fr.readfile(filename)  
    for line in lines:
        if line.startswith('Monkey'):
            current_monkey = dict()
            current_monkey['inspected'] = 0
            monkeys.append(current_monkey) 
        elif current_monkey != None:
            if line.startswith('Starting items'):
                current_monkey['items'] = list() 
                if len(line) > 16:
                    for item in line[15:].split(','):
                        current_monkey['items'].append(int(item.strip()))
            elif line.startswith('Operation'): 
                current_monkey['operator'], current_monkey['operator_amount'] = line[21:].split(' ')
            elif line.startswith('Test'):
                current_monkey['test_div'] = int(line[19:])
            elif line.startswith('If true'):
                current_monkey['true_action'] = int(line[25:])
            elif line.startswith('If false'):
                current_monkey['false_action'] = int(line[26:])

    return monkeys 

def calc_worry_level(monkey, item):
    worry_level = 0 

    operator_amount = monkey['operator_amount'] 
    if operator_amount == 'old':
        operator_amount = item 
    else:
        operator_amount = int(monkey['operator_amount'])

    if ( monkey['operator'] == '*' ):
        worry_level = item * operator_amount
    elif (monkey['operator'] == '+' ):
        worry_level = item + operator_amount
    return worry_level 

def calc_monkey_business(monkeys, num_rounds, relief_func, manage_worry_func):
    for x in range(0,num_rounds):
        for monkey in monkeys:
            for i in range(0,len(monkey['items'])):
                monkey['inspected'] += 1 
                worry_level = monkey['items'][i]
                test_div = monkey['test_div']
                worry_level = calc_worry_level(monkey, worry_level)
                worry_level = relief_func(worry_level)
                if ((worry_level % test_div) == 0):
                    monkey_to_receive = monkeys[monkey['true_action']]
                else:
                    monkey_to_receive = monkeys[monkey['false_action']] 
                monkey_to_receive['items'].append(manage_worry_func(worry_level))

            monkey['items'] = list() 

    active_monkeys = sorted(monkeys, reverse=True, key=lambda a: a['inspected'])

    monkey_business = active_monkeys[0]['inspected'] * active_monkeys[1]['inspected']

    return monkey_business 

def first(filename):
    monkeys = load_monkeys(filename) 

    #using lambda functions to control the update and worry level management. 
    #not used lambda functions before in python. 
    monkey_business = calc_monkey_business(monkeys, 20, lambda a : a // 3, lambda a : a )
    print(f"1: monkey business = {monkey_business}")
    
def second(filename):

    monkeys = load_monkeys(filename) 

    # need to store the worry levels as a modulus of the product of all the monkey divisors,
    # otherwise the numbers get too big. 
    big_div = 1 
    for monkey in monkeys:
        big_div *= monkey['test_div'] 

    # using a lambda function means we don't have to pass big_div into the calc_monkey_business 
    # function which is quite nice. 
    monkey_business = calc_monkey_business(monkeys, 10000, lambda a: a, lambda a: a % big_div) 
    print(f"2: monkey_business = {monkey_business}")


first("input/input11.txt")
second("input/input11.txt")


