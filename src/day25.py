from colorama import Fore
from numpy import ndarray, array
from helpers import create_grid, lines, Point2D, print_grid, Grid

Highlights = list[Point2D]

def step(current_gen_grid: ndarray) -> tuple[Grid, Highlights]:
    highlights: Highlights = []
    for symbol, direction in symbols_and_directions:
        next_gen_grid: Grid = current_gen_grid.copy()

        def move_if_able(ri: int, ci: int):
            here = array([ri, ci])
            new_pos_before_wrap = here + direction
            new_pos_wrapped = new_pos_before_wrap % current_gen_grid.shape
            target_coords: Point2D = tuple(new_pos_wrapped)
            if current_gen_grid[target_coords] == '.':
                next_gen_grid[ri, ci] = '.'
                next_gen_grid[target_coords] = symbol
                highlights.append((ri, ci))
                highlights.append(target_coords)

        def move_movable_symbols() -> None:
            shape = current_gen_grid.shape
            for ri in range(shape[0]):
                for ci in range(shape[1]):
                    if current_gen_grid[ri, ci] == symbol:
                        move_if_able(ri, ci)

        move_movable_symbols()
        current_gen_grid = next_gen_grid
    return current_gen_grid, highlights

grid = create_grid(lines('../data/25_test.txt'), mapper=str)
symbols_and_directions = [
    ('>', array([0, 1])),
    ('v', array([1, 0])),
]

print(Fore.GREEN + f'Starting contents' + Fore.WHITE)
print_grid(grid, [])
highlights: Highlights = []
for step_number in range(1, 1_001):
    grid, highlights = step(grid)
    print(Fore.GREEN + f'After {step_number} steps' + Fore.WHITE)
    print_grid(grid, highlights)
    if step_number > 0 and not highlights:
        break  # Stop after no movement
