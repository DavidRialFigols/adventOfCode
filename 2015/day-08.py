from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split("\n")
    return data

def process_data_1(data):
    literals, memory = 0, 0
    for d in data:
        literals += len(d)
        memory += len(eval(d))
    return literals - memory

def process_data_2(data):
    literals, new_literal = 0, 0
    for d in data:
        literals += len(d)
        new_literal += 2 + len(d) + d.count('\\')+d.count('"')
    return new_literal - literals

if __name__ == "__main__":
    start = pfc()
    day = "08"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
