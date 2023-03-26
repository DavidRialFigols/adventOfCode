from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        raw_data = [i.split() for i in fin.read().rstrip().split("\n")]
        data = []
        for raw_blueprint in raw_data:
            bp = {}
            bp['id'] = int(raw_blueprint[1][:-1])
            bp['ore_robot_cost'] = int(raw_blueprint[6])
            bp['clay_robot_cost'] = int(raw_blueprint[12])
            bp['obsidian_robot_cost'] = (int(raw_blueprint[18]), int(raw_blueprint[21]))
            bp['geode_robot_cost'] = (int(raw_blueprint[27]), int(raw_blueprint[30]))
            data.append(bp)
    return data

def get_options(bp, items, robots):
    options = []
    if items[0] >= bp['geode_robot_cost'][0] and items[2] >= bp['geode_robot_cost'][1]:
        options.append(((robots[0],robots[1],robots[2],robots[3]+1), (items[0]-bp['geode_robot_cost'][0], items[1], items[2]-bp['geode_robot_cost'][1], items[3])))
    else:
        max_cost_ore = max([bp['ore_robot_cost'], bp['clay_robot_cost'], bp['obsidian_robot_cost'][0], bp['geode_robot_cost'][0]])
        max_cost_clay = bp['obsidian_robot_cost'][1]
        max_cost_obsidian = bp['geode_robot_cost'][1]
        if robots[0] < max_cost_ore and items[0] >= bp['ore_robot_cost']:
            options.append(((robots[0]+1,robots[1],robots[2],robots[3]), (items[0]-bp['ore_robot_cost'], items[1], items[2], items[3])))

        if robots[1] < max_cost_clay and items[0] >= bp['clay_robot_cost']:
            options.append(((robots[0],robots[1]+1,robots[2],robots[3]), (items[0]-bp['clay_robot_cost'], items[1], items[2], items[3])))

        if robots[2] < max_cost_obsidian and items[0] >= bp['obsidian_robot_cost'][0] and items[1] >= bp['obsidian_robot_cost'][1]:
            options.append(((robots[0],robots[1],robots[2]+1,robots[3]), (items[0]-bp['obsidian_robot_cost'][0], items[1]-bp['obsidian_robot_cost'][1], items[2], items[3])))

    return options

def obtain_resources(items, robots):
    new_items = []
    for i, r in enumerate(robots):
        new_items.append(r+items[i])
    return tuple(new_items)

def evaluate_blueprint(bp, init_minutes):
    robots = [1,0,0,0] # ore_robots, clay_robots, obsidian_robots, geode_robots
    items = [0,0,0,0] # ore, clay, obsidian, geode
    best_result = 0
    init_state = (init_minutes, tuple(items), tuple(robots), int(init_minutes*(init_minutes-1)/2))
    states = [init_state]
    visited = set([])
    while states:
        state = states.pop()
        left_min, items, robots = state[0], state[1], state[2]
        
        if left_min == 0:
            if best_result < items[3]: best_result = items[3]
            continue
        if state[3] <= best_result: 
            continue

        options = get_options(bp, items, robots)
        items = obtain_resources(items, robots)
 
        ns = (left_min-1, items, robots, int((left_min-1)*left_min/2)+robots[3]*(left_min-1)+items[3])
        if ns not in visited:
            states.append(ns)
            visited.add(ns)
        
        for op in options:
            new_items = obtain_resources(op[1], robots)
            ns = (left_min-1, new_items, op[0], int((left_min-1)*left_min/2)+(left_min-1)*op[0][3]+new_items[3])
            if ns not in visited:
                states.append(ns)
                visited.add(ns)
                
    return best_result

def process_data_1(data):
    result = 0
    for bp in data:
        result += bp['id']*evaluate_blueprint(bp, 24)
    return result

def process_data_2(data):
    result = 1
    for bp in data[:3]:
        result *= evaluate_blueprint(bp, 32)
    return result

if __name__ == "__main__":
    start = pfc()
    day = "19"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
