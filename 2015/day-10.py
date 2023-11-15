from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = eval(fin.read())
    return data
def look_and_say(num, iterations):
    for i in range(iterations):
        next_num = []
        actual_num, counter = num[0], 1
        for n in num[1:]:
            if n!=actual_num:
                next_num.append(counter)
                next_num.append(actual_num)
                actual_num, counter = n, 1
            else:
                counter +=1
        next_num.append(counter)
        next_num.append(actual_num)
        num = next_num
    return num

def process_data_1(data):
    num = [int(d) for d in str(data)]
    num = look_and_say(num, 40)
    return len(num)

def process_data_2(data):
    num = [int(d) for d in str(data)]
    num = look_and_say(num, 50)
    return len(num)

if __name__ == "__main__":
    start = pfc()
    day = "10"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
