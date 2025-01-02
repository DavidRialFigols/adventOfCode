from tabnanny import check
from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        aux = fin.read().rstrip().split("\n\n")
        data = {'designs': set(aux[0].split(', ')), 'patterns': aux[1].split('\n')}
    return data


def process_data_1(data):
    possible = 0
    for pattern in data['patterns']:
        possibilities = ['']
        visited = set()
        while len(possibilities) > 0:
            s = possibilities.pop()
            if s in visited: continue
            if s == pattern: break
            visited.add(s)
            for d in data['designs']:
                ns = s+d
                if ns == pattern[:len(ns)]:
                    possibilities.append(ns)
            possibilities = sorted(possibilities, key=lambda x: len(x), reverse=True)
        if s==pattern: 
            possible += 1
    return possible

def process_data_2(data):
    possible = 0

    for pattern in data['patterns']:
        visited = {}

        def check_pattern(remaining_pattern):
            if not remaining_pattern: return 1

            if remaining_pattern in visited: return visited[remaining_pattern]

            result = 0
            for d in data['designs']:
                if remaining_pattern[:len(d)]==d:
                    result += check_pattern(remaining_pattern[len(d):])
            visited[remaining_pattern] = result
            return result
        
        possible += check_pattern(pattern)
    return possible

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
