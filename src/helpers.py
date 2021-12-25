from pathlib import Path
from typing import Iterator, NamedTuple, Sequence
import numpy as np
from numpy import ndarray
from colorama import Fore

Point2D = tuple[int, int]
Grid = ndarray

def create_grid(lines: list[str], mapper=int):
    grid = np.array([[mapper(ch) for ch in row] for row in lines])
    print(f'Grid shape: {grid.shape}')
    return grid

def lines(filename: str, sep='\n') -> list[str]:
    return Path(filename).read_text().strip().split(sep)

def print_grid(grid: ndarray, highlights: list[Point2D], color=Fore.LIGHTYELLOW_EX) -> None:
    for ri in range(grid.shape[0]):
        for ci in range(grid.shape[1]):
            c = color if (ri, ci) in highlights else Fore.WHITE
            print(c + grid[ri, ci], end='')
        print()
    print(Fore.WHITE)

def plural(num):
    'Return an s or an empty string. (0 items, 1 item, 2 items)'
    return '' if num == 1 else 's'

neighbor_offsets_x_y = np.array([  # x, y
              [0, -1],
    [-1, 0],           [1, 0],
              [0,  1],
])

neighbor_offsets_no_diag = np.array([  # row, column
              [-1, 0],
    [ 0, -1],          [ 0, 1],
              [ 1, 0],
])

neighbor_offsets = np.array([  # row, column
    [-1, -1], [-1, 0], [-1, 1],
    [ 0, -1],          [ 0, 1],
    [ 1, -1], [ 1, 0], [ 1, 1]
])

rc_9_offsets = [
    (-1,  -1), (-1,  0), (-1,  1),
    ( 0,  -1), ( 0,  0), ( 0,  1),
    ( 1,  -1), ( 1,  0), ( 1,  1),
]

def neighbor_coords(shape: tuple[int, int], r: int, c: int, diag=True) -> Iterator[tuple[int, int]]:
    for nro, nco in neighbor_offsets if diag else neighbor_offsets_no_diag:
        nr = r + nro
        nc = c + nco
        if 0 <= nr < shape[0] and 0 <= nc < shape[1]:
            yield nr, nc

class Point(NamedTuple):
    x: int
    y: int

    @classmethod
    def new(cls, coords: Sequence):
        return Point(coords[0], coords[1])
