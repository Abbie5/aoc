#!/usr/bin/env python3

with open("input", "r") as f:
    lines = f.read().splitlines()

def calc_fuel(mass):
    return mass // 3 - 2

total = 0

for line in lines:
    total = total + calc_fuel(int(line))

print(total)
