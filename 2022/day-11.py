from time import perf_counter as pfc
import math
from collections import defaultdict
import numpy as np
import copy

def obtain_operation(text):
    # delete the introduction
    text = text[text.index(':')+2:].split()[2:]
    # obtain the possible operations
    if text[1]=='*':
        if text[2]=='old':
            operation = lambda x: x*x
        else:
            operation = lambda x: x*int(text[2])
    elif text[1] == '+':
        if text[2]=='old':
            operation = lambda x: x+x
        else:
            operation = lambda x: x+int(text[2])
    else: # raise an Exception if the operation is different from the possible ones
        raise Exception('The operation could not be obtained!')
    return operation

def obtain_test(test, positive_result, negative_result):
    test_op = lambda x: x%(int(test.split()[-1]))==0
    test_div = int(test.split()[-1])
    positive_result = int(positive_result.split()[-1])
    negative_result = int(negative_result.split()[-1])

    return [test_op, positive_result, negative_result, test_div]

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        aux = [i.split('\n') for i in fin.read().rstrip().split("\n\n")]
        data = []
        for i, m in enumerate(aux):
            new_m = {}
            m = [j.lstrip() for j in m[1:]]
            new_m['items'] = [int(j) for j in m[0].replace(',','').split()[2:]]
            new_m['operation'] = obtain_operation(m[1])
            new_m['test'] = obtain_test(m[2], m[3], m[4])
            data.append(new_m)
    return data

def process_data_1(data):
    num_rounds = 20
    items_inspected = defaultdict(int)
    for r in range(num_rounds):
        for num_m, m in enumerate(data):
            # print(f'STARTING MONKEY {num_m}')
            for item in m['items']:
                # inspect item
                # print(f'--Inspecting item {item}')
                wl = m['operation'](item) # Worry Level
                items_inspected[num_m] += 1
                # print(f'--New worry level: {wl}')
                # relief
                wl = math.floor(wl/3)
                # print(f'--After relief: {wl}')

                # test worry level
                num_next_m = m['test'][1] if m['test'][0](wl) else m['test'][2]
                # print(f'--Throwing item to: {num_next_m}')

                # throw to monkey
                data[num_next_m]['items'].append(wl)

            # delete all items of the monkey
            data[num_m]['items'] = []
            # print()
    items_inspected = sorted(list(items_inspected.values()), reverse=True)
    return np.prod(items_inspected[:2])

def obtain_lcm(nums):
    lcm = 1
    for i in nums:
        lcm = lcm*i//math.gcd(lcm, i)
    return lcm

def process_data_2(data):
    num_rounds = 10000
    lcm = obtain_lcm([i['test'][3] for i in data])
    items_inspected = defaultdict(int)
    for r in range(num_rounds):
        for num_m, m in enumerate(data):
            # print(f'STARTING MONKEY {num_m}')
            for item in m['items']:
                # inspect item
                # print(f'--Inspecting item {item}')
                wl = m['operation'](item) # Worry Level
                items_inspected[num_m] += 1
                # print(f'--New worry level: {wl}')
                
                # reduce the wl
                wl = wl%lcm

                # test worry level
                num_next_m = m['test'][1] if m['test'][0](wl) else m['test'][2]
                # print(f'--Throwing item to: {num_next_m}')

                # throw to monkey
                data[num_next_m]['items'].append(wl)

            # delete all items of the monkey
            data[num_m]['items'] = []
            # print()

    items_inspected = sorted(list(items_inspected.values()), reverse=True)
    return np.prod(items_inspected[:2])

if __name__ == "__main__":
    start = pfc()
    day = "11"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
