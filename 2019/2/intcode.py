def compute(program):
    pointer = 0

    while True:
        opcode = program[pointer]
        if opcode == 1:
            program[program[pointer + 3]] = program[program[pointer + 1]] + program[program[pointer + 2]]
            pointer = pointer + 4
        elif opcode == 2:
            program[program[pointer + 3]] = program[program[pointer + 1]] * program[program[pointer + 2]]
            pointer = pointer + 4
        elif opcode == 99:
            break
        else:
            raise ValueError("Invalid opcode")

    return program[0]
