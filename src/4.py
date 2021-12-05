from pathlib import Path

class Card:
    numbers: list[list[int]]
    hits: list[list[bool]]
    is_winner: bool

    def __init__(self, card_as_string: str):
        '''Create a Card from input like the following:
        22 13 17 11  0\n 8  2 23  4 24\n21  9 14 16  7\n 6 10  3 18  5\n 1 12 20 15 19'''
        self.numbers = [list(map(int, line.split())) for line in card_as_string.split('\n')]
        self.hits = [[False for _ in range(5)] for _ in range(5)]
        self.is_winner = False

    def update(self, pick: int) -> bool:
        def is_winner() -> bool:
            def col_selected(col: int) -> bool:
                return sum(self.hits[row][col] for row in range(5)) == 5

            return (
                any(sum(self.hits[row]) == 5 for row in range(5)) or  # Any completed rows?
                any(col_selected(col) for col in range(5)))           # Any completed columns?

        for ri in range(5):
            for ci in range(5):
                if self.numbers[ri][ci] == pick:
                    self.hits[ri][ci] = True
                    self.is_winner = is_winner()
                    return self.is_winner
        return False

    def unmarked_numbers_sum(self) -> int:
        return sum([self.numbers[ri][ci] for ri in range(5) for ci in range(5) if not self.hits[ri][ci]])

def solve_both_parts():
    input_groups: list[str] = Path('../data/4_test.txt').read_text().rstrip().split('\n\n')
    picks: list[int] = list(map(int, input_groups[0].split(',')))
    card_data_groups: list[str] = input_groups[1:]  # Skip 1st group which is picks
    cards: list[Card] = [Card(card_data) for card_data in card_data_groups]
    hits = [[[False for r in range(5)] for c in range(5)] for b in range(len(cards))]

    for pick in picks:
        for card, selected in zip(cards, hits):
            if not card.is_winner:
                card_wins = card.update(pick)
                if card_wins:
                    unmarked_sum = card.unmarked_numbers_sum()
                    print(f'Winner: {unmarked_sum=}, {pick=}, {unmarked_sum * pick=}')

solve_both_parts()
