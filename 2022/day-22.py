from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split("\n\n")
        aux = data[0].split('\n')
        data[0] = []
        for i, row in enumerate(aux):
            r = {'row': row.replace(' ', ''), 'end_col': max(row.rfind('.'), row.rfind('#'))}
            if row.find('.')>=0:
                if row.find('#') >=0:
                    r['init_col'] = min(row.find('.'), row.find('#'))
                else:
                    r['init_col'] = row.find('.')
            else:
                r['init_col'] = row.find('#')
            data[0].append(r)
 
    return data

def obtain_steps(text):
    steps = []
    act_step = ''
    for ch in text:
        if ch.isdigit():
            act_step += ch
        else:
            if len(act_step)>0:
                steps.append(int(act_step))
                act_step = ''
            steps.append(ch)
    if len(act_step) > 0:
        steps.append(int(act_step))
    return steps

def find_limits(field):
    limits = []
    for n_col in range(max([row['end_col'] for row in field])+1):
        inf = min([i for i, row in enumerate(field) if row['init_col']<=n_col and row['end_col']>=n_col])
        sup = max([i for i, row in enumerate(field) if row['init_col']<=n_col and row['end_col']>=n_col])
        limits.append((inf,sup))
    return limits

def process_data_1(data):
    steps = obtain_steps(data[1])
    field = data[0]
    limits = find_limits(field)
    person = {'position': [0,field[0]['init_col']], 'direction': 0} # Directions: 0:right, 1:down, 2:left, 3:up
    direction = {0: (0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)}
    print(limits)
    print(len(limits))
    for j, step in enumerate(steps):
        # print("====NEW STEP====")
        pos = person['position']
        if type(step) is int:
            for i in range(step):
                dp = direction[person['direction']]
                np = [person['position'][0]+dp[0], person['position'][1]+dp[1]]
                if (person['direction']%2==0) and (field[np[0]]['init_col']>np[1] or field[np[0]]['end_col']<np[1]):
                    # print("changing col")
                    np[1] = field[np[0]]['init_col'] if dp[1]>0 else field[np[0]]['end_col']
                
                elif (person['direction']%2==1) and (limits[np[1]][0]>np[0] or limits[np[1]][1]<np[0]):
                    # print("Changing row")
                    np[0] = limits[np[1]][0] if dp[0] > 0 else limits[np[1]][1] # move to limit sup if you are going up, and to limit inf if you are going down
                
                coords = [np[0], np[1]-field[np[0]]['init_col']]
                
                if field[coords[0]]['row'][coords[1]]=='#': break

                print(f"{person['position']} => {np}")
                person['position'] = np
        else:
            # print(f"Turn {step}")
            if step=='R':   person['direction']=(person['direction']+1)%4
            else:           person['direction']=(person['direction']-1)%4
        # print(f"Initial position: {pos}")
        # print(f"Final position: {person['position']}")
        # print()
        # if j%25 == 0:
        #     print(input())
    print(person)
    return (person['position'][0]+1)*1000+(person['position'][1]+1)*4+person['direction']

class cube:
    __slots__ = ['rows', 'faces', 'size']

    def __init__(self, rows):
        self.rows = rows
        self.faces = self.obtain_faces(rows)
        self.size = 50

    def faces(self, rows):
        face_size = 4
        faces = [
        {'init_col': rows[0]['init_col'], 'init_row': 0, 'turn': 0, 'mirror': False},
        {'init_col': rows[self.size]['init_col'], 'init_row': self.size, 'turn': 1, 'mirror': False},
        {'init_col': rows[self.size*2]['init_col'], 'init_row': , 'turn': 2, 'mirror': },
        {'init_col': , 'init_row': , 'turn': 3, 'mirror': },
        {'init_col': , 'init_row': , 'turn': 0, 'mirror': },
        {'init_col': , 'init_row': , 'turn': , 'mirror': },
        ]

        
                


def process_data_2(data):
    steps = obtain_steps(data[1])
    field = data[0]

    limits = find_limits(field)
    person = {'position': [0,field[0]['init_col']], 'direction': 0} # Directions: 0:right, 1:down, 2:left, 3:up
    direction = {0: (0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)}
    print(limits)
    print(len(limits))
    for j, step in enumerate(steps):
        # print("====NEW STEP====")
        pos = person['position']
        if type(step) is int:
            for i in range(step):
                dp = direction[person['direction']]
                np = [person['position'][0]+dp[0], person['position'][1]+dp[1]]
                if (person['direction']%2==0) and (field[np[0]]['init_col']>np[1] or field[np[0]]['end_col']<np[1]):
                    # print("changing col")
                    np[1] = field[np[0]]['init_col'] if dp[1]>0 else field[np[0]]['end_col']
                
                elif (person['direction']%2==1) and (limits[np[1]][0]>np[0] or limits[np[1]][1]<np[0]):
                    # print("Changing row")
                    np[0] = limits[np[1]][0] if dp[0] > 0 else limits[np[1]][1] # move to limit sup if you are going up, and to limit inf if you are going down
                
                coords = [np[0], np[1]-field[np[0]]['init_col']]
                
                if field[coords[0]]['row'][coords[1]]=='#': break

                print(f"{person['position']} => {np}")
                person['position'] = np
        else:
            # print(f"Turn {step}")
            if step=='R':   person['direction']=(person['direction']+1)%4
            else:           person['direction']=(person['direction']-1)%4
        # print(f"Initial position: {pos}")
        # print(f"Final position: {person['position']}")
        # print()
        # if j%25 == 0:
        #     print(input())
    print(person)
    return (person['position'][0]+1)*1000+(person['position'][1]+1)*4+person['direction']

if __name__ == "__main__":
    start = pfc()
    day = "22"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
