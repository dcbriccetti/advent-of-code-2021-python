from pathlib import Path
from itertools import pairwise
from typing import Iterator

def part1() -> int:
    return num_increases(get_numbers())

def part2() -> int:
    return num_increases(sums_of_3())

def num_increases(numbers: Iterator[int]) -> int:
    'Return the number of times the values in numbers increases'
    increases = (b > a for a, b in pairwise(numbers))
    return sum(increases)

def sums_of_3() -> Iterator[int]:
    'Return the sum of each triple of consecutive values'
    numbers = list(get_numbers())
    return (sum(numbers[i-2:i+1]) for i in range(2, len(numbers)))

def get_numbers() -> Iterator[int]:
    lines = Path('data/1.txt').read_text().rstrip().split('\n')
    return (int(line) for line in lines)

print(part1(), part2())
