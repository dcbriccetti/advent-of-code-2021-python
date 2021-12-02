from typing import Iterator, Tuple

Movement = Tuple[str, int]

def movements() -> Iterator[Movement]:
    with open('data/2.txt') as f:
        for line in f:
            cmd, arg = line.split()
            amount = int(arg)
            yield cmd, amount

def solve(aiming: bool) -> int:
    depth = 0
    horz_pos = 0
    aim = 0

    for cmd, amount in movements():
        match cmd:
            case 'forward':
                horz_pos += amount
                if aiming:
                    depth += aim * amount
            case 'up' if aiming:
                aim -= amount
            case 'up' if not aiming:
                depth -= amount
            case 'down' if aiming:
                aim += amount
            case 'down' if not aiming:
                depth += amount

    return depth * horz_pos

print(solve(aiming=False), solve(aiming=True))
