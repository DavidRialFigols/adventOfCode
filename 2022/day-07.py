from time import perf_counter as pfc
import copy

class Node():
    def __init__(self, parent=None, is_directory=False, children=[], size=False):
        self.parent = parent
        if not is_directory:
            if len(children)>0: raise Exception('A file can not have children!')
            if not size: raise Exception('Size not indicated!')    
            self.size = size
        else:
            self.children = children
            self.size = self.calculate_size()
        
    def calculate_size(self):
        size = 0
        for ch in self.children:
            size += ch.size
        return size

class Tree():
    def __init__(self, root, nodes=[]):
        self.root = root
        self.nodes = nodes
        if root not in nodes:
            nodes.append(root)

def create_directory(data, initial_line, directory = {}):
    next_line = initial_line
    mode = 'cd'
    while next_line < len(data) and data[next_line] != '$ cd ..':
        line = data[next_line]
        if line == '$ ls': # it is ls instruction
            mode = 'ls'
        elif line[0] == '$': # it is a cd instruction
            subdirectory = line.split(' ')[-1]
            if subdirectory in directory:
                directory[subdirectory], next_line = create_directory(data, next_line+1, directory[subdirectory])
            else:
                directory[subdirectory], next_line = create_directory(data, next_line+1)
        elif mode == 'ls': # it is not an instruction and we are in a ls mode
            first, second = line.split(' ')[0], line.split(' ')[1]
            if first == 'dir':
                if second not in directory:
                    directory[second] = {}
            else:
                directory[second] = int(first)

        next_line += 1
    return directory, next_line

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split("\n")
        root_directory, final_line = create_directory(data, 1)
        print(final_line)
        data = root_directory
    return data

def recursive_part_1(directory, acumulative_size):
    size = 0
    for i in directory:
        if type(directory[i])==int:
            size += directory[i]
        else:
            subsize, acumulative_size = recursive_part_1(directory[i], acumulative_size)
            size += subsize
    if size <= 100000:
        acumulative_size += size

    return size, acumulative_size

def recursive_part_2(directory, smallest_size, needed_size):
    size = 0
    for i in directory:
        if type(directory[i])==int:
            size += directory[i]
        else:
            subsize, smallest_size = recursive_part_2(directory[i], smallest_size, needed_size)
            size += subsize
    if size >= needed_size and size<smallest_size:
        smallest_size = size
    return size, smallest_size

def process_data_1(data):
    root_size, acumulative_size = recursive_part_1(data, 0)
    return acumulative_size

def process_data_2(data):
    root_size, smallest_size = recursive_part_2(data, float('inf'), 1)
    root_size, smallest_size = recursive_part_2(data, float('inf'), -40000000 + root_size)
    return smallest_size

if __name__ == "__main__":
    start = pfc()
    day = "07"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
