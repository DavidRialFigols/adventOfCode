from time import perf_counter as pfc
import copy
import math

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [[[int(i[2:]) for i in machine.split('\n')[0].split(': ')[1].split(', ')],[int(i[2:]) for i in machine.split('\n')[1].split(': ')[1].split(', ')],[int(i[2:]) for i in machine.split('\n')[2].split(': ')[1].split(', ')]] for machine in fin.read().rstrip().split("\n\n")]
    return data

def process_data_1(data):
    tokens = []
    for machine in data:
        a, b, prize = machine[0], machine[1], machine[2]
        min_tokens, max_tokens = 100*3+101, 100*3+101 #maximum num of tokens
        for num_a in range(100):
            for num_b in range(100):
                if num_a*3+num_b > min_tokens: break # just to cut some time, we already have a better solution
                if num_a*a[0]+num_b*b[0] > prize[0]: break # as we have surpassed the X coordinate
                if num_a*a[1]+num_b*b[1] > prize[1]: break # as we have surpassed the Y coordinate
                if num_a*a[0]+num_b*b[0] < prize[0]: continue # as we have not reached the X coordinate
                if num_a*a[1]+num_b*b[1] < prize[1]: continue # as we have not reached the Y coordinate

                min_tokens = min(num_a*3+num_b*1, min_tokens)
        if min_tokens < max_tokens:
            tokens.append(min_tokens)
    return sum(tokens)

def process_data_2(data):
    tokens = []
    for machine in data:
        a, b, prize = machine[0], machine[1], [machine[2][0]+10000000000000, machine[2][1]+10000000000000]
        
        numerador_num_b = a[0]*prize[1]-prize[0]*a[1]
        denominador_num_b = a[0]*b[1]-b[0]*a[1]
        if numerador_num_b%denominador_num_b!=0:
            continue #as it will not have an integer solution
        num_b = numerador_num_b//denominador_num_b
        if (prize[0]-num_b*b[0]) % a[0] != 0:
            continue # as it will not have an integer solution
        num_a = (prize[0]-num_b*b[0])//a[0]
        
        tokens.append(num_a*3+num_b)
    return sum(tokens)

if __name__ == "__main__":
    start = pfc()
    day = "13"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
