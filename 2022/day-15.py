from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [[[int(j[j.index('=')+1:j.index(',')]), int(j[j.rindex('=')+1:])] for j in i.split(': ')] for i in fin.read().rstrip().split("\n")]
    return data

def manhattan_distance(c1, c2):
    return sum([abs(c1[i]-c2[i]) for i in range(len(c1))])

def process_data_1(data):
    line_to_check = 10
    forbidden_pos = set([])
    occupied_pos = set([])
    for line in data:
        sensor, beacon = line[0], line[1]
        d_to_line = abs(line_to_check-sensor[1])
        d_to_beacon = manhattan_distance(sensor, beacon)
        if d_to_beacon > d_to_line:
            spare_d = d_to_beacon - d_to_line
            aux = [i for i in range(sensor[0]-spare_d, sensor[0]+spare_d+1)]
        else:
            aux = []
        forbidden_pos.update(aux)

        if beacon[1] == line_to_check:
            occupied_pos.update([beacon[1]])

    #     print(f"Sensor {sensor} || d_to_line {d_to_line} || beacon {beacon} || d_s_b {d_to_beacon} || forbidden_pos {aux}")
    # print()
    # print(forbidden_pos)
    # print(occupied_pos)
    return len(forbidden_pos)-len(occupied_pos)

def process_data_2(data):
    min_coord, max_coord = 0, 4000000
    lines = {}
    k = 0
    for line in data:
        print(f"Starting line {k}")
        k += 1
        sensor, beacon = line[0], line[1]
        # d_to_line = abs(line_to_check-sensor[1])
        d_to_beacon = manhattan_distance(sensor, beacon)
        for row in range(max(min_coord,sensor[1]-d_to_beacon), min(max_coord, sensor[1]+d_to_beacon+1)):
            if row in lines:
                if not lines[row]:
                    continue
                cols = lines[row]
                spare_d = d_to_beacon - abs(row-sensor[1])
                cols += [(max(sensor[0]-spare_d, min_coord), min(sensor[0]+spare_d, max_coord))]
                cols.sort()
                i = min_coord
                for x in cols:
                    if i<x[0]-1:
                        break
                    i = max(i, x[1])
                if i >= max_coord:
                    lines[row] = False
            else:
                spare_d = d_to_beacon - abs(row-sensor[1])
                lines[row] = [(max(sensor[0]-spare_d, min_coord), min(sensor[0]+spare_d, max_coord))]

    for k in lines:
        if lines[k]:
            i = min_coord
            cols = lines[k]
            for x in cols:
                if i<x[0]-1:
                    print (i+1, k)
                    return (i+1)*4000000 + k
                i = max(i, x[1])

    return None

def process_data_2_not_so_slow(data):
    min_coord, max_coord = 0, 4000000
    for line_to_check in range(max_coord+1):
        available_pos = set([i for i in range(max_coord+1)])
        na_pos = []
        for line in data:
            sensor, beacon = line[0], line[1]
            d_to_line = abs(line_to_check-sensor[1])
            d_to_beacon = manhattan_distance(sensor, beacon)
            if d_to_beacon > d_to_line:
                spare_d = d_to_beacon - d_to_line
                na_pos += [(max(sensor[0]-spare_d, min_coord), min(sensor[0]+spare_d, max_coord))]
        na_pos.sort(key=lambda x: x[0])
        if na_pos[0][0]>0:
            return line_to_check

        for i in range(1, len(na_pos)):
            if i==len(na_pos)-1 and na_pos[i][1]<max_coord:
                return max_coord*4000000  + line_to_check
            if na_pos[i-1][1]+1 < na_pos[i][0]:
                return (na_pos[i-1][1]+1)*4000000  + line_to_check
        
        print(f"proceeding to next line num {line_to_check+1}")
            
        # print()
        # print(forbidden_pos)
        # print(occupied_pos)
    return "None empty position find"

def process_data_2_slow(data):
    min_x, max_x = 0, 4000000
    min_y, max_y = 0, 4000000
    for line_to_check in range(max_y+1):
        available_pos = set([i for i in range(max_x+1)])
        for line in data:
            sensor, beacon = line[0], line[1]
            d_to_line = abs(line_to_check-sensor[1])
            d_to_beacon = manhattan_distance(sensor, beacon)
            if d_to_beacon > d_to_line:
                spare_d = d_to_beacon - d_to_line
                available_pos = available_pos.difference(set([i for i in range(max(sensor[0]-spare_d, min_x), min(sensor[0]+spare_d+1, max_x+1))]))
            
        if len(available_pos) > 0:
            return list(available_pos)[0]*4000000  + line_to_check
        else:
            print(f"proceeding to next line num {line_to_check+1}")
            
        # print()
        # print(forbidden_pos)
        # print(occupied_pos)
    return "None empty position find"

if __name__ == "__main__":
    start = pfc()
    day = "15"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
