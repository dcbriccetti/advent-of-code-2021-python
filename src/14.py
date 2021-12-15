from collections import Counter
from io import StringIO
from itertools import pairwise

from helpers import lines

polymer, rules_lines = lines('../data/14.txt', sep='\n\n')
rules = dict([tuple(line.split(' -> ')) for line in rules_lines.split('\n')])
print(polymer, rules)

def process_polymer(iterations: int) -> int:
    growing_polymer = str(polymer)  # copy from module scope

    for i in range(1, iterations + 1):
        next_polymer = StringIO()
        next_polymer.write(growing_polymer[0])

        for left, right in pairwise(growing_polymer):
            if insertion := rules.get(left + right):
                next_polymer.write(insertion)
            next_polymer.write(right)

        growing_polymer = next_polymer.getvalue()
        print(i, len(growing_polymer))

    counts = [count for _, count in Counter(growing_polymer).items()]
    counts.sort()
    return counts[-1] - counts[0]

print(process_polymer(10))
# too slow   print(process_polymer(40))
