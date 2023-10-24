from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip()
    return data

def process_data_1(data):
    visited_houses = [(0,0)]
    x,y=0,0
    for move in data:
        if move=='>': y+=1
        elif move=='<': y-=1
        elif move=='^': x+=1
        elif move=='v': x-=1

        visited_houses.append((x,y))        
    return len(set(visited_houses))

def process_data_2(data):
    visited_houses = [(0,0)]
    santa_pos =[0,0]
    robot_pos=[0,0]
    santa = True
    for move in data:
        if santa: pos = santa_pos
        else: pos = robot_pos
        
        if move=='>': pos[1]+=1
        elif move=='<': pos[1]-=1
        elif move=='^': pos[0]+=1
        elif move=='v': pos[0]-=1

        santa = not santa

        visited_houses.append((pos[0],pos[1]))        
    return len(set(visited_houses))

if __name__ == "__main__":
    start = pfc()
    day = "03"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
