from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        aux = fin.read().rstrip().split("\n")
        data = {'height': len(aux), 'width': len(aux[0]), 'antennas': {}}
        for x, row in enumerate(aux):
            for y, el in enumerate(row):
                if el == '.': continue
                if el not in data['antennas']: data['antennas'][el] = [(x,y)]
                else: data['antennas'][el].append((x,y))

    return data

def process_data_1(data):
    antinodes = []
    for freq in data['antennas']:
        for a1 in data['antennas'][freq]:
            for a2 in data['antennas'][freq]:
                if a1==a2: continue
                antinode = (2*a1[0]-a2[0], 2*a1[1]-a2[1])
                if antinode[0] >= 0 and antinode[0]<data['height'] and antinode[1]>=0 and antinode[1]<data['width']:
                    antinodes.append(antinode)
    return len(set(antinodes))

def process_data_2(data):
    antinodes = []
    for freq in data['antennas']:
        for a1 in data['antennas'][freq]:
            for a2 in data['antennas'][freq]:
                if a1==a2: continue
                antinode = (2*a1[0]-a2[0], 2*a1[1]-a2[1])
                while (antinode[0] >= 0 and antinode[0]<data['height'] and antinode[1]>=0 and antinode[1]<data['width']):
                    antinodes.append(antinode)
                    antinode = (antinode[0]-(a2[0]-a1[0]), antinode[1]-(a2[1]-a1[1]))
        if len(data['antennas'][freq]) > 0:
            antinodes += [a for a in data['antennas'][freq]]
    return len(set(antinodes))
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
