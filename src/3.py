from pathlib import Path
from typing import Sequence

def more_ones_than_zeroes(nums: Sequence[str], bit_index: int) -> bool:
    "nums example: ['00100', '11110', '10110', ..., '01010']"
    num_one_bits = sum(int(num[bit_index]) for num in nums)
    num_zero_bits = len(nums) - num_one_bits
    return num_one_bits >= num_zero_bits

def b01(value: bool | int | str, reverse=False) -> str:
    "Convert “Truthy” to '0' or '1'"
    bool_value = bool(int(value)) if isinstance(value, str) else bool(value)
    maybe_reversed_value = not bool_value if reverse else bool_value
    return str(int(maybe_reversed_value))

nums: list[str] = Path('../data/3_test.txt').read_text().rstrip().split('\n')
num_cols = len(nums[0])

def part1():
    def most_common_digits(binary_strings: list[str]) -> str:
        "binary_strings example: ['00100', '11110', '10110', ..., '01010']"
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
        nums: list[str]
        most_common: bool
        result: None | int

        def __init__(self, nums: list[str], most_common: bool):
            self.nums = list(nums)
            self.most_common = most_common
            self.result = None

        def discard_non_matches(self, bit_index: int) -> None:
            '''Find the most (or least) common digit at bit_index
            and discard numbers not having that digit in that
            position. Once the search space shrinks to a single
            number, save that number as `result`.'''
            digit_to_match: str = b01(more_ones_than_zeroes(self.nums, bit_index),
                                      reverse=not self.most_common)
            self.nums = [num for num in self.nums
                         if num[bit_index] == digit_to_match]
            if len(self.nums) == 1:
                self.result = int(self.nums[0], 2)

    mrf = RatingFinder(nums, most_common=True)
    lrf = RatingFinder(nums, most_common=False)
    finders = [mrf, lrf]

    for bit_index in range(num_cols):
        for finder in finders:
            if not finder.result:
                finder.discard_non_matches(bit_index)
        if all(finder.result for finder in finders):
            break

    return mrf.result * lrf.result

print(part1(), part2())
