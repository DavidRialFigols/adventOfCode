from time import perf_counter as pfc
import copy
from typing import MutableMapping

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        aux = [i.split(' ') for i in fin.read().rstrip().split("\n")]
        data = []
        for i in aux:
            if len(i)==5:
                data.append((f"{i[0]} {i[1]}", [int(j) for j in i[2].split(',')], [int(j) for j in i[4].split(',')]))
            else:
                data.append((i[0], [int(j) for j in i[1].split(',')], [int(j) for j in i[3].split(',')]))
    return data

def process_data_1(data):
    blocks = [0b0 for j in range(1000)]
    for action in data:
        if action[0] == 'turn on':
            to_on = int(''.join(['1' if i>=action[1][1] and i<=action[2][1] else '0' for i in range(1000)]), 2)
            for i in range(action[1][0], action[2][0]+1):
                blocks[i] |= to_on 
        elif action[0] == 'turn off':
            to_off = int(''.join(['0' if i>=action[1][1] and i<=action[2][1] else '1' for i in range(1000)]), 2)
            for i in range(action[1][0], action[2][0]+1):
                blocks[i] &= to_off

        elif action[0] == 'toggle':
            to_toggle = int(''.join(['1' if i>=action[1][1] and i<=action[2][1] else '0' for i in range(1000)]), 2)
            for i in range(action[1][0], action[2][0]+1):
                blocks[i] ^= to_toggle
    total = 0
    for line in blocks:
        total += str(bin(line)).count('1')
    return total

def process_data_2(data):
    blocks = [[0 for i in range(1000)] for j in range(1000)]
    for action in data:
        if action[0] == 'turn on':
            for i in range(action[1][0], action[2][0]+1):
                for j in range(action[1][1], action[2][1]+1):
                    blocks[i][j]+=1  
        elif action[0] == 'turn off':
            for i in range(action[1][0], action[2][0]+1):
                for j in range(action[1][1], action[2][1]+1):
                    blocks[i][j] = max(0, blocks[i][j]-1)  

        elif action[0] == 'toggle':
            for i in range(action[1][0], action[2][0]+1):
                for j in range(action[1][1], action[2][1]+1):
                    blocks[i][j]+=2  
    return sum([sum(i) for i in blocks])

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
