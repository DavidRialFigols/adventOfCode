from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split("\n")
    return data

def find_init_pos(data):
    for i in range(len(data)):
        if '^' in data[i]:
            for j in range(len(data[i])):
                if data[i][j] == '^':
                    return (i,j), 0
                elif data[i][j] == '>':
                    return (i,j), 1
                elif data[i][j] == 'v':
                    return (i,j), 2
                elif data[i][j] == '<':
                    return (i,j), 3
    return -1

def process_data_1(data):
    moves = {
        0: (-1,0),
        1: (0,1),
        2: (1,0),
        3: (0,-1)
    }
    act_pos, dir = find_init_pos(data)
    positions = []
    while True:
        positions.append(act_pos)
        next_pos = (act_pos[0]+moves[dir][0], act_pos[1]+moves[dir][1])
        if next_pos[0] < 0 or next_pos[0]>=len(data) or next_pos[1] < 0 or next_pos[1]>=len(data[0]):
            break
        if data[next_pos[0]][next_pos[1]]=='#':
            dir = (dir+1)%4
        else:
            act_pos = next_pos
    return len(list(set(positions)))

def test_obstruction(moves, walls, new_wall, num_rows, num_cols, act_pos, dir):
    visited_states = set()
    while True:
        next_pos = (act_pos[0]+moves[dir][0], act_pos[1]+moves[dir][1])

        if next_pos[0] < 0 or next_pos[0]>=num_rows or next_pos[1] < 0 or next_pos[1]>=num_cols:
            return False
                
        if (next_pos[0],next_pos[1]) in walls or (next_pos[0],next_pos[1]) == new_wall:
            dir = (dir+1)%4
        else:
            if (next_pos, dir) in visited_states:
                return True
            act_pos = next_pos
        
        visited_states.add((act_pos, dir))

def process_data_2(data):
    moves = {
        0: (-1,0),
        1: (0,1),
        2: (1,0),
        3: (0,-1)
    }
    visited_pos = []
    act_pos, dir = find_init_pos(data)
    walls = set()
    num_rows, num_cols = len(data), len(data[0])
    for x in range(num_rows):
        for y in range(num_cols):
            if data[x][y]=='#':
                walls.add((x,y))
    while True:
        visited_pos.append(act_pos)
        next_pos = (act_pos[0]+moves[dir][0], act_pos[1]+moves[dir][1])
        if next_pos[0] < 0 or next_pos[0]>=num_rows or next_pos[1] < 0 or next_pos[1]>=num_cols:
            break
        if (next_pos[0],next_pos[1]) in walls:
            dir = (dir+1)%4
        else:
            act_pos = next_pos

    visited_pos = list(set(visited_pos))

    loops_found = 0
    act_pos, dir = find_init_pos(data)
    for x,y in visited_pos[1:]:
        if test_obstruction(moves, walls, (x,y), num_rows, num_cols, act_pos, dir):
            loops_found += 1
    return loops_found

if __name__ == "__main__":
    start = pfc()
    day = "06"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
