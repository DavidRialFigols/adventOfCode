from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [i.split(',') for i in fin.read().rstrip().split("\n")]
        for i in range(len(data)):
            data[i][0] = [int(j) for j in data[i][0].split('-')]
            data[i][1] = [int(j) for j in data[i][1].split('-')]
    return data

def process_data_1(data):
    condition = lambda x,y: x[0]<=y[0] and y[1]<=x[1] # so, xmin <= ymin < ymax <= xmax
    return sum([condition(i[0],i[1]) or condition(i[1],i[0]) for i in data])

def process_data_2(data):
    condition = lambda x,y: (x[0]<=y[0] and y[0]<=x[1]) or (x[0]<=y[1] and y[1]<=x[1]) # so, xmin <= ymin <= xmax or xmin <= ymax <= xmax
    return sum([condition(i[0],i[1]) or condition(i[1],i[0]) for i in data])

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
