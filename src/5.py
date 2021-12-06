from collections import Counter
from dataclasses import dataclass
from itertools import chain
from pathlib import Path
from typing import Iterator


@dataclass(frozen=True)
class Point:
    x: int
    y: int

class Line:
    repr: str
    points: list[Point]

    def __init__(self, line_string: str):
        '''Create a Line from input like the following:
        0,9 -> 5,9
        '''
        self.repr = line_string
        pairs: list[str] = line_string.split(' -> ')
        self.points = [Point(x, y)
                       for x, y in (map(int, pair.split(','))
                                    for pair in pairs)]

    def __repr__(self):
        return self.repr

    def is_horz_or_vert(self) -> bool:
        return self.points[0].y == self.points[1].y or \
               self.points[0].x == self.points[1].x

    def points_on_line(self) -> list[Point]:
        def chg(start: int, end: int):
            'Return change amount to get from start to end (-1, 0, 1)'
            diff = end - start
            return 0 if not diff else 1 if diff > 0 else -1

        p1, p2 = self.points
        x_chg = chg(p1.x, p2.x)
        y_chg = chg(p1.y, p2.y)
        x = p1.x
        y = p1.y
        points = []
        while not (x == p2.x and y == p2.y):
            points.append(Point(x, y))
            x += x_chg
            y += y_chg
        points.append(Point(x, y))
        return points

input_lines: list[str] = Path('../data/5.txt').read_text().rstrip().split('\n')
lines: list[Line] = [Line(il) for il in input_lines]
horz_vert_lines: Iterator[Line] = (line for line in lines
                                   if line.is_horz_or_vert())

def part1():
    return num_with_at_least_2(horz_vert_lines)

def part2():
    return num_with_at_least_2(lines)

def num_with_at_least_2(lines: Iterator[Line]) -> int:
    points: list[Point] = list(chain(*(line.points_on_line() for line in lines)))
    counter = Counter(points)
    return sum(1 for num_lines_here in counter.values() if num_lines_here >= 2)

print(part1(), part2())
