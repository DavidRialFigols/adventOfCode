from operator import ne
from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [[int(op.split(': ')[0]), list(map(int, op.split(' ')[1:]))] for op in fin.read().rstrip().split("\n")]
    return data

def calculate_1(result, numbers_left, actual=False):
    if actual and actual > result: 
        return False
    next_num = numbers_left[0]
    numbers_left = numbers_left[1:]

    with_mul = actual*next_num if actual else next_num
    with_sum = actual+next_num if actual else next_num

    if len(numbers_left)==0:
        return (with_mul==result or with_sum==result)
    
    if calculate_1(result, numbers_left.copy(), with_sum):
        return True
    else:
        return calculate_1(result, numbers_left.copy(), with_mul)

def process_data_1(data):
    return sum([el[0] for el in data if calculate_1(el[0], el[1])])

def calculate_2(result, numbers_left, actual=False):
    if actual and actual > result: 
        return False
    
    next_num = numbers_left[0]
    numbers_left = numbers_left[1:]

    with_mul = actual*next_num if actual else next_num
    with_sum = actual+next_num if actual else next_num
    with_con = int(str(actual)+str(next_num)) if actual else next_num

    if len(numbers_left)==0:
        return (with_mul==result or with_sum==result or with_con==result)
    
    if calculate_2(result, numbers_left.copy(), with_sum):
        return True
    elif calculate_2(result, numbers_left.copy(), with_mul):
        return True
    else:
        return calculate_2(result, numbers_left.copy(), with_con)

def process_data_2(data):
    return sum([el[0] for el in data if calculate_2(el[0], el[1])])

#2299902366948 too low
#2299996597595 idk
#2299996597595

if __name__ == "__main__":
    start = pfc()
    day = "07"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
