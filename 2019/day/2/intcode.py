from enum import IntEnum

class Opcode(IntEnum):
    ADD = 1
    MUL = 2
    END = 99

def compute(program):
    """Process Intcode program and return value in index 0"""
    pointer = 0

    while True:
        opcode = program[pointer]
        noun = program[pointer + 1]
        verb = program[pointer + 2]
        result = program[pointer + 3]

        if opcode == Opcode.ADD:
            program[result] = program[noun] + program[verb]
        elif opcode == Opcode.MUL:
            program[result] = program[noun] * program[verb]
        elif opcode == Opcode.END:
            break
        else:
            raise ValueError("Invalid opcode")

        pointer += 4

    return program[0]
