#!/usr/bin/env python3


def calc_fuel(mass):
    return mass // 3 - 2

total = 0

with open("input", "r") as f:
    for line in f:
        total = total + calc_fuel(int(line))
    print(total)
