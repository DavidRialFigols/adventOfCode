from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [eval(i) for i in fin.read().rstrip().split("\n")]
    return data

def heuristic(pos, goal):
    return abs(pos[0]-goal[0])+abs(pos[1]-goal[1])

def process_data_1(data):
    max_size=70
    num_bytes=1024
    corrupted = data[:num_bytes]
    pos, goal = (0,0), (max_size, max_size)
    paths = [(pos, heuristic(pos, goal), 0)]
    visited = set()
    neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
    while len(paths)>0:
        current_state = paths.pop()
        pos, h, s = current_state[0], current_state[1], current_state[2]
        if pos == goal:
            break
        if pos in visited:
            continue
        visited.add(pos)
        for n in neighbors:
            np = (pos[0]+n[0], pos[1]+n[1])
            if np[0] < 0 or np[0]>max_size or np[1]<0 or np[1]>max_size: continue # np is out of the memory space
            if np in corrupted: continue
            nh = heuristic(np, goal)
            ns = s+1
            paths.append((np, nh, ns))
        paths = sorted(paths, key=lambda x: (x[2], x[1]), reverse=True)
    return current_state[2]

def process_data_2(data):
    max_size=70
    num_bytes=1024
    corrupted = data[:num_bytes]
    init_pos, goal = (0,0), (max_size, max_size)
    route_exists = True
    while route_exists:
        paths = [(init_pos, heuristic(init_pos, goal), 0, [init_pos])]
        visited = set()
        neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
        while len(paths)>0:
            current_state = paths.pop()
            pos, h, s, route = current_state[0], current_state[1], current_state[2], current_state[3]
            if pos == goal:
                break
            if pos in visited: continue
            visited.add(pos)
            for n in neighbors:
                np = (pos[0]+n[0], pos[1]+n[1])
                if np[0] < 0 or np[0]>max_size or np[1]<0 or np[1]>max_size: continue # np is out of the memory space
                if np in corrupted: continue
                nh = heuristic(np, goal)
                ns = s+1
                paths.append((np, nh, ns, route+[np]))
            paths = sorted(paths, key=lambda x: (x[2], x[1]), reverse=True)
        if pos == goal:
            next_corrupted = data[num_bytes]
            while next_corrupted not in route:
                num_bytes += 1
                next_corrupted = data[num_bytes]
            corrupted = data[:num_bytes+1]
        route_exists = pos==goal
    return data[num_bytes]

if __name__ == "__main__":
    start = pfc()
    day = "18"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
