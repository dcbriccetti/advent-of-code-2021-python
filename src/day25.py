from colorama import Fore
from numpy import ndarray, array
from helpers import create_grid, lines, Point2D, print_grid, Grid, plural

Highlights = list[Point2D]

def step(step_number: int, current_gen_grid: ndarray) -> tuple[Grid, int]:
    num_moves = 0
    for i, (symbol, direction) in enumerate(symbols_and_directions):
        num_moves_in_phase = 0
        highlights: Highlights = []
        next_gen_grid: Grid = current_gen_grid.copy()

        def move_if_able(ri: int, ci: int) -> bool:
            here = array([ri, ci])
            new_pos_before_wrap = here + direction
            new_pos_wrapped = new_pos_before_wrap % current_gen_grid.shape
            target_coords: Point2D = tuple(new_pos_wrapped)
            if current_gen_grid[target_coords] == '.':
                next_gen_grid[ri, ci] = '.'
                next_gen_grid[target_coords] = symbol
                highlights.append((ri, ci))
                highlights.append(target_coords)
                return True
            return False

        def move_movable_symbols() -> int:
            num_moved = 0
            shape = current_gen_grid.shape
            for ri in range(shape[0]):
                for ci in range(shape[1]):
                    if current_gen_grid[ri, ci] == symbol:
                        if move_if_able(ri, ci):
                            num_moved += 1
            return num_moved

        num_moves_in_phase += move_movable_symbols()
        print(Fore.GREEN +
              f'After step {step_number}-{i + 1}, {num_moves_in_phase} move{plural(num_moves_in_phase)}' +
              Fore.WHITE)
        print_grid(next_gen_grid, highlights, [Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX][i])
        current_gen_grid = next_gen_grid
        num_moves += num_moves_in_phase
    return current_gen_grid, num_moves

grid = create_grid(lines('../data/25_test.txt'), mapper=str)
symbols_and_directions = [
    ('>', array([0, 1])),
    ('v', array([1, 0])),
]

print(Fore.GREEN + f'Starting contents' + Fore.WHITE)
print_grid(grid, [])
for step_number in range(1, 1_001):
    grid, num_changes = step(step_number, grid)
    if step_number > 0 and num_changes == 0:
        break  # Stop after no movement
