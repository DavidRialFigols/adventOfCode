from time import perf_counter as pfc
import copy
from math import floor

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [int(i) for i in fin.read().rstrip().split("\n")]
    return data

def mix(data, aux):
    for i, num in enumerate(data):
        aux.sort(key=lambda x: x[1])
        
        act_pos = aux[i][0]
        next_pos = (act_pos + num)%(len(data)-1)

        aux.sort(key=lambda x: x[0])
        j = act_pos
        aux[act_pos][0] = next_pos
        while j != next_pos:
            if j<next_pos:
                j += 1
                aux[j%len(data)][0] = j-1
                j = j%len(data)
            elif j > next_pos:
                j -= 1
                aux[j%len(data)][0] = j+1
                j = j%len(data)
    aux.sort(key=lambda x: x[0])
    return aux

def process_data_1(data):
    aux = []
    for i, num in enumerate(data):
        aux.append([i, i, num]) # actual_position, initial_pos, num

    aux = mix(data, aux)
    
    for i in aux:
        if i[2] == 0:
            zero_pos = i[0]
    return sum([aux[(1000*(i+1)+zero_pos)%len(data)][2] for i in range(3)])

def process_data_2(data):
    aux = []

    key = 811589153
    for i in range(len(data)):
        data[i] *= key

    for i, num in enumerate(data):
        aux.append([i, i, num]) # actual_position, initial_pos, num

    for k in range(10):
        aux = mix(data, aux)

    for i in aux:
        if i[2] == 0:
            zero_pos = i[0]
    return sum([aux[(1000*(i+1)+zero_pos)%len(data)][2] for i in range(3)])

if __name__ == "__main__":
    start = pfc()
    day = "20"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
