from pathlib import Path

starting_days_until_spawns: list[int] = list(map(int,
    Path('../data/6.txt').read_text().rstrip().split(',')))

class Fish:
    days_until_spawn: int

    def __init__(self, days_until_spawn: int):
        self.days_until_spawn = days_until_spawn

    def update(self) -> bool:
        if self.days_until_spawn == 0:
            self.days_until_spawn = 6
            return True
        self.days_until_spawn -= 1
        return False

def part1():
    def print_days(fishes):
        print(len(fishes), ','.join(str(fish.days_until_spawn) for fish in fishes))
    fishes = [Fish(days_left) for days_left in starting_days_until_spawns]
    print_days(fishes)
    for n in range(256):
        num_to_spawn = sum(fish.update() for fish in fishes)
        fishes.extend(Fish(8) for _ in range(num_to_spawn))
        print(f'Day {n + 1}, spawning {num_to_spawn:,}, count: {len(fishes):,}')
    return

def part2():
    return

print(part1(), part2())
