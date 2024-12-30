from atexit import register
from logging import ERROR
from time import perf_counter as pfc
import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        aux = fin.read().rstrip().split("\n\n")
        data = {'registers': [int(i.split(': ')[1]) for i in aux[0].split('\n')], 'program': eval(aux[1].split(': ')[1])}
    return data

def adv(registers, operand, n_instruction, output):
    combo = obtain_combo(registers, operand)
    registers[0] = int(registers[0]/(2**combo))
    return registers, n_instruction+2, output

def bxl(registers, operand, n_instruction, output):
    registers[1] = registers[1] ^ operand
    return registers, n_instruction+2, output

def bst(registers, operand, n_instruction, output):
    combo = obtain_combo(registers, operand)
    registers[1] = combo % 8
    return registers, n_instruction+2, output

def jnz(registers, operand, n_instruction, output):
    """ The jnz instruction (opcode 3) does nothing if the A register is 0. 
    However, if the A register is not zero, it jumps by setting the instruction 
    pointer to the value of its literal operand; if this instruction jumps, the 
    instruction pointer is not increased by 2 after this instruction.
    """

    if registers[0]==0: return registers, n_instruction+2, output
    return registers, operand, output

def bxc(registers, operand, n_instruction, output):
    """The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C,
    then stores the result in register B. (For legacy reasons, this instruction reads an operand
    but ignores it.)
    """
    registers[1] = registers[1] ^ registers[2]
    return registers, n_instruction+2, output

def out(registers, operand, n_instruction, output):
    """The out instruction (opcode 5) calculates the value of its combo operand modulo 8, 
    then outputs that value. (If a program outputs multiple values, they are separated by commas.)
    """
    combo = obtain_combo(registers, operand)
    output += ',' + str(combo%8) if len(output)>0 else str(combo%8)
    return registers, n_instruction+2, output

def bdv(registers, operand, n_instruction, output):
    """The bdv instruction (opcode 6) works exactly like the adv instruction
    except that the result is stored in the B register. (The numerator is
    still read from the A register.)
    """
    combo = obtain_combo(registers, operand)
    registers[1] = int(registers[0]/(2**combo))
    return registers, n_instruction+2, output

def cdv(registers, operand, n_instruction, output):
    """The cdv instruction (opcode 7) works exactly like the adv instruction
    except that the result is stored in the C register. (The numerator is still
    read from the A register.)
    """
    combo = obtain_combo(registers, operand)
    registers[2] = int(registers[0]/(2**combo))
    return registers, n_instruction+2, output

def obtain_combo(registers, num):
    """
    Combo operands 0 through 3 represent literal values 0 through 3.
    Combo operand 4 represents the value of register A.
    Combo operand 5 represents the value of register B.
    Combo operand 6 represents the value of register C.
    Combo operand 7 is reserved and will not appear in valid programs.
    """
    if 0<=num<=3: return num
    if num==4: return registers[0]
    if num==5: return registers[1]
    if num==6: return registers[2]
    if num>6:
        print("ERROR, this should not happen!")
        raise ERROR

def process_data_1(data):
    instructions = {
        0: adv,
        1: bxl,
        2: bst,
        3: jnz,
        4: bxc,
        5: out,
        6: bdv,
        7: cdv
    }
    n_instruction = 0
    output = ''
    while n_instruction < len(data['program']):
        opcode, operand = data['program'][n_instruction], data['program'][n_instruction+1]
        data['registers'], n_instruction, output = instructions[opcode](data['registers'], operand, n_instruction, output)

    return output

def process_data_2(data):
    instructions = {
        0: adv,
        1: bxl,
        2: bst,
        3: jnz,
        4: bxc,
        5: out,
        6: bdv,
        7: cdv
    }
    value = 0
    registers = [0,0,0]
    found = False
    for i in reversed(range(len(data['program']))):
        while not found:
            registers = [value, data['registers'][1], data['registers'][2]]
            output = ''
            n_instruction = 0
            while n_instruction < len(data['program']):
                opcode, operand = data['program'][n_instruction], data['program'][n_instruction+1]
                registers, n_instruction, output = instructions[opcode](registers, operand, n_instruction, output)
                
            if len(output)>1 and eval(output)==data['program']:
                found=True
            elif (i==len(data['program'])-1 and int(output) == data['program'][i]) or (len(output)>1 and list(eval(output))==list(data['program'][i:])):
                break
            else:
                value += 1
        if not found:
            value <<= 3

    return value

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
