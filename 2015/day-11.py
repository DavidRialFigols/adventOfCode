from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read()
    return data

def requirement_1(pwd):
    prev_num, counter = pwd[0], 1
    for n in pwd[1:]:
        if n-1 == prev_num:
            counter += 1
            if counter == 3:
                return True
        else:
            counter = 1
        prev_num = n
    return False

def requirement_2(pwd):
    # 'i' is 9
    # 'o' is 15
    # 'l' is 12
    return (9 not in pwd) and (15 not in pwd) and (12 not in pwd)

def requirement_3(pwd):
    pairs = {}
    for i in range(0,len(pwd)-1):
        if pwd[i]==pwd[i+1]:
            if pwd[i] not in pairs:
                pairs[pwd[i]] = [i, 1]
                if sum([pairs[i][1] for i in pairs]) >= 2:
                    return True
            elif pairs[pwd[i]][0]-i > 1:
                pairs[pwd[i]] = [i, pairs[pwd[i]][1]+1]
    return sum([pairs[i][1] for i in pairs]) >= 2

def increase_pwd(pwd):
    for i in range(len(pwd)-1, 0, -1):
        if pwd[i] < 26:
            pwd[i] = pwd[i]+1
            break
        else:
            pwd[i] = 1
    return pwd

def find_next_pwd(pwd):
    while not(requirement_1(pwd)) or not (requirement_2(pwd)) or not (requirement_3(pwd)):
        if not requirement_2(pwd):
            for i in range(len(pwd)):
                if pwd[i] in [9, 12, 15]: #as they are the numbers of the characters i, o and l
                    pwd[i] = pwd[i]+1
                    for j in range(i+1, len(pwd)):
                        pwd[j] = 1
                    break
        else:
            pwd = increase_pwd(pwd)
    return pwd

def process_data_1(data):
    pwd = [ord(char) - 96 for char in data.lower()]
    pwd = find_next_pwd(pwd)
    pwd = ''.join([chr(num+96) for num in pwd])
    return pwd

def process_data_2(data):
    pwd = [ord(char) - 96 for char in data.lower()]
    pwd = find_next_pwd(pwd)
    pwd = increase_pwd(pwd)
    pwd = find_next_pwd(pwd)
    pwd = ''.join([chr(num+96) for num in pwd])
    return pwd

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
