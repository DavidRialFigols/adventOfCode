from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [i.split('\n') for i in fin.read().rstrip().split("\n\n")]
        for i, line in enumerate(data):
            data[i][0] = eval(data[i][0])
            data[i][1] = eval(data[i][1])
            print(data[i])
    return data

def check_right_order(list1, list2):
    for i, item in enumerate(list1):
        if i >= len(list2): break
        if type(item)==int:
            if type(list2[i])==int and item!=list2[i]:
                return True, item<list2[i]
            elif type(list2[i])==list:
                final, ordenat = check_right_order([item], list2[i])
                if final:
                    return final, ordenat
    
        elif type(item)==list:
            if type(list2[i])==int:
                final, ordenat = check_right_order(item, [list2[i]])
                if final:
                    return final, ordenat
            elif type(list2[i])==list:
                final, ordenat = check_right_order(item, list2[i])
                if final:
                    return final, ordenat
    final = len(list1) != len(list2)
    ordenat = len(list1)<=len(list2)
    return final, ordenat

def process_data_1(data):
    return sum([i+1 for i, lists in enumerate(data) if check_right_order(lists[0],lists[1])[1]])

def partition(l, lindex, rindex):
    pivot = l[rindex]
    i = lindex-1
    for j in range(lindex, rindex):
        if check_right_order(l[j], pivot)[1]:
            i+=1
            l[i], l[j] = l[j], l[i]
    l[rindex], l[i+1] = l[i+1], l[rindex]
    return l, i+1

def quicksort(l, lindex, rindex):
    if (lindex < rindex):
        l, p = partition(l, lindex, rindex)
        l = quicksort(l, lindex, p-1)
        l = quicksort(l, p, rindex)
    return l

def process_data_2(data):
    new_data = [[[2]],[[6]]]
    for i in data:
        new_data+=i
    
    l = quicksort(new_data, 0, len(new_data)-1)

    return (l.index([[2]])+1)*(l.index([[6]])+1)

if __name__ == "__main__":
    start = pfc()
    day = "13"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
