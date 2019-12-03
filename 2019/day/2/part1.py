#!/usr/bin/env python3

import intcode
from copy import copy

with open("input", "r") as f:
    program = list(map(int, f.read().split(",")))

program_modified = copy(program)
program_modified[1] = 12
program_modified[2] = 2

print(intcode.compute(program_modified))
