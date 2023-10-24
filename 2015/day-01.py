from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip()
    return data

def process_data_1(data):
    return data.count('(') - data.count(')')

def process_data_2(data):
    floor = 0
    character = 0
    while floor!=-1 and character < len(data):
        if data[character] == '(': floor+=1
        else: floor -=1
        character += 1
    return character if character<len(data) else None

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
