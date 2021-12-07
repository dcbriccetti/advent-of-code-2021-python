from pathlib import Path

horz_positions: list[int] = list(map(int,
    Path('../data/7.txt').read_text().rstrip().split(',')))

def linear_cost(n: int) -> int:
    return n

def triangular_cost(n: int) -> int:
    return (n * (n + 1)) // 2

def cost(pos: int, fn) -> int:
    return sum(fn(abs(pos - hp)) for hp in horz_positions)

def solve():
    horz_positions.sort()
    median = horz_positions[len(horz_positions) // 2]
    mean = sum(horz_positions) // len(horz_positions)
    print(f'{median=}, {mean=}')

    print(f'Part 1: Position: {median}, Cost: {cost(median, linear_cost)}')

    full_range = range(min(horz_positions), max(horz_positions))
    total_cost, position = min((cost(n, triangular_cost), n) for n in full_range)
    print(f'Part 2: Position: {position}, Cost: {total_cost}')

print(solve())
