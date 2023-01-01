from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [[[int(j[j.index('=')+1:j.index(',')]), int(j[j.rindex('=')+1:])] for j in i.split(': ')] for i in fin.read().rstrip().split("\n")]
    return data

def manhattan_distance(c1, c2):
    return sum([abs(c1[i]-c2[i]) for i in range(len(c1))])

def process_data_1(data):
    line_to_check = 10
    return

def process_data_2(data):
    return

if __name__ == "__main__":
    start = pfc()
    day = "15"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
