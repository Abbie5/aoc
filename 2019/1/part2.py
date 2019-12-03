#!/usr/bin/env python3

def calc_fuel(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + calc_fuel(fuel)

total = 0

with open("input", "r") as f:
    for line in f:
        total = total + calc_fuel(int(line))
    print(total)
