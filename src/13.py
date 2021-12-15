from typing import Iterable
from helpers import lines, Point

def fold(points: set[Point], axis: str, fold_point: int) -> set[Point]:
    'Return a new set of points, folded at the specified position along the specified axis (x or y)'
    new_points: set[Point] = set()
    coord_index = 0 if axis == 'x' else 1
    for point in points:
        coords: list[int] = list(point)
        if coords[coord_index] > fold_point:
            coords[coord_index] -= 2 * (coords[coord_index] - fold_point)
        new_points.add(Point.new(coords))

    print(f'Folding along {axis}={fold_point}, {len(new_points):,} points remain')
    return new_points

def draw_image(points: Iterable[Point]) -> None:
    print()
    max_x, max_y = [max(p[i] for p in points) for i in range(2)]
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print('😀' if (x, y) in points else '🥶', end='')
        print()

def process() -> None:
    coord_lines, fold_commands = lines('../data/13_test.txt', sep='\n\n')
    points: set[Point] = set(Point.new([int(s) for s in line.split(',')])
                             for line in coord_lines.split('\n'))

    # Example fold command: fold along y=7
    axis_pos = len('fold along ')
    coord_pos = axis_pos + 2

    for fold_command in fold_commands.split('\n'):
        points = fold(points, fold_command[axis_pos], int(fold_command[coord_pos:]))

    draw_image(points)

process()
