from typing import Iterator

class DeterministicDie:
    def __init__(self):
        def roller() -> Iterator[int]:
            while True:
                for n in range(1, 101):
                    yield n
        self.roller = roller()
        self.num_rolls = 0

    def roll(self):
        self.num_rolls += 1
        return next(self.roller)

class Player:
    next_player_number = 0
    die: DeterministicDie
    player_number: int
    pos: int
    score: int

    def __init__(self, starting_pos: int, die: DeterministicDie):
        Player.next_player_number += 1
        self.player_number = Player.next_player_number
        self.pos = starting_pos
        self.die = die
        self.score = 0

    def advance(self) -> None:
        steps = self._roll3()
        new_space = (self.pos + steps - 1) % 10 + 1
        self.score += new_space
        self.pos = new_space
        print(f'Player {self.player_number} rolls {steps} and moves to space {new_space} for a total score of {self.score}')

    def _roll3(self) -> int:
        return sum(self.die.roll() for _ in range(3))

def play():
    die = DeterministicDie()
    players = [Player(pos, die) for pos in (10, 8)]
    while True:
        for index, player in enumerate(players):
            player.advance()
            if player.score >= 1000:
                other_player_score = players[not index].score
                return other_player_score * die.num_rolls

print(play())
