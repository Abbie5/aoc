#!/usr/bin/env python3

with open("1.input", "r") as f:
    lines = f.read().splitlines()

# part 1

def calc_fuel(mass):
    return mass // 3 - 2

total = 0

for line in lines:
    total = total + calc_fuel(int(line))

print(total)

# part 2

def calc_fuel_recursive(mass):
    fuel = calc_fuel(mass)
    if fuel <= 0:
        return 0
    else:
        return fuel + calc_fuel_recursive(fuel)

total = 0

for line in lines:
    total = total + calc_fuel_recursive(int(line))

print(total)
