from helpers import lines, ints_from_line

Point = tuple[int, int]

def fold(points: set[Point], axis: str, fold_point: int) -> set[Point]:
    new_points: set[tuple[int, int]] = set()
    coord_index = 0 if axis == 'x' else 1
    for point in points:
        coords: list[int] = list(point)
        if coords[coord_index] > fold_point:
            coords[coord_index] -= 2 * (coords[coord_index] - fold_point)
        new_points.add((coords[0], coords[1]))

    print(f'Folding along {axis}={fold_point}, {len(new_points):,} points remain')
    return new_points

def plot_points():
    global y, x
    print()
    for y in range(max(p[1] for p in points) + 1):
        for x in range(max(p[0] for p in points) + 1):
            print('😀' if (x, y) in points else '🥶', end='')
        print()

coord_lines, fold_commands = lines('../data/13.txt', sep='\n\n')
points = set(ints_from_line(line) for line in coord_lines.split('\n'))

axis_pos = len('fold along ')
coord_pos = axis_pos + 2

for fold_command in fold_commands.split('\n'):
    points = fold(points, fold_command[axis_pos], int(fold_command[coord_pos:]))

plot_points()
