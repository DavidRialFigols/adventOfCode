from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split("\n")[0]
    return data

def process_data_1(data):
    for i in range(4, len(data)):
        if len(set([ch for ch in data[i-4:i]]))==4: break        
    return i

def process_data_2(data):
    for i in range(14, len(data)):
        if len(set([ch for ch in data[i-14:i]]))==14: break        
    return i

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
