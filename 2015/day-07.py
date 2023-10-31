from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [[i.split(' -> ')[0].split(' '), i.split(' -> ')[1]] for i in fin.read().rstrip().split("\n")]
    return data

def process_data_1(data):
    values = {}
    visited_gates = []
    while len(data) > len(visited_gates):
        prev_step = len(visited_gates)
        for step, row in enumerate(data):
            if step in visited_gates: continue
            operation, destination = row[0], row[1]
            if len(operation) == 1: 
                if operation[0].isnumeric():
                    values[destination] = int(operation[0])
                    visited_gates.append(step)
                elif ((operation[0] in values) and (not operation[0].isnumeric())): 
                    values[destination] = values[operation[0]]
                    visited_gates.append(step)
            elif (len(operation) == 2) and (operation[1] in values): 
                values[destination] = 65535 - values[operation[1]]
                visited_gates.append(step)
            elif (operation[1] == 'AND'):
                if (operation[0] in values) and (operation[2] in values): 
                    values[destination] = values[operation[0]] & values[operation[2]]
                    visited_gates.append(step)
                elif (operation[0] == '1') and (operation[2] in values): 
                    values[destination] = int(operation[0]) & values[operation[2]]
                    visited_gates.append(step)
            elif (operation[1] == 'OR') and (operation[0] in values) and (operation[2] in values):
                values[destination] = values[operation[0]] | values[operation[2]]
                visited_gates.append(step)
            elif (operation[1] == 'LSHIFT') and (operation[0] in values): 
                values[destination] = values[operation[0]] << int(operation[2])
                visited_gates.append(step)
            elif (operation[1] == 'RSHIFT') and (operation[0] in values): 
                values[destination] = values[operation[0]] >> int(operation[2])
                visited_gates.append(step)
        if len(visited_gates) == prev_step:
            break
    return values['a']

def process_data_2(data):
    # BUCLE 1
    values = {}
    visited_gates = []
    while len(data) > len(visited_gates):
        prev_step = len(visited_gates)
        for step, row in enumerate(data):
            if step in visited_gates: continue
            operation, destination = row[0], row[1]
            if len(operation) == 1: 
                if operation[0].isnumeric():
                    values[destination] = int(operation[0])
                    visited_gates.append(step)
                elif ((operation[0] in values) and (not operation[0].isnumeric())): 
                    values[destination] = values[operation[0]]
                    visited_gates.append(step)
            elif (len(operation) == 2) and (operation[1] in values): 
                values[destination] = 65535 - values[operation[1]]
                visited_gates.append(step)
            elif (operation[1] == 'AND'):
                if (operation[0] in values) and (operation[2] in values): 
                    values[destination] = values[operation[0]] & values[operation[2]]
                    visited_gates.append(step)
                elif (operation[0] == '1') and (operation[2] in values): 
                    values[destination] = int(operation[0]) & values[operation[2]]
                    visited_gates.append(step)
            elif (operation[1] == 'OR') and (operation[0] in values) and (operation[2] in values):
                values[destination] = values[operation[0]] | values[operation[2]]
                visited_gates.append(step)
            elif (operation[1] == 'LSHIFT') and (operation[0] in values): 
                values[destination] = values[operation[0]] << int(operation[2])
                visited_gates.append(step)
            elif (operation[1] == 'RSHIFT') and (operation[0] in values): 
                values[destination] = values[operation[0]] >> int(operation[2])
                visited_gates.append(step)
        if len(visited_gates) == prev_step:
            break
    # BUCLE 2
    values = {'b': values['a']}
    visited_gates = []
    while len(data) > len(visited_gates):
        prev_step = len(visited_gates)
        for step, row in enumerate(data):
            if step in visited_gates: continue
            operation, destination = row[0], row[1]
            if len(operation) == 1: 
                if operation[0].isnumeric():
                    if destination!='b': values[destination] = int(operation[0])
                    visited_gates.append(step)
                elif ((operation[0] in values) and (not operation[0].isnumeric())): 
                    values[destination] = values[operation[0]]
                    visited_gates.append(step)
            elif (len(operation) == 2) and (operation[1] in values): 
                values[destination] = 65535 - values[operation[1]]
                visited_gates.append(step)
            elif (operation[1] == 'AND'):
                if (operation[0] in values) and (operation[2] in values): 
                    values[destination] = values[operation[0]] & values[operation[2]]
                    visited_gates.append(step)
                elif (operation[0] == '1') and (operation[2] in values): 
                    values[destination] = int(operation[0]) & values[operation[2]]
                    visited_gates.append(step)
            elif (operation[1] == 'OR') and (operation[0] in values) and (operation[2] in values):
                values[destination] = values[operation[0]] | values[operation[2]]
                visited_gates.append(step)
            elif (operation[1] == 'LSHIFT') and (operation[0] in values): 
                values[destination] = values[operation[0]] << int(operation[2])
                visited_gates.append(step)
            elif (operation[1] == 'RSHIFT') and (operation[0] in values): 
                values[destination] = values[operation[0]] >> int(operation[2])
                visited_gates.append(step)
        if len(visited_gates) == prev_step:
            break
    return values['a']

if __name__ == "__main__":
    start = pfc()
    day = "07"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
