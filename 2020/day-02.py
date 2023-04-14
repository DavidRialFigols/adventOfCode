from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [i.split(': ') for i in fin.read().rstrip().split("\n")]
        for i in range(len(data)):
            min_policy, max_policy = int(data[i][0].split('-')[0]), int(data[i][0].split('-')[1].split(' ')[0])
            letter = data[i][0].split(' ')[1]
            data[i][0] = [(min_policy, max_policy), letter]
    return data

def process_data_1(data):
    return sum([p[0][0][0] <= p[1].count(p[0][1]) <= p[0][0][1] for p in data])

def process_data_2(data):
    condition1 = sum([(p[0][0][0] <= len(p[1]) and p[1][p[0][0][0]-1] == p[0][1]) or (p[0][0][1] <= len(p[1]) and p[1][p[0][0][1]-1] == p[0][1]) for p in data])
    condition2 = sum([(p[0][0][1] <= len(p[1]) and p[1][p[0][0][0]-1]==p[1][p[0][0][1]-1]==p[0][1] ) for p in data])
    return condition1-condition2

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
