from time import perf_counter as pfc
import copy
import hashlib

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip()
    return data

def process_data_1(data):
    i = 0
    found = False
    while not found:
        i += 1
        key = hashlib.md5(f"{data}{i}".encode()).hexdigest()
        found = key[:5]=='00000'
    return i

def process_data_2(data):
    i = 0
    found = False
    while not found:
        i += 1
        key = hashlib.md5(f"{data}{i}".encode()).hexdigest()
        found = key[:6]=='000000'
    return i

if __name__ == "__main__":
    start = pfc()
    day = "04"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
