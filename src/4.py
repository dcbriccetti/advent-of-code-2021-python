from pathlib import Path
from typing import List

Card = List[List[int]]

def get_card(groups: str) -> Card:
    return [list(map(int, line.split())) for line in groups.split('\n')]

def update_card(card: Card, selected: Card, pick: int) -> tuple[bool, bool]:
    def is_winner() -> bool:
        if any(sum(selected[row]) == 5 for row in range(5)):
            return True
        for col in range(5):
            if sum(selected[row][col] for row in range(5)) == 5:
                return True
        return False

    for ri in range(5):
        for ci in range(5):
            if card[ri][ci] == pick:
                selected[ri][ci] = True
                return True, is_winner()
    return False, False

def unmarked_numbers_sum(card: Card, selected: Card) -> int:
    return sum([card[ri][ci] for ri in range(5) for ci in range(5) if not selected[ri][ci]])

input_data_groups: list[str] = Path('../data/4.txt').read_text().rstrip().split('\n\n')
picks: List[int] = list(map(int, input_data_groups[0].split(',')))
cards = [get_card(input_data_groups[i]) for i in range(1, len(input_data_groups))]
print(f'There are {len(cards)} cards')
hits = [[[False for r in range(5)] for c in range(5)] for b in range(len(cards))]
winner_found = False
found_winner_ids = set()

for pick in picks:
    print(f'{pick=}')
    num_updated = 0
    for i, (card, selected) in enumerate(zip(cards, hits)):
        updated, winner = update_card(card, selected, pick)
        num_updated += updated
        if winner and i not in found_winner_ids:
            winner_found = True
            found_winner_ids.add(i)
            unmarked_sum = unmarked_numbers_sum(card, selected)
            print(f'Winner: {i=}, {unmarked_sum=}, {unmarked_sum * pick=}')
    if num_updated:
        print(f'{num_updated=}')
