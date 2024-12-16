from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [int(i) for i in fin.read().rstrip().split(" ")]
    return data

def apply_rules(num):
    if num==0: return 1
    if len(str(num))%2==0: return [int(str(num)[:int(len(str(num))/2)]), int(str(num)[int(len(str(num))/2):])]
    return num*2024

def blink_p1(data):
    res = []
    for n in data:
        i = apply_rules(n)
        if type(i) == int: res.append(i)
        elif type(i)==list: res += i
    return res

def process_data_1(data):
    for _ in range(25):
        data = blink_p1(data)
    return len(data)

def blink_p2(data):
    res = {}
    for n in data:
        i = apply_rules(n)
        if type(i) == int:
            if i not in res: res[i] = data[n]
            else: res[i] += data[n]
        elif type(i)==list:
            if i[0] not in res: res[i[0]] = data[n]
            else: res[i[0]] += data[n]
            if i[1] not in res: res[i[1]] = data[n]
            else: res[i[1]] += data[n]
    return res

def process_data_2(data):
    data = {n: 1 for n in data}
    for _ in range(75):
        data = blink_p2(data)
    return sum([data[n] for n in data])

if __name__ == "__main__":
    start = pfc()
    day = "11"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
