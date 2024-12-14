from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split("\n")
    return data

def process_data_1(data):
    orientations = [
        ((-1,-1),(-2,-2),(-3,-3)), # up-left
        ((-1,0),(-2,0),(-3,0)), # up
        ((-1,1),(-2,2),(-3,3)), # up-right
        ((0,1),(0,2),(0,3)), # right
        ((1,1),(2,2),(3,3)), # down-right
        ((1,0),(2,0),(3,0)), # down
        ((1,-1),(2,-2),(3,-3)), # down-left
        ((0,-1),(0,-2),(0,-3)) # left
    ]
    found = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'X':
                for ori in orientations:
                    try:
                        if i+ori[0][0] < 0 or j+ori[0][1] < 0 or i+ori[1][0] < 0 or j+ori[1][1] < 0 or i+ori[2][0] < 0 or j+ori[2][1] < 0:
                            continue
                        l1 = data[i+ori[0][0]][j+ori[0][1]]
                        l2 = data[i+ori[1][0]][j+ori[1][1]]
                        l3 = data[i+ori[2][0]][j+ori[2][1]]
                        if l1+l2+l3=='MAS':
                            found +=1
                    except:
                        continue
         
    return found

def process_data_2(data):
    orientations = [
        ((-1,-1),(-1,1),(1,1),(1,-1)),
        ((1,-1),(-1,-1),(-1,1),(1,1)),
        ((1,1),(1,-1),(-1,-1),(-1,1)),
        ((-1,1),(1,1),(1,-1),(-1,-1))
    ]
    found = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'A':
                for ori in orientations:
                    try:
                        if i+ori[0][0] < 0 or j+ori[0][1] < 0 or i+ori[1][0] < 0 or j+ori[1][1] < 0 or i+ori[2][0] < 0 or j+ori[2][1] < 0 or i+ori[3][0] < 0 or j+ori[3][1] < 0:
                            continue
                        l1 = data[i+ori[0][0]][j+ori[0][1]]
                        l2 = data[i+ori[1][0]][j+ori[1][1]]
                        l3 = data[i+ori[2][0]][j+ori[2][1]]
                        l4 = data[i+ori[3][0]][j+ori[3][1]]
                        if l1+l2+l3+l4=='MMSS':
                            found +=1
                            break
                    except:
                        continue
         
    return found

if __name__ == "__main__":
    start = pfc()
    day = "04"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
