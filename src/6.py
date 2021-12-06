from pathlib import Path

input_lines: list[int] = list(map(int, Path('../data/6_test.txt').read_text().rstrip().split(',')))

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
    fishes = [Fish(days_left) for days_left in input_lines]
    print_days(fishes)
    for n in range(80):
        num_to_spawn = 0
        print(f'Day {n + 1}')
        for fish in fishes:
            if fish.update():
                num_to_spawn += 1
        new_fishes = [Fish(8) for _ in range(num_to_spawn)]
        print(f'Spawning {len(new_fishes)}')
        fishes.extend(new_fishes)
        print_days(fishes)
    return

def part2():
    return

print(part1(), part2())
