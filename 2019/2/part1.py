#!/usr/bin/env python3

import intcode

with open("input", "r") as f:
    program = list(map(int, f.read().split(",")))

    program[1] = 12
    program[2] = 2

    print(intcode.compute(program))
