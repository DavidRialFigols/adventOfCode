from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [[i.split(' = ')[0].split(' to '), int(i.split(' = ')[1])] for i in fin.read().rstrip().split("\n")]
    return data

def process_data_1(data):
    unique_places = set([i[0][0] for i in data]).union(set([i[0][1] for i in data]))
    data += [[[i[0][1], i[0][0]], i[1]] for i in data]
    all_routes = sorted(data, key=lambda x: x[1], reverse=True)
    visited = []
    while True:
        route = all_routes.pop()
        if "".join(route[0]) in visited: continue
        else: visited.append("".join(route[0]))
        
        if len(route[0])==len(unique_places): break
        
        last_visited = route[0][-1]

        for next_route in data:
            if (next_route[0][0] == last_visited) and (next_route[0][1] not in route[0]):
                next_route = [route[0]+[next_route[0][1]], route[1]+next_route[1]]
                all_routes.append(next_route)

        all_routes = sorted(all_routes, key=lambda x: x[1], reverse=True)
    return route[1]

def process_data_2(data):
    max_dist = max([i[1] for i in data])
    unique_places = set([i[0][0] for i in data]).union(set([i[0][1] for i in data]))
    data += [[[i[0][1], i[0][0]], i[1]] for i in data]
    reverse_data = [[i[0], max_dist-i[1]] for i in data]
    all_routes = sorted(reverse_data, key=lambda x: x[1], reverse=True)
    visited = []
    while True:
        route = all_routes.pop()
        if "".join(route[0]) in visited: continue
        else: visited.append("".join(route[0]))
        
        if len(route[0])==len(unique_places): break
        
        last_visited = route[0][-1]

        for next_route in reverse_data:
            if (next_route[0][0] == last_visited) and (next_route[0][1] not in route[0]):
                next_route = [route[0]+[next_route[0][1]], route[1]+next_route[1]]
                all_routes.append(next_route)

        all_routes = sorted(all_routes, key=lambda x: x[1], reverse=True)
    
    total_dist = 0
    for i in range(1, len(route[0])):
        total_dist += [j[1] for j in data if route[0][i-1]==j[0][0] and route[0][i]==j[0][1]][0]
    
    return total_dist

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
