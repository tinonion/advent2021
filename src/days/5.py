from ast import parse
from multiprocessing.sharedctypes import Value
import re
from typing import Counter

class VentLine:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __repr__(self) -> str:
        return f"({self.x1},{self.y1} -> {self.x2},{self.y2})"

    def is_diagonal(self):
        return self.x1 != self.x2 and self.y1 != self.y2 

    def get_points(self) -> list[tuple[int, int]]:
        x1, x2, y1, y2 = self.x1, self.x2, self.y1, self.y2

        pts = []

        if self.is_diagonal():
            y_inc = -1 if y1 > y2 else 1
            x_inc = -1 if x1 > x2 else 1

            curr_x = x1
            curr_y = y1

            pts.append((curr_x, curr_y))
            while curr_x != x2: 
                curr_x += x_inc
                curr_y += y_inc
                
                pts.append((curr_x, curr_y))

        else:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    pts.append((x, y))

        return pts


def parse_input(input_path: str) -> list[VentLine]:
    line_pat = re.compile(r"^(\d+),(\d+) -> (\d+),(\d+)$")

    vent_lines = []
    with open(input_path, 'r') as fp:
        for line in fp:
            m = line_pat.match(line)

            if not m:
                raise ValueError(f"could not parse {line=}")

            x1 = m[1]
            y1 = m[2]
            x2 = m[3]
            y2 = m[4]
            vent_lines.append(VentLine(int(x1), int(y1), int(x2), int(y2)))

    return vent_lines

def part_one(input_path: str) -> int:
    vent_lines = parse_input(input_path)

    line_pts = []
    for vent_line in vent_lines:
        if vent_line.is_diagonal():
            continue

        line_pts += vent_line.get_points()
    
    counter = Counter([str(pt) for pt in line_pts])

    more_than_two = 0
    for count in counter.values():
        if count > 1:
            more_than_two += 1

    return more_than_two

def part_two(input_path: str) -> int:
    vent_lines = parse_input(input_path)

    line_pts = []
    for vent_line in vent_lines:
        line_pts += vent_line.get_points()
    
    counter = Counter([str(pt) for pt in line_pts])

    more_than_two = 0
    for count in counter.values():
        if count > 1:
            more_than_two += 1

    return more_than_two