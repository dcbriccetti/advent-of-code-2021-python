from itertools import chain

import helpers

def unique_pattern(code: str):
    return len(code) in [2, 3, 4, 7]

lines: list[str] = helpers.lines('../data/8.txt')
data: list[tuple[str, str]] = [(left, right) for left, right in [line.split(' | ') for line in lines]]
print(sum(1 for _ in chain(*(filter(unique_pattern, output_values.split()) for _, output_values in data))))
