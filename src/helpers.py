from pathlib import Path
from typing import Iterator

import numpy as np

def create_grid(filename):
    grid = np.array([[int(digit_in_string) for digit_in_string in row] for row in lines(filename)])
    print(f'Grid shape: {grid.shape}')
    return grid

def lines(filename: str, sep='\n') -> list[str]:
    return Path(filename).read_text().strip().split(sep)

def ints_from_line(line: str) -> tuple[int, int]:
    a, b = line.split(',')
    return int(a), int(b)

neighbor_offsets_no_diag = np.array([
              [-1, 0],
    [ 0, -1],          [ 0, 1],
              [ 1, 0],
])

neighbor_offsets = np.array([
    [-1, -1], [-1, 0], [-1, 1],
    [ 0, -1],          [ 0, 1],
    [ 1, -1], [ 1, 0], [ 1, 1]
])

def neighbor_coords(shape: tuple[int, int], r: int, c: int, diag=True) -> Iterator[tuple[int, int]]:
    for nro, nco in neighbor_offsets if diag else neighbor_offsets_no_diag:
        nr = r + nro
        nc = c + nco
        if 0 <= nr < shape[0] and 0 <= nc < shape[1]:
            yield nr, nc
