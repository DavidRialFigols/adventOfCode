from time import perf_counter as pfc
import copy
import heapq

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [[int(j) for j in i.split('\n')] for i in fin.read().rstrip().split('\n\n')]
    return data

def process_data_1(data):
    return max([sum(i) for i in data])

def process_data_2(data):
    return sum(heapq.nlargest(3, ([sum(i) for i in data])))

if __name__ == "__main__":
    start = pfc()
    day = "01"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
