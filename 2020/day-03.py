from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split("\n")
    return data

def process_data_1(data):
    x,y = 0,0
    trees = 0
    while y < len(data):
        trees += data[y][x] == '#' 
        y += 1
        x = (x+3)%len(data[0])
    return trees

def process_data_2(data):
    slopes = [
        {'slope': (1,1), 'position': [0,0], 'trees': 0},
        {'slope': (3,1), 'position': [0,0], 'trees': 0},
        {'slope': (5,1), 'position': [0,0], 'trees': 0},
        {'slope': (7,1), 'position': [0,0], 'trees': 0},
        {'slope': (1,2), 'position': [0,0], 'trees': 0},
        ]
    stop = False
    while not stop:
        stop = True
        for slope in slopes:
            p = slope['position']
            if p[1] < len(data):
                stop = False
                slope['trees'] += data[p[1]][p[0]] == '#' 
                dx,dy = slope['slope'][0],slope['slope'][1]
                slope['position'] = [(p[0]+dx)%len(data[0]), p[1]+dy]
    mul = 1
    for slope in slopes:
        mul *= slope['trees']
    return mul

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
