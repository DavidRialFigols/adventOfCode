from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip()
    return data

class Rock:
    __slots__ = ['bottom_height', 'rows', 'pos']

    def __init__(self, rows, bottom_height):
        self.rows = rows
        self.bottom_height = bottom_height
        self.pos = 2

    def move_h(self, move):
        if move=="<":
            for i, row in enumerate(self.rows):
                self.rows[i] = row << 1
                self.pos -= 1
        else:
            for i, row in enumerate(self.rows):
                self.rows[i] = row >> 1
                self.pos += 1

    def check_move_h(self, move, fixed_rocks):
        if move=="<":
            for i, row in enumerate(self.rows):
                if row & 0b1000000: return False
                if i<len(fixed_rocks):
                    if (row<<1) & fixed_rocks[i]: return False
        else:
            for i, row in enumerate(self.rows):
                if row & 0b0000001: return False
                if i<len(fixed_rocks):
                    if (row>>1) & fixed_rocks[i]: return False
        return True

    def overlaps(self, fixed_rocks):
        for i, row in enumerate(self.rows):
            if i<len(fixed_rocks):
                if row & fixed_rocks[i]:
                    return True
        return False

    def obtain_snippet_fixed_rocks(self, fixed_rocks):
        if self.bottom_height >= len(fixed_rocks):
            return []
        
        return fixed_rocks[self.bottom_height:min(self.bottom_height+len(self.rows), len(fixed_rocks))]

def fall_rock(rock, fixed_rocks, index_jet, data):
    max_index_jet = len(data)
    falling = True
    snippet_fixed_rocks = rock.obtain_snippet_fixed_rocks(fixed_rocks)
    while not rock.overlaps(snippet_fixed_rocks):
        if rock.check_move_h(data[index_jet], snippet_fixed_rocks):
            rock.move_h(data[index_jet])
        index_jet = (index_jet+1)%max_index_jet
        rock.bottom_height -= 1
        snippet_fixed_rocks = rock.obtain_snippet_fixed_rocks(fixed_rocks)
    
    rock.bottom_height += 1

    if rock.bottom_height > len(fixed_rocks)+1:
        print(f"There has been an error!")
    if rock.bottom_height == len(fixed_rocks):
        fixed_rocks += rock.rows
    else:
        for i in range(min(len(rock.rows), len(fixed_rocks)-rock.bottom_height)):
            fixed_rocks[rock.bottom_height+i] = fixed_rocks[rock.bottom_height+i] | rock.rows[i]
        if len(rock.rows) > len(fixed_rocks) - rock.bottom_height:
            for i in range(len(fixed_rocks) - rock.bottom_height, len(rock.rows)):
                fixed_rocks.append(rock.rows[i])

    return fixed_rocks, index_jet



def process_data_1(data):
    fixed_rocks = [0b1111111]
    rocks = {
        0: [
            0b0011110
           ],
        1: [
            0b0001000,
            0b0011100,
            0b0001000
           ],
        2: [
            0b0011100,
            0b0000100,
            0b0000100
           ],
        3: [
            0b0010000,
            0b0010000,
            0b0010000,
            0b0010000
           ],
        4: [
            0b0011000,
            0b0011000
           ]   
    }
    index_jet = 0
    for n_rock in range(2022):
        rock = Rock(rocks[n_rock%5].copy(), len(fixed_rocks)+3)
        fixed_rocks, index_jet = fall_rock(rock, fixed_rocks, index_jet, data)

    return len(fixed_rocks)-1

def process_data_2(data):
    fixed_rocks = [0b1111111]
    rocks = {
        0: [
            0b0011110
           ],
        1: [
            0b0001000,
            0b0011100,
            0b0001000
           ],
        2: [
            0b0011100,
            0b0000100,
            0b0000100
           ],
        3: [
            0b0010000,
            0b0010000,
            0b0010000,
            0b0010000
           ],
        4: [
            0b0011000,
            0b0011000
           ]   
    }
    index_jet = 0

    states = {}
    total_rocks = 1000000000000
    for n_rock in range(total_rocks):
        rock = Rock(rocks[n_rock%5].copy(), len(fixed_rocks)+3)
        fixed_rocks, index_jet = fall_rock(rock, fixed_rocks, index_jet, data)
        state = (index_jet, n_rock%5, rock.pos)
        if state not in states:
            states[state] = (n_rock, len(fixed_rocks))
        else:
            cycle_n_rocks = n_rock - states[state][0]
            cycle_height = len(fixed_rocks) - states[state][1]
            if (total_rocks - n_rock - 1)%(cycle_n_rocks) == 0:
                return len(fixed_rocks) + cycle_height*int((total_rocks-n_rock-1)/cycle_n_rocks) -1

    return len(fixed_rocks)-1

if __name__ == "__main__":
    start = pfc()
    day = "17"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
