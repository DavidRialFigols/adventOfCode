from time import perf_counter as pfc
import copy

def read_file(day):
    plays = {'A': 0, 'B': 1, 'C': 2,
            'X': 0, 'Y': 1, 'Z': 2}
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split("\n")
        aux = []
        for play in data:
            aux.append((plays[play[0]], plays[play[2]]))
        data = aux
    return data

def process_data_1(data):
    score = 0
    for play in data:
        score += play[1]+1 #because the range of the scores is from 1 to 3 and not from 0 to 2
        if play[0]==play[1]: score+=3
        elif (play[0]+1)%3 == play[1]: score+=6

    return score

def process_data_2(data):
    score = 0
    for play in data:
        if play[1] == 0:
            score += (play[0]+2)%3 +1
        elif play[1] == 1:
            score += 3 + (play[0])%3 +1
        else:
            score += 6 + (play[0]+1)%3 +1

    return score

if __name__ == "__main__":
    start = pfc()
    day = "02"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
