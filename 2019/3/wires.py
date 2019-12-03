from enum import Enum
from copy import copy

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pp(self):
        return f"({self.x},{self.y})"

class Direction(Enum):
    X = 0
    Y = 1

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_direction(self):
        if self.start.x == self.end.x:
            return Direction.Y
        elif self.start.y == self.end.y:
            return Direction.X
        else:
            raise ValueError("Line must be ortholinear")

    def get_length(self):
        if self.get_direction() == Direction.X:
            return abs(self.end.x - self.start.x)
        elif self.get_direction() == Direction.Y:
            return abs(self.end.y - self.start.y)

    def pp(self):
        return f"{self.start.pp()} -> {self.end.pp()}"

class Intersect:
    def __init__(self, line1, line2):
        self.line1 = line1
        self.line2 = line2

    def get_coordinate(self):
        result = None
        line1 = self.line1
        line2 = self.line2

        if are_parallel(line1, line2):
            return result

        if line1.get_direction() == Direction.X:
            if (
                    (
                        (line1.start.x <= line2.start.x <= line1.end.x) or
                        (line1.start.x >= line2.start.x >= line1.end.x)
                    ) and
                    (
                        (line2.start.y <= line1.start.y <= line2.end.y) or
                        (line2.start.y >= line1.start.y >= line2.end.y)
                    )
            ):
                result = Coordinate(line2.start.x, line1.start.y)

        elif line1.get_direction() == Direction.Y:
            if (
                    (
                        (line1.start.y <= line2.start.y <= line1.end.y) or
                        (line1.start.y >= line2.start.y >= line1.end.y)
                    ) and
                    (
                        (line2.start.x <= line1.start.x <= line2.end.x) or
                        (line2.start.x >= line1.start.x >= line2.end.x)
                    )
            ):
                result = Coordinate(line1.start.x, line2.start.y)

        return result

    def pp(self):
        return f"{self.line1.pp()} + {self.line2.pp()} : {self.get_coordinate().pp()}"

def are_parallel(line1, line2):
    return line1.get_direction() == line2.get_direction()

def manhattan_distance(start, end):
    return abs(end.x - start.x) + abs(end.y - start.y)

def parse(_file):
    wires = [s.split(",") for s in _file.read().splitlines()]

    points = [[Coordinate(0,0)], [Coordinate(0,0)]]

    # construct points array
    for i in range(len(points)):
        current_coordinate = Coordinate(0,0)
        wire = wires[i]

        for movement in wire:
            direction = movement[0]
            length = int(movement[1:])

            if direction == "R":
                current_coordinate.x += length
            elif direction == "L":
                current_coordinate.x -= length
            elif direction == "U":
                current_coordinate.y += length
            elif direction == "D":
                current_coordinate.y -= length
            else:
                raise ValueError("Invalid direction")

            points[i].append(copy(current_coordinate))

    # construct lines
    lines = [[],[]]
    for j in range(len(points)):
        wire = points[j]
        for k in range(len(wire) - 1):
            start, end = wire[k], wire[k+1]
            lines[j].append(copy(Line(start, end)))

    return lines

# find the intersects between two wires
def find_intersects(wire1, wire2):
    intersects = []

    for line1 in wire1:
        for line2 in wire2:
            intersect = Intersect(line1, line2)
            coordinate = intersect.get_coordinate()
            if coordinate == None:
                pass
            else:
                intersects.append(copy(intersect))

    return intersects
