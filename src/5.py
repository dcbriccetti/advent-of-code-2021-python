from pathlib import Path

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Line:
    repr: str
    points: list[Point]

    def __init__(self, line_string: str):
        '''Create a Line from input like the following:
        0,9 -> 5,9
        '''
        self.repr = line_string
        pairs: list[str] = line_string.split(' -> ')
        points = [Point(int(x), int(y)) for x, y in (map(int, pair.split(',')) for pair in pairs)]
        self.points = points

    def __repr__(self):
        return self.repr

    def is_horz(self) -> bool:
        return self.points[0].y == self.points[1].y

    def is_vert(self) -> bool:
        return self.points[0].x == self.points[1].x

    def is_horz_or_vert(self) -> bool:
        return self.is_horz() or self.is_vert()

    def contains_point(self, point: Point) -> bool:
        if self.is_horz():
            min_x = min(p.x for p in self.points)
            max_x = max(p.x for p in self.points)
            return min_x <= point.x <= max_x
        else:
            min_y = min(p.y for p in self.points)
            max_y = max(p.y for p in self.points)
            return min_y <= point.y <= max_y

input_lines: list[str] = Path('../data/5_test.txt').read_text().rstrip().split('\n')
lines: list[Line] = [Line(il) for il in input_lines]
hv_lines: list[Line] = [line for line in lines if line.is_horz_or_vert()]
max_x1 = max(line.points[0].x for line in hv_lines)
max_x2 = max(line.points[1].x for line in hv_lines)
max_x = max(max_x1, max_x2)
max_y1 = max(line.points[0].y for line in hv_lines)
max_y2 = max(line.points[1].y for line in hv_lines)
max_y = max(max_y1, max_y2)


def part1():
    num_2_or_more = 0
    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if num_at_point := sum(line.contains_point(Point(x, y)) for line in hv_lines):
                # print(f'({x}, {y}): {num_at_point}')
                if num_at_point >= 2:
                    num_2_or_more += 1

    return num_2_or_more

print(part1())
