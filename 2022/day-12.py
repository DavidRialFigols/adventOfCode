from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split("\n")
    return data

def get_position(data, letter):
    return [(i,j) for i, row in enumerate(data) for j, l in enumerate(row) if l==letter][0]

def process_data_1(data):
    S = get_position(data, 'S')
    E = get_position(data, 'E')
    data[E[0]] = data[E[0]].replace('E','z')
    data[S[0]] = data[S[0]].replace('S','a')
    moves = [(0,1),(1,0),(0,-1),(-1,0)]
    visited_places = []
    possible_moves = [(0,E)]
    while len(possible_moves)>0:
        possible_moves = sorted(possible_moves, key=lambda x: x[0], reverse=True)
        cost, pos = possible_moves.pop()
        if pos in visited_places: continue
        visited_places.append(pos)
        if pos == S:
            return cost
        # print(f"Starting position {pos}")
        for dy,dx in moves:
            nm = (pos[0]+dy, pos[1]+dx)
            if nm[0]>=0 and nm[0]<len(data) and nm[1]>=0 and nm[1]<len(data[0]):
                # print(f"next move correct")
                # print(f"1st: {data[nm[0]][nm[1]]} - {ord(data[nm[0]][nm[1]])}")
                # print(f"2st: {data[pos[0]][pos[1]]} - {ord(data[pos[0]][pos[1]])}")

                if ord(data[nm[0]][nm[1]]) >= ord(data[pos[0]][pos[1]])-1 and nm not in visited_places:
                    # man_dist = abs(nm[0]-S[0]) + abs(nm[1]-S[1])
                    possible_moves.append([cost+1, nm])
                    # print(f"actual position: {pos} - move appended: {nm}")
    return "ERROR"

def process_data_2(data):
    S = get_position(data, 'S')
    E = get_position(data, 'E')
    data[E[0]] = data[E[0]].replace('E','z')
    data[S[0]] = data[S[0]].replace('S','a')
    moves = [(0,1),(1,0),(0,-1),(-1,0)]
    visited_places = []
    possible_moves = [(0,E)]
    while len(possible_moves)>0:
        possible_moves = sorted(possible_moves, key=lambda x: x[0], reverse=True)
        cost, pos = possible_moves.pop()
        if pos in visited_places: continue
        visited_places.append(pos)
        if data[pos[0]][pos[1]]=='a':
            return cost
        # print(f"Starting position {pos}")
        for dy,dx in moves:
            nm = (pos[0]+dy, pos[1]+dx)
            if nm[0]>=0 and nm[0]<len(data) and nm[1]>=0 and nm[1]<len(data[0]):
                # print(f"next move correct")
                # print(f"1st: {data[nm[0]][nm[1]]} - {ord(data[nm[0]][nm[1]])}")
                # print(f"2st: {data[pos[0]][pos[1]]} - {ord(data[pos[0]][pos[1]])}")

                if ord(data[nm[0]][nm[1]]) >= ord(data[pos[0]][pos[1]])-1 and nm not in visited_places:
                    # man_dist = abs(nm[0]-S[0]) + abs(nm[1]-S[1])
                    possible_moves.append([cost+1, nm])
                    # print(f"actual position: {pos} - move appended: {nm}")
    return "ERROR"

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
