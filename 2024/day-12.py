from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split("\n")
    return data

def separate_regions(positions):
    regions = []
    visited = set()
    for act_pos in positions:
        if act_pos in visited: continue

        visited.add(act_pos)
        act_region = [act_pos]
        to_check = [act_pos]
        while len(to_check) > 0:
            pos = to_check.pop()
            for neighbor in [(pos[0]+1,pos[1]),(pos[0]-1,pos[1]),(pos[0],pos[1]+1),(pos[0],pos[1]-1)]:
                if neighbor in positions and neighbor not in visited:
                    act_region.append(neighbor)
                    to_check.append(neighbor)
                    visited.add(neighbor)
        regions.append(act_region)
    return regions

def calculate_price_p1(regions):
    price = 0
    for r in regions:
        area = len(r)
        perimeter = 0
        for pos in r:
            if (pos[0]+1,pos[1]) not in r: perimeter +=1
            if (pos[0]-1,pos[1]) not in r: perimeter +=1
            if (pos[0],pos[1]+1) not in r: perimeter +=1
            if (pos[0],pos[1]-1) not in r: perimeter +=1
        price += area*perimeter
    return price

def process_data_1(data):
    letters_pos = {}
    for x, row in enumerate(data):
        for y, l in enumerate(row):
            if l not in letters_pos:
                letters_pos[l] = [(x,y)]
            else:
                letters_pos[l].append((x,y))
    res = 0
    for l in letters_pos:
        regions = separate_regions(letters_pos[l])
        res += calculate_price_p1(regions)
    return res

def calculate_price_p2(regions):
    price = 0
    for r in regions:
        area = len(r) 
        edges = {(-1,0): [], (1,0): [], (0,1): [], (0,-1): []}
        for pos in r:
            for edge in edges:
                if (pos[0]+edge[0], pos[1]+edge[1]) not in r: edges[edge].append(pos)
        n_sides = 0
        for edge in edges:
            visited = set()
            for pos in edges[edge]:
                if pos in visited: continue
                
                visited.add(pos)
                to_check = [pos]
                aux_edge = [pos]
                while len(to_check) > 0:
                    act_pos = to_check.pop()
                    for neighbor in [(act_pos[0]+edge[1],act_pos[1]+edge[0]),(act_pos[0]-edge[1],act_pos[1]-edge[0])]:
                        if neighbor in edges[edge] and neighbor not in visited:
                            visited.add(neighbor)
                            to_check.append(neighbor)
                            aux_edge.append(neighbor)
                n_sides +=1
        price += area*n_sides
    return price

def process_data_2(data):
    letters_pos = {}
    for x, row in enumerate(data):
        for y, l in enumerate(row):
            if l not in letters_pos:
                letters_pos[l] = [(x,y)]
            else:
                letters_pos[l].append((x,y))
    res = 0
    for l in letters_pos:
        regions = separate_regions(letters_pos[l])
        res += calculate_price_p2(regions)
    return res

if __name__ == "__main__":
    start = pfc()
    day = "12"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
