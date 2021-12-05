from pathlib import Path
from typing import List, Tuple
import numpy as np
from numpy import ndarray

groups = Path('../data/4.txt').read_text().rstrip().split('\n\n')
picks: List[int] = list(map(int, groups[0].split(',')))

def get_board(groups: str) -> np.ndarray:
    board = [list(map(int, line.split())) for line in groups.split('\n')]
    return np.array(board, dtype=object)

boards: list[ndarray] = [get_board(groups[i]) for i in range(1, len(groups))]
print(f'There are {len(boards)} boards')
selecteds = np.zeros([len(boards), 5, 5], dtype=bool)

winner_found = False


def is_winner(selected) -> bool:
    if any(selected[row].all() for row in range(5)):
        return True
    for col in range(5):
        if selected[:][col].all():
            return True

def update_board(board: np.ndarray, selected: np.ndarray, pick: int) -> tuple[bool, bool]:
    for ri in range(5):
        for ci in range(5):
            if board[ri][ci] == pick:
                selected[ri, ci] = True
                return True, is_winner(selected)
    return False, False

def unmarked_numbers_sum(board: np.ndarray, selected: np.ndarray) -> int:
    return sum([board[ri][ci] for ri in range(5) for ci in range(5) if not selected[ri][ci]])

while picks:
    pick = picks.pop(0)
    print(f'{pick=}')
    num_updated = 0
    for i, (board, selected) in enumerate(zip(boards, selecteds)):
        updated, winner = update_board(board, selected, pick)
        num_updated += updated
        uns = unmarked_numbers_sum(board, selected)
        if winner:
            print(f'Winner: {i=}, {uns=}, {uns * pick=}')
        # print(board)
        # print(selected)
    if num_updated:
        print(f'{num_updated=}')
# print(selecteds)
