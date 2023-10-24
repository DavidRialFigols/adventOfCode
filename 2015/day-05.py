from time import perf_counter as pfc
from collections import defaultdict
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split("\n")
    return data

def requirement_1(word):
    return sum([i in 'aeiou' for i in word])>=3

def requirement_2(word):
    return any([word[i]==word[i+1] for i in range(0,len(word)-1)])

def requirement_3(word):
    denied_strings = ['ab', 'cd', 'pq', 'xy']
    return all([i not in word for i in denied_strings])

def requirement_4(word):
    pairs = {}
    for i in range(0,len(word)-1):
        if (word[i], word[i+1]) not in pairs:
            pairs[(word[i], word[i+1])] = i
        else:
            if abs(pairs[(word[i], word[i+1])]-i)>1:
                return True
    return False

def requirement_5(word):
    return any([word[i]==word[i+2] for i in range(0,len(word)-2)])

def process_data_1(data):
    total = 0
    for word in data:
        total += requirement_3(word) and requirement_2(word) and requirement_1(word)
    return total

def process_data_2(data):
    total = 0
    for word in data:
        total += requirement_5(word) and requirement_4(word)
    return total

if __name__ == "__main__":
    start = pfc()
    day = "05"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
