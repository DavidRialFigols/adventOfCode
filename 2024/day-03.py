from time import perf_counter as pfc
import copy
import re

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip()
    return data

def process_data_1(data):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = [i[4:-1].split(',') for i in re.findall(pattern, data)]
    return sum([int(i[0])*int(i[1]) for i in matches])

def process_data_2(data):
    dodonts = r"(do\(\)|don't\(\))"
    matches = re.split(dodonts, data)
    take = True
    intoaccount = []
    for i in matches:
        if i=="don't()":
            take = False
        elif i == "do()":
            take = True
        else:
            if take:
                intoaccount.append(i)
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = [i[4:-1].split(',') for i in re.findall(pattern, ''.join(intoaccount))]
    return sum([int(i[0])*int(i[1]) for i in matches])

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
