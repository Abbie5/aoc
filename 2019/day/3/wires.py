from enum import Enum, auto
from copy import copy

class Coordinate:
    """Represents a point in 2D space"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
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

    def __repr__(self):
        return f"{self.start} -> {self.end}"

    def get_direction(self):
        """Get the direction of the line"""
        if self.start.x == self.end.x:
            return Direction.Y

        elif self.start.y == self.end.y:
            return Direction.X

        else:
            raise ValueError(f"Line is not on the grid")

    def get_length(self):
        """Get the length of a line. This is easy since lines are always parallel to the x- or y-axis"""
        if self.get_direction() == Direction.X:
            return abs(self.end.x - self.start.x)

        elif self.get_direction() == Direction.Y:
            return abs(self.end.y - self.start.y)

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

        # this code is messy, i know ;_;
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

def are_parallel(line1, line2):
    """Test if two lines are parallel"""
    return line1.get_direction() == line2.get_direction()

def manhattan_distance(start, end):
    """Calculate the Manhattan distance from a start point to an end point"""
    return abs(end.x - start.x) + abs(end.y - start.y)

def parse(_file):
    """Parse a file into a list of wires (lists of lines)"""
    wires_raw = [line.split(",") for line in _file.read().splitlines()]
    num_wires = 2 # assumed

    origin = Coordinate(0,0)

    # construct wires array
    wires = [[], []]
    for wire_index in range(num_wires):
        current_coordinate = copy(origin)
        wire_raw = wires_raw[wire_index]

        for movement in wire_raw:
            direction = movement[0]
            length = int(movement[1:])

            prev_coordinate = copy(current_coordinate)

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

            line = Line(copy(prev_coordinate), copy(current_coordinate))
            wires[wire_index].append(copy(line))

    return wires

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
