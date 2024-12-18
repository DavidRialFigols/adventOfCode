from time import perf_counter as pfc
import copy
import math

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [[eval(robot.split(' ')[0][2:]), eval(robot.split(' ')[1][2:])] for robot in fin.read().rstrip().split("\n")]
    return data

def process_data_1(data):
    seconds = 100
    height, width = 103, 101
    if height%2 == 0: mid_y = (height)/2
    else:             mid_y = (height-1)/2

    if width%2 == 0: mid_x = (width)/2
    else:            mid_x = (width-1)/2

    quadrants = [0,0,0,0]
    for robot in data:
        robot[0] = ((robot[0][0]+seconds*robot[1][0])%width, (robot[0][1]+seconds*robot[1][1])%height)
        if robot[0][0] < mid_x and robot[0][1] < mid_y: quadrants[0] += 1
        elif robot[0][0] < mid_x and robot[0][1] > mid_y: quadrants[1] += 1
        elif robot[0][0] > mid_x and robot[0][1] < mid_y: quadrants[2] += 1
        elif robot[0][0] > mid_x and robot[0][1] > mid_y: quadrants[3] += 1 

    return math.prod(quadrants)

def move_robot(data):
    height, width = 103, 101
    for robot in data:
        robot[0] = ((robot[0][0]+robot[1][0])%width, (robot[0][1]+robot[1][1])%height)
    return data

def check_tree(data):
    next_set = set()
    matching = set()
    
    for r in data:
        if r[0] in next_set:
            matching.add(r[0])
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                next_set.add((r[0][0]+dx, r[0][1]+dy))
    return len(matching) > 250

def process_data_2(data):
    height, width = 103, 101
    i = 0
    while len(input("Continue? (empty enter to continue)"))==0:
        data = move_robot(data)
        i+=1
        while not check_tree(data):
            data = move_robot(data)
            i+=1
        for x in range(height):
            line = ''
            for y in range(width):
                line += '.' if (y,x) not in [r[0] for r in data] else 'R'
            print(line)
    return i

if __name__ == "__main__":
    start = pfc()
    day = "14"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
