from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = {}
        line = fin.readline().rstrip()
        while line:
            origin_valve = line.split(" ")[1]
            rate = int(line[line.index("=")+1:line.index(";")])
            destination_valves = line.replace(",", "").split(" ")[9:]
            data[origin_valve] = {"rate": rate, "destination_valves": destination_valves}
            line = fin.readline().rstrip()
    return data

def check_next_state(states, next_state, next_total_pressure, next_rate, next_minutes):
    if next_state not in states:
        return True

    return next_total_pressure+next_rate*next_minutes > states[next_state]

def find_distance(data, start, end, route):
    if end in data[start]['destination_valves']:
        return 1 

    return 1+min([find_distance(data, neighbour, end, route+[neighbour]) if neighbour not in route else len(data) for neighbour in data[start]['destination_valves']])

def preprocess(state):
    distances = {}
    nodes = ['AA'] + [valve for valve in data if data[valve]['rate']>0]

    for start in nodes:
        for end in nodes:
            if start==end:
                continue

            dist = find_distance(data, start, end, [start])
            if start not in distances:
                distances[start] = {}
            if end!='AA': distances[start][end] = dist

    return nodes, distances

def recursive(data, distances, valve, min_left, pressure, solutions, visited_valves):
    if tuple(visited_valves) in solutions:
        solutions[tuple(visited_valves)] = max(pressure, solutions[tuple(visited_valves)])
    else:
        solutions[tuple(visited_valves)] = pressure
    for next_valve in distances[valve]:
        if next_valve in visited_valves: continue
        next_min_left = min_left - distances[valve][next_valve] - 1
        if next_min_left <= 0: continue
        next_visited_valves = visited_valves+[next_valve]
        next_visited_valves.sort()
        recursive(data, distances, next_valve, next_min_left, pressure+data[next_valve]['rate']*next_min_left, solutions, visited_valves+[next_valve])
    return solutions

def process_data_1(data):    
    nodes, distances = preprocess(data)

    solutions = recursive(data, distances, 'AA', 30, 0, {}, ['AA'])

    return max(solutions.values())

def process_data_2(data):
    nodes, distances = preprocess(data)

    solutions = recursive(data, distances, 'AA', 26, 0, {}, ['AA'])

    best_sol = 0
    for j, (v1, p1) in enumerate(solutions.items()):
        if j%1000 == 0:
            print(f"j={j}")
        for k, (v2, p2) in enumerate(solutions.items()):
            if (k <= j) or (p1 + p2 <= best_sol): continue
            if len(set(v1)&set(v2))==1:
                best_sol = p1+p2
    return best_sol
if __name__ == "__main__":
    start = pfc()
    day = "16"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
