from pathlib import Path
from typing import Sequence

def more_ones_than_zeroes(nums: Sequence[str], pos: int) -> bool:
    num_one_bits = sum(int(num[pos]) for num in nums)
    num_zero_bits = len(nums) - num_one_bits
    return num_one_bits >= num_zero_bits

def b01(value: bool | int | str, reverse=False) -> str:  # “Truthy” to '0' or '1'
    bool_value = bool(int(value)) if isinstance(value, str) else bool(value)
    maybe_reversed_value = not bool_value if reverse else bool_value
    return str(int(maybe_reversed_value))

nums: list[str] = Path('data/3.txt').read_text().rstrip().split('\n')
num_cols = len(nums[0])

def part1():
    def most_common_digits(binary_strings: list[str]) -> str:
        digits = (b01(more_ones_than_zeroes(binary_strings, bit_index))
                  for bit_index in range(num_cols))
        return ''.join(digits)

    mcd: str = most_common_digits(nums)
    least_common_digits: str = ''.join(b01(digit, reverse=True) for digit in mcd)
    gamma_rate = int(mcd, 2)
    epsilon_rate = int(least_common_digits, 2)
    return gamma_rate * epsilon_rate

def part2():
    class RatingFinder:
        def __init__(self, nums: list[str], most_common: bool):
            self.nums = list(nums)
            self.most_common = most_common
            self.result = None

        def find(self, bit_index: int):
            def find_digit(nums: list[str], digit: int, most_common: bool) -> str:
                m1: bool = more_ones_than_zeroes(nums, digit)
                return b01(m1 if most_common else not m1)  # '0' or '1' from bool

            digit: str = find_digit(self.nums, bit_index, self.most_common)
            self.nums = [num for num in self.nums if num[bit_index] == digit]
            if len(self.nums) == 1:
                self.result = int(self.nums[0], 2)
            return self.result

    mrf = RatingFinder(nums, most_common=True)
    lrf = RatingFinder(nums, most_common=False)
    finders = [mrf, lrf]

    for bit_index in range(num_cols):
        for finder in finders:
            if not finder.result:
                finder.find(bit_index)
        if all(finder.result for finder in finders):
            break

    return mrf.result * lrf.result

print(part1(), part2())
