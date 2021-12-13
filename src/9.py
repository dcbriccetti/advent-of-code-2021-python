from typing import Iterator
import numpy as np
from numpy import ndarray
from helpers import create_grid, neighbor_offsets_no_diag

Point = ndarray

def is_lowest(row: int, col: int) -> bool:
    'Return whether the value at the given coordinates is the lowest among its neighbors'
    this_val = grid[row, col]
    for row_off, col_off in neighbor_offsets_no_diag:
        neighbor_col = col + col_off
        neighbor_row = row + row_off
        invalid_offsets = neighbor_col < 0 or neighbor_row < 0 or \
            neighbor_col >= grid.shape[1] or neighbor_row >= grid.shape[0]
        if not invalid_offsets:
            if grid[neighbor_row][neighbor_col] <= this_val:
                return False

    return True

def higher_neighbor_points(starting_point: ndarray) -> Iterator[Point]:
    'Provide a sequence of the neighbor points whose values are higher than the value at the starting point'
    starting_value: int = grid[starting_point[0], starting_point[1]]
    for neighbor_offset in neighbor_offsets_no_diag:
        explore_point: ndarray = starting_point + neighbor_offset
        if tuple(explore_point) not in explored:
            coords_in_range = 0 <= explore_point[0] < grid.shape[0] and \
                              0 <= explore_point[1] < grid.shape[1]
            if coords_in_range:
                explore_point_value = grid_value(explore_point)
                if explore_point_value != 9 and explore_point_value > starting_value:
                    yield explore_point

def basin_cells(starting_point: Point, depth=0) -> int:
    'Return the number of cells in the basin at `starting_point`'
    starting_value: int = grid_value(starting_point)
    print('  ' * depth + f'Expanding basin at {starting_point}, {starting_value}')
    cells = 1
    for explore_point in higher_neighbor_points(starting_point):
        explored.add(tuple(explore_point))
        cells += basin_cells(explore_point, depth + 1)
    return cells

def grid_value(point: ndarray) -> int:
    return grid[point[0], point[1]]

grid = create_grid('../data/9_test.txt')

low_points = np.array([(r, c) for r in range(grid.shape[0]) for c in range(grid.shape[1])
                       if is_lowest(r, c)])
print('Low points:')
print(low_points)

# Part 1
risk_level_sum = sum(map(grid_value, low_points)) + len(low_points)
print(f'Sum of risk levels: {risk_level_sum}\n')

# Part 2
explored = set()
basin_sizes = list(map(basin_cells, low_points))
basin_sizes.sort(reverse=True)
print(np.prod(basin_sizes[:3]))
