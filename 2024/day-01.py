from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [(int(i.split(' ')[0]), int(i.split(' ')[-1])) for i in fin.read().rstrip().split("\n")]
        data = [[i[0] for i in data], [i[1] for i in data]]
    return data

def process_data_1(data):
    l1, l2 = sorted(data[0]), sorted(data[1])
    return sum([abs(l1[i]-l2[i]) for i in range(len(l1))])

def process_data_2(data):
    l1, l2 = data[0], data[1]
    return sum([n*sum([n==i for i in l2]) for n in l1])

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
