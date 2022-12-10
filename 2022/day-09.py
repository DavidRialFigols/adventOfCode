from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [[i.split(' ')[0], int(i.split(' ')[1])] for i in fin.read().rstrip().split("\n")]
    return data

def process_data_1(data):
    places_tail = [(0,0)]
    head, tail = [0,0], [0,0]
    for move in data:
        if move[0] == 'U': direction = (0,1)
        elif move[0] == 'D': direction = (0,-1)
        elif move[0] == 'R': direction = (1,0)
        elif move[0] == 'L': direction = (-1,0)
        for st in range(move[1]):
            head = [head[0]+direction[0], head[1]+direction[1]]
            if abs(head[0]-tail[0]) >= 2 or abs(head[1]-tail[1]) >= 2: # then move the tail
                tail = [tail[0]+direction[0], tail[1]+direction[1]]
                if abs(head[0]-tail[0]) + abs(head[1]-tail[1]) == 2: # it has to move diagonally
                    if direction[0]==0: # the head is moving in a vertical direction
                        tail[0] += 1 if head[0]>tail[0] else -1
                    else:
                        tail[1] += 1 if head[1]>tail[1] else -1
                places_tail.append(tuple(tail))

    return len(set(places_tail))

def move_knot(head, tail):
    if abs(head[0]-tail[0]) == 2: # then move the tail vertically
        tail[0] += 1 if head[0]>tail[0] else -1
        if abs(head[1]-tail[1]) >= 1: # it has to move diagonally
            tail[1] += 1 if head[1]>tail[1] else -1

    elif abs(head[1]-tail[1]) == 2: # then move the tail vertically
        tail[1] += 1 if head[1]>tail[1] else -1
        if abs(head[0]-tail[0]) >= 1: # it has to move diagonally
            tail[0] += 1 if head[0]>tail[0] else -1    
    return tail    

def process_data_2(data):
    places_tail = [(0,0)]
    knots = [[0,0] for i in range(10)]
    for move in data:
        if move[0] == 'U': direction = (0,1)
        elif move[0] == 'D': direction = (0,-1)
        elif move[0] == 'R': direction = (1,0)
        elif move[0] == 'L': direction = (-1,0)
        for st in range(move[1]):
            head = knots[0]
            knots[0] = [head[0]+direction[0], head[1]+direction[1]]
            for i in range(1,len(knots)):
                knots[i] = move_knot(knots[i-1],knots[i])
            places_tail.append(tuple(knots[-1]))

    return len(set(places_tail))

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
