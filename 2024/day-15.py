from hmac import new
from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        aux = [i.split('\n') for i in fin.read().rstrip().split("\n\n")]
        data = {'walls': [], 'boxes': [], 'moves': ''.join(aux[1])}
        for x, row in enumerate(aux[0]):
            for y, el in enumerate(row):
                if el=='#': data['walls'].append((x,y))
                elif el=='O': data['boxes'].append((x,y))
                elif el=='@': data['robot'] = (x,y)
    return data

def check_box(data, pos, m):
    while pos in data['boxes']:
        pos = (pos[0]+m[0], pos[1]+m[1])
    return pos not in data['walls'], pos

def print_state(data):
    height = max([max([i[0] for i in data['walls']]), max([i[0] for i in data['boxes']]), data['robot'][0]])
    width = max([max([i[1] for i in data['walls']]), max([i[1] for i in data['boxes']]), data['robot'][1]])

    for x in range(height+1):
        line = ''
        for y in range(width+1):
            if (x,y) in data['walls']: line += '#'
            elif (x,y) in data['boxes']: line += 'O'
            elif (x,y)==data['robot']: line += '@'
            else: line += '.'
        print(line)

def process_data_1(data):
    moves = {
        '^': (-1,  0),
        '>': ( 0,  1),
        'v': ( 1,  0),
        '<': ( 0, -1)
    }
    for m in data['moves']:
        next_pos = (data['robot'][0]+moves[m][0],data['robot'][1]+moves[m][1])
        if next_pos in data['walls']: continue
        if next_pos in data['boxes']: 
            should_move, pos = check_box(data, next_pos, moves[m])
            if should_move: 
                data['boxes'].append(pos)
                data['boxes'].remove(next_pos)
                data['robot'] = next_pos
        else:
            data['robot'] = next_pos
        #print_state(data)
    return sum([100*pos[0]+pos[1] for pos in data['boxes']])

def enlarge_map(data):
    new_data = {'walls': [], 'boxes': [], 'robot': (data['robot'][0], data['robot'][1]*2), 'moves': data['moves']}
    
    for w in data['walls']:
        new_data['walls'] += [(w[0],w[1]*2), (w[0], w[1]*2+1)]

    for w in data['boxes']:
        new_data['boxes'].append((w[0],w[1]*2)) #we only store the left part of the boxes
    return new_data

def print_state_2(data):
    height = max([max([i[0] for i in data['walls']]), max([i[0] for i in data['boxes']]), data['robot'][0]])
    width = max([max([i[1] for i in data['walls']]), max([i[1]+1 for i in data['boxes']]), data['robot'][1]])

    for x in range(height+1):
        line = ''
        for y in range(width+1):
            if (x,y) in data['walls']: line += '#'
            elif (x,y) in data['boxes']: line += '['
            elif (x,y-1) in data['boxes']: line += ']'
            elif (x,y)==data['robot']:
                line += '@'
            else: line += '.'
        print(line)

def check_box_2_v(data, pos, m):
    to_check = [pos]
    to_remove = []
    to_add = []
    visited = set()
    while len(to_check) > 0:
        pos = to_check.pop()
        if pos in visited: continue
        visited.add(pos)
        np = (pos[0]+m, pos[1])
        if pos in data['walls']:
            return False, [], []
        if pos in data['boxes']:
            to_check += [np, (np[0], np[1]+1)]
            if (pos[0]+m, pos[1]) not in data['boxes']:
                to_add.append((pos[0]+m, pos[1]))
            if (pos[0]-m, pos[1]) not in data['boxes']:
                to_remove.append(pos)
            if (np not in data['boxes']) and ((np[0], np[1]+1) in data['boxes']):
                to_add.append(np)
        elif (pos[0], pos[1]-1) in data['boxes']:
            to_check.append((pos[0], pos[1]-1))
        else: 
            if (pos[0]-m, pos[1]) in data['boxes'] and pos not in data['boxes']:
                to_add.append(pos)
    
    return True, list(set(to_add)), list(set(to_remove))

def check_box_2_h(data, pos, m):
    to_remove = []
    to_add = []
    if m==-1:
        pos = (pos[0], pos[1]-1)
    while pos in data['boxes'] or (pos[0], pos[1]+m) in data['boxes']:
        if pos in data['boxes']:
            to_remove.append(pos)
            to_add.append((pos[0], pos[1]+m))
        pos = (pos[0], pos[1]+m) 
    if m==-1: 
        return pos not in data['walls'], to_remove, to_add
    else: 
        return (pos[0], pos[1]+m) not in data['walls'], to_remove, to_add

def process_data_2(data):
    moves = {
        '^': (-1,  0),
        '>': ( 0,  1),
        'v': ( 1,  0),
        '<': ( 0, -1)
    }
    
    data = enlarge_map(data) #Obtain new map

    for m in data['moves']:
        next_pos = (data['robot'][0]+moves[m][0],data['robot'][1]+moves[m][1])
        if next_pos in data['walls']: continue
        if moves[m][0]==0:
            if (moves[m][1]==1 and next_pos not in data['boxes']) or (moves[m][1]==-1 and (next_pos[0], next_pos[1]-1) not in data['boxes']):
                data['robot'] = next_pos
            else:
                should_move, to_remove, to_add = check_box_2_h(data, next_pos, moves[m][1])
                if should_move:
                    for p in to_remove:
                        data['boxes'].remove(p)
                    data['boxes'] += to_add
                    data['robot'] = next_pos
        else:
            if (next_pos not in data['boxes']) and ((next_pos[0], next_pos[1]-1) not in data['boxes']):
                data['robot'] = next_pos
            else:
                should_move, positions, pos_to_remove = check_box_2_v(data, next_pos, moves[m][0])
                if should_move:
                    data['boxes'] += [pos for pos in positions if pos!=next_pos and pos not in data['boxes']]
                    for pos in pos_to_remove:
                        data['boxes'].remove(pos)
                    data['robot'] = next_pos
    return sum([100*pos[0]+pos[1] for pos in data['boxes']])

if __name__ == "__main__":
    start = pfc()
    day = "15"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
