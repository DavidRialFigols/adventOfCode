from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split("\n")
    return data

def process_data_1(data):
    values = []
    strength = 1
    cycle = 0
    for instr in data:
        if instr == 'noop':
            cycle += 1
            if cycle in [20,60,100,140,180,220]:
                values.append(strength*cycle)
        elif 'addx' in instr:
            cycle += 1
            if cycle in [20,60,100,140,180,220]:
                values.append(strength*cycle)
            cycle += 1
            if cycle in [20,60,100,140,180,220]:
                values.append(strength*cycle)
            strength += int(instr.split()[1])   
    return sum(values)

def do_a_cycle(cycle, x, line, lines):
    cycle += 1
    if x <= cycle and cycle <= x+2:
        line += ' #'
    else:
        line += ' .'

    if cycle%40 == 0:
        lines.append(line)
        line = ''
        cycle = 0

    return cycle, line 

def print_crt(lines):
    for line in lines:
        print(line)

def process_data_2(data):
    lines = []
    line = ''
    x = 1
    cycle = 0
    for instr in data:
        if instr == 'noop':
            cycle, line = do_a_cycle(cycle, x, line, lines)
            
        elif 'addx' in instr:
            cycle, line = do_a_cycle(cycle, x, line, lines)
            cycle, line = do_a_cycle(cycle, x, line, lines)
            x += int(instr.split()[1])      
    print_crt(lines)
    return lines

if __name__ == "__main__":
    start = pfc()
    day = "10"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
