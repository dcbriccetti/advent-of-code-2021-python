from pathlib import Path

horz_positions: list[int] = list(map(int,
    Path('../data/7.txt').read_text().rstrip().split(',')))

def triangle(n: int):
    return (n * (n + 1)) // 2

def cost1(pos: int):
    return sum(abs(pos - hp) for hp in horz_positions)

def cost2(pos: int):
    return sum(triangle(abs(pos - hp)) for hp in horz_positions)

def solve():
    horz_positions.sort()
    median = horz_positions[len(horz_positions) // 2]
    print(f'{median=}, mean={sum(horz_positions) // len(horz_positions)}')
    print(f'Part 1: ({cost1(median)}, {median})')
    print('Part 2:', min((cost2(n), n) for n in range(min(horz_positions), max(horz_positions))))

print(solve())
