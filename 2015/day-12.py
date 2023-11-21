from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = eval(fin.read())
    return data

def sum_dict_1(item):
    counter = 0
    for k in item:
        el = item[k]
        if type(el) == int:
            counter += el
        elif type(el) == list:
            counter += sum_list_1(el)
        elif type(el) == dict:
            counter += sum_dict_1(el)
    return counter

def sum_list_1(item):
    counter = 0
    for i in item:
        if type(i) == int:
            counter += i
        elif type(i) == list:
            counter += sum_list_1(i)
        elif type(i) == dict:
            counter += sum_dict_1(i)
    return counter

def sum_dict_2(item):
    counter = 0
    for k in item:
        el = item[k]
        if type(el) == int:
            counter += el
        elif type(el) == list:
            counter += sum_list_2(el)
        elif type(el) == dict:
            counter += sum_dict_2(el)
        elif el=="red":
            counter=0
            break
    return counter

def sum_list_2(item):
    counter = 0
    for i in item:
        if type(i) == int:
            counter += i
        elif type(i) == list:
            counter += sum_list_2(i)
        elif type(i) == dict:
            counter += sum_dict_2(i)
    return counter

def process_data_1(data):
    counter = 0
    for i in data:
        if type(i) == int:
            counter += i
        elif type(i) == list:
            counter += sum_list_1(i)
        elif type(i) == dict:
            counter += sum_dict_1(i)
    return counter

def process_data_2(data):
    counter = 0
    for i in data:
        if type(i) == int:
            counter += i
        elif type(i) == list:
            counter += sum_list_2(i)
        elif type(i) == dict:
            counter += sum_dict_2(i)
    return counter

if __name__ == "__main__":
    start = pfc()
    day = "12"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
