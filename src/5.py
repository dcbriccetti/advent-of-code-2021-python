from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from itertools import chain
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
        points = [Point(int(x), int(y))
                  for x, y in (map(int, pair.split(','))
                               for pair in pairs)]
        self.points = points

    def __repr__(self):
        return self.repr

    def is_horz(self) -> bool:
        return self.points[0].y == self.points[1].y

    def is_vert(self) -> bool:
        return self.points[0].x == self.points[1].x

    def is_horz_or_vert(self) -> bool:
        return self.is_horz() or self.is_vert()

    def points_on_line(self) -> list[Point]:
        xes = [p.x for p in self.points]
        ys = [p.y for p in self.points]
        min_x = min(xes)
        max_x = max(xes)
        min_y = min(ys)
        max_y = max(ys)
        if self.is_horz():
            return [Point(x, self.points[0].y) for x in range(min_x, max_x + 1)]
        if self.is_vert():
            return [Point(self.points[0].x, y) for y in range(min_y, max_y + 1)]
        dist = max_x - min_x
        points = [Point(min_x + offset, min_y + offset) for offset in range(dist + 1)]
        return points

input_lines: list[str] = Path('../data/5_test.txt').read_text().rstrip().split('\n')
lines: list[Line] = [Line(il) for il in input_lines]
horz_vert_lines: list[Line] = [line for line in lines if line.is_horz_or_vert()]

def part1():
    return num_with_at_least_2(horz_vert_lines)

def part2():
    return num_with_at_least_2(lines)

def num_with_at_least_2(lines: Iterator[Line]) -> int:
    points: list[Point] = list(chain(*(line.points_on_line() for line in lines)))
    counter = Counter(points)
    return sum(1 for num_lines_here in counter.values() if num_lines_here >= 2)


print(part2())
