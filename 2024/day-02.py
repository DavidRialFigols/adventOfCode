from email.errors import InvalidMultipartContentTransferEncodingDefect
from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [list(map(int, i.split(' '))) for i in fin.read().rstrip().split("\n")]
    return data

def is_safe(nums):
    cond1 = lambda x: len(set(x))==len(x)
    cond2 = lambda x: sorted(x)==x or sorted(x, reverse=True)==x
    cond3 = lambda x: max([abs(x[i-1]-x[i]) for i in range(1, len(x))]) <= 3
    return cond1(nums) and cond2(nums) and cond3(nums)

def process_data_1(data):
    return sum([is_safe(l) for l in data])

def process_data_2(data):
    n_safe = 0
    for l in data:
        if is_safe(l):
            n_safe += 1
        else:
            for i in range(len(l)):
                if is_safe(l[:i]+l[i+1:]):
                    n_safe += 1
                    break
    return n_safe

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
