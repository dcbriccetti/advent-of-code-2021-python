from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

starting_days_until_spawns: list[int] = list(map(int,
    Path('../data/6.txt').read_text().rstrip().split(',')))

@dataclass
class FishCycleGroup:
    'All fish at the same point in the days_until_spawn cycle'
    days_until_spawn: int
    num_members: int

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
    cycle_groups: list[FishCycleGroup]
    day: int = 0

    def __init__(self, starting_days_until_spawns: Iterable[int]):
        self.cycle_groups = []
        for days_left in starting_days_until_spawns:
            self.add(days_left, 1)

    def add(self, starting_days_until_spawn: int, count: int):
        if matches := [f for f in self.cycle_groups
                       if f.days_until_spawn == starting_days_until_spawn]:
            matches[0].num_members += 1
        else:
            self.cycle_groups.append(FishCycleGroup(starting_days_until_spawn, count))

    def update(self):
        self.day += 1
        num_to_spawn = sum(fish.update() for fish in self.cycle_groups)
        if num_to_spawn:
            self.add(8, num_to_spawn)
        print(f'Day {self.day}, spawning {num_to_spawn:,}, count: {sum(f.num_members for f in self.cycle_groups):,}, cycle groups: {len(self.cycle_groups)}')
        print(self.cycle_groups)

def solve():
    pop = FishPopulation(starting_days_until_spawns)
    for n in range(256):
        pop.update()
    return

print(solve())
