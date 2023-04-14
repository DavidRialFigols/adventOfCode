from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        data = [i.split() for i in fin.read().rstrip().split("\n")]
    return data

def process_instructions(data, number):
    variables = {'x':0,'y':0,'z':0,'w':0}
    index_input = 0
    for i, instruction in enumerate(data):
        # print('=====================')
        # print(f"Variables: {variables}")
        # print(f"Instruction: {instruction}")
        if instruction[0] == 'inp':
            variables[instruction[1]] = int(number[index_input])
            index_input += 1
        elif instruction[0] == 'add':
            variables[instruction[1]] += variables[instruction[2]] if instruction[2].isalpha() else int(instruction[2])
        elif instruction[0] == 'mul':
            variables[instruction[1]] *= variables[instruction[2]] if instruction[2].isalpha() else int(instruction[2])
        elif (instruction[0] == 'div'):
            if (not instruction[2].isalpha() or (instruction[2].isalpha() and variables[instruction[2]]!=0)):
                variables[instruction[1]] /= variables[instruction[2]] if instruction[2].isalpha() else int(instruction[2])
                variables[instruction[1]] = int(variables[instruction[1]])
            else:
                # print("error")
                break
        elif (instruction[0] == 'mod'):
            if (variables[instruction[1]]>=0) and ((not instruction[2].isalpha()) or (instruction[2].isalpha() and variables[instruction[2]>0])):
                variables[instruction[1]] %= variables[instruction[2]] if instruction[2].isalpha() else int(instruction[2])
            else:
                break
        elif instruction[0] == 'eql':
            variables[instruction[1]] = int(variables[instruction[2]]==variables[instruction[1]]) if instruction[2].isalpha() else int(variables[instruction[1]]==int(instruction[2]))
        else:
            print("ERROR=================================")
        # print(f"New values variables: {variables}")
    return i==len(data)-1 and variables['z']==0, index_input-1

def process_data_1(data):
    number = ''.join(['9' for i in range(14)])
    stop = False
    while not stop:
        index_input = 13
        if not '0' in number:
            stop, index_input = process_instructions(data, number)
            if index_input < 13:
                print(stop, index_input, number)
            

        number = str(int(number)-int(10**(13-index_input)))

    number = str(int(number)+1)
    return ''.join([str(n) for n in number])

def process_data_2(data):
    return


if __name__ == "__main__":
    start = pfc()
    day = "24"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"Result part 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"Result part 2: {result_2}")
    print(f"Duration: {pfc()-start}")
