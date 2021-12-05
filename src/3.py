from pathlib import Path
from typing import Sequence

nums: list[str] = Path('data/3.txt').read_text().rstrip().split('\n')
num_cols = len(nums[0])

def most_digits(nums: Sequence[str], pos: int) -> str:
    bit_counts = sum(int(num[pos]) for num in nums)
    return '1' if bit_counts > len(nums) / 2 else '0'

def part1():
    digits = ''.join((most_digits(nums, bit_index)) for bit_index in range(num_cols))
    gamma_rate = int(digits, 2)
    flipped_digits: str = ''.join(('0' if digit == '1' else '1' for digit in digits))
    epsilon_rate = int(flipped_digits, 2)
    return gamma_rate * epsilon_rate

def part2():
    return 0

print(part1())
