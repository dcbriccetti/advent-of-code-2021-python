import re
from dataclasses import dataclass

import helpers

@dataclass(frozen=True)
class Point3D:
    x: int
    y: int
    z: int

@dataclass(frozen=True)
class Range3D:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int

    def points_in(self):
        return (Point3D(x, y, z)
                for x in range(self.x1, self.x2 + 1)
                for y in range(self.y1, self.y2 + 1)
                for z in range(self.z1, self.z2 + 1))

def solve(include_far: bool) -> int:
    lines = helpers.lines('../data/22_test.txt')
    on_points: set[Point3D] = set()
    for line in lines:
        coords = tuple(map(int, re.findall(r'-?\d+', line)))
        if include_far or all(abs(coord) <= 50 for coord in coords):
            print(line)
            r3d = Range3D(*coords)
            points = r3d.points_in()
            if line.startswith('on'):
                on_points.update(points)
            else:
                on_points -= set(points)
    return len(on_points)

def part1() -> int:
    return solve(False)

def part2() -> int:
    return solve(True)

print('Points:', part1())
