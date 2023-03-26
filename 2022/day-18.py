from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [tuple([int(j) for j in i.split(',')]) for i in fin.read().rstrip().split("\n")]
    return data

def process_data_1(data):
    surface = 6*len(data)
    sides = ((1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1))
    for cube in data:
        for side in sides:
            side_cube = (cube[0]+side[0], cube[1]+side[1], cube[2]+side[2])
            if side_cube in data:
                surface -= 1

    return surface

def process_data_2(data):
    surface = 0
    exit = max([max(i) for i in data])
    sides = ((1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1))
    num_cubes = len(data)
    wrong_cubes, good_cubes = [], []
    for i, cube in enumerate(data):
        for side in sides:
            routes = [ [(cube[0]+side[0], cube[1]+side[1], cube[2]+side[2])]]
            visited = []
            while routes:
                route = routes.pop()
                sc = route[-1]
                if sc in data:
                    continue
                if max(sc) > exit or min(sc) < 0 or sc in good_cubes:
                    surface += 1
                    good_cubes += visited
                    break
                if sc in wrong_cubes:
                    break
                for s in sides:
                    next_sc = (sc[0]+s[0],sc[1]+s[1],sc[2]+s[2])
                    if (next_sc not in visited) and (next_sc not in data):
                        visited.append(next_sc)
                        routes.append(route+[next_sc])
                routes.sort(key=lambda x: max(x[-1]))
            if max(sc) < exit and min(sc) > 0 and sc not in good_cubes:
                wrong_cubes += visited

    return surface

if __name__ == "__main__":
    start = pfc()
    day = "18"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
