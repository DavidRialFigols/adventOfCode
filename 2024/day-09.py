from time import perf_counter as pfc
import copy

from numpy import empty

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split("\n")[0]
    return data

def process_data_1(data):
    empty_spaces = [] 
    ids = [] # list of lists with [id, amount] . The amount will be decreasing from the end as we keep moving them with empty spaces
    result = []

    for pos, num in enumerate(data):
        if pos%2==0:
            ids.append([int(pos/2), int(num)])
        else:
            empty_spaces.append(int(num))

    i = 0
    while i < len(ids):
        result += [ids[i][0] for _ in range(ids[i][1])]
        if i != len(ids)-1:
            for _ in range(empty_spaces[0]):
                result.append(ids[-1][0])
                ids[-1][1] -= 1
                if ids[-1][1] == 0:
                    ids = ids[:len(ids)-1]
                    if i == len(ids)-1: break
            
            empty_spaces = empty_spaces[1:] if len(empty_spaces)>0 else empty_spaces
        i += 1

    return sum([pos*num for pos,num in enumerate(result)])

def process_data_2(data):
    ids = [] # list of lists with [type, id, amount] . The amount will be decreasing from the end as we keep moving them with empty spaces
    result = []

    for pos, num in enumerate(data):
        if pos%2==0:
            ids.append([1, int(pos/2), int(num)])
        else:
            ids.append([0, 0, int(num)])

    i = len(ids)-1
    while i > 0:
        if ids[i][0] == 1: # only take it into account if it is not a space block
            for pos in range(i):
                if ids[pos][0] == 1: continue #it is not a space block

                if ids[i][2] < ids[pos][2]:
                    ids = ids[:pos]+[ids[i]]+[[0, 0, ids[pos][2]-ids[i][2]]] + ids[pos+1:i] + [[0,0,ids[i][2]]] + ids[i+1:] #move ids[i] to the middle
                    break
                elif ids[i][2] == ids[pos][2]:
                    ids[i], ids[pos] = ids[pos], ids[i] #we do not need to merge empty spaces if moved backwards
                    break # as we have been able to relocate the last item
                
        i -= 1

    result = [i[1] for i in ids for _ in range(i[2])]
    return sum([pos*num for pos,num in enumerate(result)])

if __name__ == "__main__":
    start = pfc()
    day = "09"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
