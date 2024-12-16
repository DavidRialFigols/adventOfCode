from itertools import count
from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [list(map(int, i)) for i in fin.read().rstrip().split("\n")]
    return data

def count_trail_p1(data, pos_x, pos_y, value=0):
    if value==9:
        return [(pos_x, pos_y)]
    
    trails_found = []
    if pos_x>0 and data[pos_x-1][pos_y]==value+1: #up
        trails_found += count_trail_p1(data, pos_x-1, pos_y, value+1)
    if pos_y<len(data[0])-1 and data[pos_x][pos_y+1]==value+1: #right
        trails_found += count_trail_p1(data, pos_x, pos_y+1, value+1)
    if pos_x<len(data)-1 and data[pos_x+1][pos_y]==value+1: #down
        trails_found += count_trail_p1(data, pos_x+1, pos_y, value+1)
    if pos_y>0 and data[pos_x][pos_y-1]==value+1: #left
        trails_found += count_trail_p1(data, pos_x, pos_y-1, value+1)
    return list(set(trails_found))

def process_data_1(data):
    return sum([len(count_trail_p1(data, x, y)) for x, row in enumerate(data) for y, num in enumerate(row) if num==0])

def count_trail_p2(data, pos_x, pos_y, value=0):
    if value==9:
        return 1
    
    trails_found = 0
    if pos_x>0 and data[pos_x-1][pos_y]==value+1: #up
        trails_found += count_trail_p2(data, pos_x-1, pos_y, value+1)
    if pos_y<len(data[0])-1 and data[pos_x][pos_y+1]==value+1: #right
        trails_found += count_trail_p2(data, pos_x, pos_y+1, value+1)
    if pos_x<len(data)-1 and data[pos_x+1][pos_y]==value+1: #down
        trails_found += count_trail_p2(data, pos_x+1, pos_y, value+1)
    if pos_y>0 and data[pos_x][pos_y-1]==value+1: #left
        trails_found += count_trail_p2(data, pos_x, pos_y-1, value+1)
    return trails_found

def process_data_2(data):
    return sum([count_trail_p2(data, x, y) for x, row in enumerate(data) for y, num in enumerate(row) if num==0])

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
