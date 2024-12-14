from time import perf_counter as pfc
import copy
from turtle import update

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        aux = [i.split('\n') for i in fin.read().rstrip().split("\n\n")]
        data = {'rules': [(int(rule.split('|')[0]), int(rule.split('|')[1])) for rule in aux[0]], 'updates': [[int(n) for n in i.split(',')] for i in aux[1]]}
    return data

def validate_update(update, rules):
    for i, n in enumerate(update):
        previous_nums = [r[0] for r in rules if r[1]==n]
        next_nums = [r[1] for r in rules if r[0]==n] 
        if any([m in next_nums for m in update[:i]]) or any([m in previous_nums for m in update[i+1:]]):
            return False
    return True

def process_data_1(data):
    nums = 0
    for up in data['updates']:
        if validate_update(up, data['rules']):
            nums += up[int(len(up)/2)]
    return nums

def order_update(update, rules):
    while not validate_update(update, rules):
        for i, n in enumerate(update):
            changed = False
            previous_nums = [r[0] for r in rules if r[1]==n]
            for j, m in enumerate(update[i+1:]):
                if m in previous_nums:
                    update[i], update[i+j+1] = m, n
                    changed = True
                    break
            if not changed:
                next_nums = [r[1] for r in rules if r[0]==n]
                for j, m in enumerate(update[:i]):
                    if m in next_nums:
                        update[i], update[j] = m, n
                        break
    return update


def process_data_2(data):
    nums = 0
    for k, up in enumerate(data['updates']):
        if not validate_update(up, data['rules']):
            ordered_up = order_update(up, data['rules'])
            nums += ordered_up[int(len(ordered_up)/2)]
    return nums

if __name__ == "__main__":
    start = pfc()
    day = "05"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
