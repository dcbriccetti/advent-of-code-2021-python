from pathlib import Path

horz_positions: list[int] = list(map(int,
    Path('../data/7.txt').read_text().rstrip().split(',')))

def linear_cost(n: int):
    return n

def triangular_cost(n: int):
    return (n * (n + 1)) // 2

def cost(pos: int, fn):
    return sum(fn(abs(pos - hp)) for hp in horz_positions)

def solve():
    horz_positions.sort()
    median = horz_positions[len(horz_positions) // 2]
    print(f'{median=}, mean={sum(horz_positions) // len(horz_positions)}')
    print(f'Part 1: ({cost(median, triangular_cost)}, {median})')
    print(f'Part 2: {min((cost(n, triangular_cost), n) for n in range(min(horz_positions), max(horz_positions)))}')

print(solve())
