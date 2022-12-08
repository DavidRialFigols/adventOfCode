from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split("\n")
    return data

def process_data_1(data):
    total_visible_trees = 0
    num_rows, num_cols = len(data), len(data[0])
    for x, row in enumerate(data):
        for y, tree in enumerate(row):
            # check horizontal trees
            visible_tree = all([row[dy]<tree for dy in range(y+1, num_cols)])
            visible_tree = visible_tree or all([row[dy]<tree for dy in range(0,y)])

            # check vertical trees
            visible_tree = visible_tree or all([data[dx][y]<tree for dx in range(x+1, num_rows)])
            visible_tree = visible_tree or all([data[dx][y]<tree for dx in range(0,x)])

            if visible_tree:
                total_visible_trees += 1
    return total_visible_trees

def calculate_visible_trees(height, trees):
    if len(trees)==0: return 0
    
    print(height, trees)
    print()
    for num, tree in enumerate(trees):
        if tree>=height:
            return num+1

    return len(trees)

def process_data_2(data):
    max_found = 0
    num_rows, num_cols = len(data), len(data[0])
    for x, row in enumerate(data):
        for y, tree in enumerate(row):
            # check horizontal trees
            visible_trees = calculate_visible_trees(tree, [row[dy] for dy in range(y+1, num_cols)])
            visible_trees *= calculate_visible_trees(tree, [row[dy] for dy in range(y-1,-1,-1)])

            # check vertical trees
            visible_trees *= calculate_visible_trees(tree, [data[dx][y] for dx in range(x+1, num_rows)])
            visible_trees *= calculate_visible_trees(tree, [data[dx][y] for dx in range(x-1,-1,-1)])

            if visible_trees > max_found:
                max_found = visible_trees
    return max_found

if __name__ == "__main__":
    start = pfc()
    day = "08"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
