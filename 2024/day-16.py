from time import perf_counter as pfc
import copy

from numpy import tile

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        neighbors = [(1,0),(-1,0),(0,1),(0,-1)]
        aux = fin.read().rstrip().split("\n")
        data = {'direction': 0, 'position': (0,0), 'goal': (0,0), 'road': {}}
        for x, row in enumerate(aux):
            for y, el in enumerate(row):
                if el=='S': data['position'] = (x,y)
                elif el=='E': data['goal'] = (x,y)
                if el in ['.', 'S', 'E']: 
                    data['road'][(x,y)] = [(x+dx,y+dy) for dx,dy in neighbors if aux[x+dx][y+dy] in ['.','S','E']]
    return data

def heuristic(pos, goal):
    return abs(pos[0]-goal[0])+abs(pos[1]-goal[1])

def process_data_1(data):
    directions = { 
        0: ( 0, 1), # east
        1: ( 1, 0), # south
        2: ( 0,-1), # west
        3: (-1, 0) # north
    }
    states = [(0, [data['position']], data['direction'])]
    visited_states = set()
    while states[-1][1][-1] != data['goal']:
        score, route, act_dir = states.pop()
        act_pos = route[-1]
        visited_states.add(act_pos)
        neighbors = data['road'][act_pos]
        for n in neighbors:
            if n in visited_states: continue
            if n in route: continue
            if n == (act_pos[0]+directions[act_dir][0], act_pos[1]+directions[act_dir][1]): #no change in direction
                states.append((score+1, route+[n], act_dir))
            elif n==(act_pos[0]+directions[(act_dir+1)%4][0], act_pos[1]+directions[(act_dir+1)%4][1]): #clockwise
                states.append((score+1001, route+[n], (act_dir+1)%4))
            elif n==(act_pos[0]+directions[(act_dir-1)%4][0], act_pos[1]+directions[(act_dir-1)%4][1]): #counterclockwise
                states.append((score+1001, route+[n], (act_dir-1)%4))
        states = sorted(states, reverse=True)

    return states[-1][0]

def process_data_2(data):
    directions = { 
        0: ( 0, 1), # east
        1: ( 1, 0), # south
        2: ( 0,-1), # west
        3: (-1, 0) # north
    }
    states = [(0, [data['position']], data['direction'])]
    visited_states = {}
    tiles_to_sit = []
    best_score = False
    while len(states)>0:
        score, route, act_dir = states.pop()
        act_pos = route[-1]
        if act_pos == data['goal']:
            if score==best_score:
                tiles_to_sit += route
            if not best_score:
                tiles_to_sit += route
                best_score = score
        
        elif best_score and score >= best_score:
            continue

        visited_states[(act_pos, act_dir)] = score
        neighbors = data['road'][act_pos]
        for n in neighbors:
            if n in route: continue
            if n == (act_pos[0]+directions[act_dir][0], act_pos[1]+directions[act_dir][1]): #no change in direction
                if (n, act_dir) in visited_states and score+1>visited_states[(n, act_dir)]: continue
                states.append((score+1, route+[n], act_dir))
            elif n==(act_pos[0]+directions[(act_dir+1)%4][0], act_pos[1]+directions[(act_dir+1)%4][1]): #clockwise
                if (n,(act_dir+1)%4) in visited_states and score+1001>visited_states[(n,(act_dir+1)%4)]: continue
                states.append((score+1001, route+[n], (act_dir+1)%4))
            elif n==(act_pos[0]+directions[(act_dir-1)%4][0], act_pos[1]+directions[(act_dir-1)%4][1]): #counterclockwise
                if (n,(act_dir-1)%4) in visited_states and score+1001>visited_states[(n,(act_dir-1)%4)]: continue
                states.append((score+1001, route+[n], (act_dir-1)%4))
        states = sorted(states, reverse=True)
    return len(set(tiles_to_sit))

if __name__ == "__main__":
    start = pfc()
    day = "16"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
