#!/usr/bin/env python3

import intcode
from copy import copy

with open("2.input", "r") as f:
    program = list(map(int, f.read().split(",")))

# part 1

program_modified = copy(program)
program_modified[1] = 12
program_modified[2] = 2

print(intcode.compute(program_modified))

# part 2

def find_input(desired_result, initial_program):
    for noun in range(0,100):
        for verb in range(0,100):
            program = initial_program.copy()

            program[1] = noun
            program[2] = verb

            result = intcode.compute(program)

            if result == desired_result:
                return noun * 100 + verb

print(find_input(19690720, program))
