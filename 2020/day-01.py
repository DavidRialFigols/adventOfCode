from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [int(i) for i in fin.read().rstrip().split("\n")]
    return data

def process_data_1(data):
    data.sort()
    for i, num1 in enumerate(data):
        if i+1 < len(data):
            for num2 in data[i+1:]:
                if num1+num2==2020:
                    return num1*num2

                if num1+num2 > 2020:
                    break

    return "Not Found"

def process_data_2(data):
    data.sort()
    for i, num1 in enumerate(data):
        if i+1 < len(data):
            for j, num2 in enumerate(data[i+1:]):
                if num1+num2 > 2020:
                    break
                for num3 in data[i+j+1:]:
                    if num1+num2+num3==2020:
                        return num1*num2*num3
                    if num1+num2+num3>2020:
                        break
    return "Not Found"

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
