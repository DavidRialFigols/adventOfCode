from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split("\n")
    return data

def process_data_1(data):
    total_value = 0
    for rs in data:
        fh, sh = rs[:int(len(rs)/2)], rs[int(len(rs)/2):]
        common = [i for i in fh if i in sh][0]
        value = ord(common)
        value = value - 96 if value>97 else value-65+27
        total_value+=value
    return total_value

def process_data_2(data):
    total_value = 0
    for line, rs in enumerate(data):
        if line%3==0:
            group = [rs]
            continue

        group.append(rs)
        if line%3==1: continue

        common = [i for i in group[0] if i in group[1] and i in group[2]][0]
        value = ord(common)
        value = value - 96 if value>97 else value-65+27
        total_value+=value
    return total_value

if __name__ == "__main__":
    start = pfc()
    day = "03"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
