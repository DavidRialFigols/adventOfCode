from time import perf_counter as pfc
import copy
import numpy as np

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [[int(j) for j in i.split('x')] for i in fin.read().rstrip().split("\n")]
    return data

def process_data_1(data):
    total = 0
    for present in data:
        sides = [present[0]*present[1], present[0]*present[2], present[1]*present[2]]
        total += 2*(sum(sides))+min(sides)
    return total

def process_data_2(data):
    total = 0
    for present in data:
        total += 2*(sum(present)-max(present))
        total += np.prod(present)
    return total

if __name__ == "__main__":
    start = pfc()
    day = "02"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
