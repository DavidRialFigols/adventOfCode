from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [[[int(k) for k in j.split(',')] for j in i.split(' -> ')] for i in fin.read().rstrip().split("\n")]
    return data

def next_unit(maxy, full_spaces):
    sand_position = [500, 0]
    rest = False
    while not rest:
        if sand_position[1] > maxy:
            return True, sand_position
        elif (sand_position[0], sand_position[1]+1) not in full_spaces:
            sand_position[1] += 1
        elif (sand_position[0]-1, sand_position[1]+1) not in full_spaces:
            sand_position = [sand_position[0]-1, sand_position[1]+1]
        elif (sand_position[0]+1, sand_position[1]+1) not in full_spaces:
            sand_position = [sand_position[0]+1, sand_position[1]+1]
        else:
            rest = True
    return False, tuple(sand_position)

def next_unit_2(maxy, full_spaces):
    sand_position = [500, 0]
    rest = False
    if (500, 0) in full_spaces:
        return True, sand_position
    while not rest:
        if sand_position[1] == maxy-1:
            return False, tuple(sand_position)
        elif (sand_position[0], sand_position[1]+1) not in full_spaces:
            sand_position[1] += 1
        elif (sand_position[0]-1, sand_position[1]+1) not in full_spaces:
            sand_position = [sand_position[0]-1, sand_position[1]+1]
        elif (sand_position[0]+1, sand_position[1]+1) not in full_spaces:
            sand_position = [sand_position[0]+1, sand_position[1]+1]
        else:
            rest = True
    return False, tuple(sand_position)

def process_data_1(data):
    full_spaces = []
    for rock in data:
        for i, coords in enumerate(rock):
            if i==0: continue
            maxx, maxy = max([rock[i-1][0], coords[0]]), max([rock[i-1][1], coords[1]])
            minx, miny = min([rock[i-1][0], coords[0]]), min([rock[i-1][1], coords[1]])
            full_spaces += [(j, coords[1]) for j in range(minx, maxx+1)]
            full_spaces += [(coords[0], j) for j in range(miny, maxy+1)]

    maxy = max([coords[1] for rock in data for coords in rock])
    full_spaces = set(full_spaces)
    rocks = full_spaces.copy()
    full = False
    sand_units = 0
    while not full:
        full, np = next_unit(maxy, full_spaces)
        if not full:
            full_spaces.add(np)
            sand_units += 1
    # dibuixar_sorra(full_spaces, rocks)
    return sand_units

def dibuixar_sorra(full_spaces, rocks):
    minx, maxx = min([i[0] for i in list(full_spaces)]), max([i[0] for i in list(full_spaces)])
    maxy = max([coords[1] for rock in data for coords in rock])
    for y in range(0, maxy+1):
        line = ''
        for x in range(minx, maxx+1):
            if (x,y) == (500,0):
                line += 'S'
            elif (x,y) in rocks:
                line += '#'
            elif (x,y) in full_spaces:
                line += 'o'
            else:
                line += '.'
        print(line)

def process_data_2(data):
    full_spaces = []
    for rock in data:
        for i, coords in enumerate(rock):
            if i==0: continue
            maxx, maxy = max([rock[i-1][0], coords[0]]), max([rock[i-1][1], coords[1]])
            minx, miny = min([rock[i-1][0], coords[0]]), min([rock[i-1][1], coords[1]])
            full_spaces += [(j, coords[1]) for j in range(minx, maxx+1)]
            full_spaces += [(coords[0], j) for j in range(miny, maxy+1)]

    maxy = 2+max([coords[1] for rock in data for coords in rock])
    full_spaces = set(full_spaces)
    rocks = full_spaces.copy()
    full = False
    sand_units = 0
    while not full:
        full, np = next_unit_2(maxy, full_spaces)
        if not full:
            full_spaces.add(np)
            sand_units += 1
    # dibuixar_sorra(full_spaces, rocks)
    return sand_units

if __name__ == "__main__":
    start = pfc()
    day = "14"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
