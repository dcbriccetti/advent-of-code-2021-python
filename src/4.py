from pathlib import Path
from typing import List

groups = Path('../data/4.txt').read_text().rstrip().split('\n\n')
picks: List[int] = list(map(int, groups[0].split(',')))

def get_board(groups: str) -> List[List[int]]:
    board = [list(map(int, line.split())) for line in groups.split('\n')]
    return board

boards = [get_board(groups[i]) for i in range(1, len(groups))]
print(f'There are {len(boards)} boards')
selecteds = [[[False for r in range(5)] for c in range(5)] for b in range(len(boards))]

winner_found = False


def is_winner(selected) -> bool:
    if any(sum(selected[row]) == 5 for row in range(5)):
        return True
    for col in range(5):
        if sum(selected[row][col] for row in range(5)) == 5:
            return True
    return False

def update_board(board, selected, pick: int) -> tuple[bool, bool]:
    for ri in range(5):
        for ci in range(5):
            if board[ri][ci] == pick:
                selected[ri][ci] = True
                return True, is_winner(selected)
    return False, False

def unmarked_numbers_sum(board, selected) -> int:
    return sum([board[ri][ci] for ri in range(5) for ci in range(5) if not selected[ri][ci]])

num_winners = 0

while picks and num_winners < 10:
    pick = picks.pop(0)
    print(f'{pick=}')
    num_updated = 0
    for i, (board, selected) in enumerate(zip(boards, selecteds)):
        updated, winner = update_board(board, selected, pick)
        num_updated += updated
        uns = unmarked_numbers_sum(board, selected)
        if winner:
            num_winners += 1
            print(f'Winner: {i=}, {uns=}, {uns * pick=}')
        # print(board)
        # print(selected)
    if num_updated:
        print(f'{num_updated=}')
# print(selecteds)
