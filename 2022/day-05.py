from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = fin.read().rstrip().split("\n")

        # obtain the stacks
        i = 0
        aux = [[] for i in range(9)]
        while len(data[i])>0:
            for j, ch in enumerate(data[i]):
                if ch in [' ', '[', ']']: continue
                aux[int((j-1)/4)].append(ch)
            i+=1
        for j in aux:
            j.pop()
            j.reverse()
        stacks = [j.copy() for j in aux]

        # now the procedure
        i += 1
        procedure = []
        for j in range(i, len(data)):
            step = data[j].split(' ')
            procedure.append((int(step[1]), (int(step[3])-1, int(step[5])-1))) # each step is: (number of crates to move, (initial stack, final stack))
        
        data = {'stacks': stacks, 'procedure': procedure}
    return data

def process_data_1(data):
    stacks = data['stacks']
    for step in data['procedure']:
        num_crates, st0, st1 = step[0], step[1][0], step[1][1]
        for i in range(num_crates):
            stacks[st1].append(stacks[st0].pop())

    result = ''.join([st.pop() for st in stacks])
    return result

def process_data_2(data):
    stacks = data['stacks']
    for step in data['procedure']:
        num_crates, st0, st1 = step[0], step[1][0], step[1][1]
        aux = []
        for i in range(num_crates):
            aux.append(stacks[st0].pop())
        aux.reverse()
        stacks[st1] += aux

    result = ''.join([st.pop() for st in stacks])
    return result

if __name__ == "__main__":
    start = pfc()
    day = "05"
    data = read_file(day)
    print(f"Data: {data}")
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
