#!/usr/bin/env python3

from wires import parse, Direction, Coordinate, find_intersects

with open("input", "r") as f:
    wires = parse(f)

def on_line(coordinate, line):
    result = False

    if line.get_direction() == Direction.X:
        if coordinate.y == line.start.y:
            if (
                    (line.start.x <= coordinate.x <= line.end.x) or
                    (line.start.x >= coordinate.x >= line.end.x)
            ):
                result = True

    elif line.get_direction() == Direction.Y:
        if coordinate.x == line.start.x:
            if (
                    (line.start.y <= coordinate.y <= line.end.y) or
                    (line.start.y >= coordinate.y >= line.end.y)
            ):
                result = True

    return result

def least_steps_to(origin, coordinate, wire):
    steps = 0
    for line in wire:
        if on_line(coordinate, line):
            if line.get_direction() == Direction.X:
                steps += abs(coordinate.x - line.start.x)
            elif line.get_direction() == Direction.Y:
                steps += abs(coordinate.y - line.start.y)

            return steps

        else:
            steps += line.get_length()

origin = Coordinate(0,0)
wire1 = wires[0]
wire2 = wires[1]
intersects = find_intersects(wire1, wire2)

least_total_steps = None
for intersect in intersects:
    coordinate = intersect.get_coordinate()
    steps1 = least_steps_to(origin, coordinate, wire1)
    steps2 = least_steps_to(origin, coordinate, wire2)
    total_steps = steps1 + steps2

    if (least_total_steps == None) or (total_steps < least_total_steps):
        least_total_steps = total_steps

print(least_total_steps)
