from enum import Enum, auto
from copy import copy

class Coordinate:
    """Represents a point in 2D space"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pp(self):
        return f"({self.x},{self.y})"

class Direction(Enum):
    """Whether a line is parallel to the x-axis or the y-axis"""
    X = auto()
    Y = auto()

class Line:
    """Really a line segment, starts and ends at specified coordinates (has a direction)"""
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_direction(self):
        """Get the direction of the line"""
        if self.start.x == self.end.x:
            return Direction.Y
        elif self.start.y == self.end.y:
            return Direction.X
        else:
            raise ValueError("Line must be ortholinear")

    def get_length(self):
        """Get the length of a line. This is easy since lines are always parallel to the x- or y-axis"""
        if self.get_direction() == Direction.X:
            return abs(self.end.x - self.start.x)
        elif self.get_direction() == Direction.Y:
            return abs(self.end.y - self.start.y)

    def pp(self):
        return f"{self.start.pp()} -> {self.end.pp()}"

class Intersect:
    """The intersection between two lines. Is not actually calculated until asked for"""
    def __init__(self, line1, line2):
        self.line1 = line1
        self.line2 = line2

    def get_coordinate(self):
        """Get the coordinate of the intersection. Will return None if there is none"""
        result = None
        line1 = self.line1
        line2 = self.line2

        # if the lines are parallel, we don't need to do any more checking
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
    """Test if two lines are parallel"""
    return line1.get_direction() == line2.get_direction()

def manhattan_distance(start, end):
    """Calculate the Manhattan distance from a start point to an end point"""
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
    """Find all intersections between two wires"""
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
