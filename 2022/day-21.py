from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = {}
        for mk in fin.read().rstrip().split("\n"):
            print (mk)
            if len(mk[6:].split()) == 1:
                data[mk[:4]] = int(mk[6:])
            else:
                data[mk[:4]] = mk[6:].split()
    return data

def calculate_monkey(data, mk):
    if type(data[mk]) is int:
        return data[mk]

    data[mk] = int(eval(f"{calculate_monkey(data, data[mk][0])}{data[mk][1]}{calculate_monkey(data, data[mk][2])}"))
    return data[mk]

def process_data_1(data):
    return calculate_monkey(data, 'root')

def find_humn(data, mk):
    if mk=='humn':
        return True

    if type(data[mk]) is int:
        return False

    if find_humn(data, data[mk][0]):
        return 1
    elif find_humn(data, data[mk][2]):
        return 2

    return False

def calculate_humn(data, mk, acum_value, opposites):
    humn = find_humn(data, mk)
    if humn==1 and mk!='humn':
        new_acum_val = int(eval(f"{acum_value}{opposites[data[mk][1]]}{calculate_monkey(data, data[mk][2])}"))
        return calculate_humn(data, data[mk][0], new_acum_val, opposites)
    elif humn==2 and (data[mk][1]=='*' or data[mk][1]=="+"):
        new_acum_val = int(eval(f"{acum_value}{opposites[data[mk][1]]}{calculate_monkey(data, data[mk][0])}"))
        return calculate_humn(data, data[mk][2], new_acum_val, opposites)
    elif humn==2: # only - and /
        new_acum_val = int(eval(f"{calculate_monkey(data, data[mk][0])}{data[mk][1]}{acum_value}"))
        return calculate_humn(data, data[mk][2], new_acum_val, opposites)
    # only in humn case
    return acum_value



def process_data_2(data):
    opposites = {'+':"-", "-":"+", "*":"/", "/":"*"}

    humn = find_humn(data, 'root')
    if humn==1:
        new_acum_val = calculate_monkey(data, data['root'][2])
        return calculate_humn(data, data['root'][0], new_acum_val, opposites)
    
    new_acum_val = calculate_monkey(data, data['root'][0])
    return calculate_humn(data, data['root'][0], new_acum_val, opposites)
    

if __name__ == "__main__":
    start = pfc()
    day = "21"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
