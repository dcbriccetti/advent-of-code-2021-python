from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

starting_days_until_spawns: list[int] = list(map(int,
    Path('../data/6.txt').read_text().rstrip().split(',')))

@dataclass
class Fish:
    days_until_spawn: int
    num_members: int

    def __init__(self, days_until_spawn: int, num_members: int):
        self.days_until_spawn = days_until_spawn
        assert num_members > 0
        self.num_members = num_members

    def __repr__(self):
        return f'{self.days_until_spawn}×{self.num_members:,}'

    def update(self) -> int:
        if self.days_until_spawn == 0:
            self.days_until_spawn = 6
            return self.num_members
        self.days_until_spawn -= 1
        return 0

@dataclass
class FishPopulation:
    fishes: list[Fish]
    day: int = 0

    def __init__(self, starting_days_until_spawns: Iterable[int]):
        self.fishes = []
        for days_left in starting_days_until_spawns:
            self.add(days_left, 1)

    def add(self, starting_days_until_spawn: int, count: int):
        matches = [f for f in self.fishes if f.days_until_spawn == starting_days_until_spawn]
        if matches:
            matches[0].num_members += 1
        else:
            new_fish = Fish(starting_days_until_spawn, count)
            self.fishes.append(new_fish)

    def update(self):
        self.day += 1
        num_to_spawn = sum(fish.update() for fish in self.fishes)
        if num_to_spawn:
            self.add(8, num_to_spawn)
        print(f'Day {self.day}, spawning {num_to_spawn:,}, count: {sum(f.num_members for f in self.fishes):,}, cycle groups: {len(self.fishes)}')
        print(self.fishes)

def solve():
    def print_days(fishes):
        print(len(fishes), ','.join(str(fish.days_until_spawn) for fish in fishes))
    pop = FishPopulation(starting_days_until_spawns)
    print_days(pop.fishes)
    for n in range(256):
        pop.update()
    return

print(solve())
