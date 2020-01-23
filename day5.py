from aocd.models import Puzzle
puzzle = Puzzle(year=2019, day=5)
data = puzzle.input_data

inputs = [int(x) for x in data.split(",")]

def intcode2(inputs):
    i = 0
    error = 0
    while i < len(inputs):
        print(f"statement: {inputs[i]}")
        if inputs[i] == 99:
            return inputs, 0
        par1 = inputs[i+1]
        par2 = inputs[i+2]
        par3 = inputs[i+3]
        if len(str(inputs[i])) > 1:
            opcode = int(str(inputs[i])[-2::])
            try:
                par1 = int(str(inputs[i])[-3])
                if par1 == 1:
                    par1 = i+1
                par2 = int(str(inputs[i])[-4])
                if par2 == 1:
                    par2 = i+2
                par3 = int(str(inputs[i])[-5])
                if par3 == 1:
                    par3 = i+3
            except IndexError:
                pass
        else:
            opcode = inputs[i]
            print(f"identified opcode: {opcode}")

        if opcode == 1:
            inputs[par3] = inputs[par1] + inputs[par2]
            i += 4
        if opcode == 2:
            inputs[par3] = inputs[par1]* inputs[par2]
            i += 4
        if opcode == 3:
            a = "10"
            while len(a) != 1:
                a = input("Type a single-digit number:")
                number = int(a)
            inputs[inputs[i+1]] = number
            i += 2
        if opcode == 4:
            print(inputs[inputs[i+1]])
            i += 2
        if opcode not in (1, 2, 3, 4):
            error += 1

test, error = intcode2(inputs)
print(error)
