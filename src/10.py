from collections import deque
from pathlib import Path
from typing import Iterator

opens  = '([{<'
closes = ')]}>'
points = [[3, 57, 1197, 25137], [1, 2, 3, 4]]
lines: list[str] = Path('../data/10.txt').read_text().strip().split('\n')
stack = deque()

def is_pair(delim1: str, delim2: str) -> bool:
    expected_close = closes[opens.index(delim1)]
    return delim2 == expected_close

def error_in_line(line: str) -> None | str:
    for ch in line:
        if ch in closes:
            if not is_pair(stack.pop(), ch):
                return ch
        else:
            stack.append(ch)
    return None

def find_error_points() -> Iterator[int]:
    for line in lines:
        stack.clear()
        if ch := error_in_line(line):
            yield points[0][closes.index(ch)]

def incompletes() -> list[str]:
    return list(filter(lambda line: not error_in_line(line), lines))

print(sum(find_error_points()))


def repair_value(incomplete: str) -> int:
    total = 0
    stack.clear()
    for ch in incomplete:
        if ch in opens:
            stack.append(ch)
        else:
            stack.pop()
    while stack:
        ch = stack.pop()
        i = opens.index(ch)
        p = points[1][i]
        total *= 5
        total += p
    return total


in_points = [repair_value(incomplete) for incomplete in incompletes()]
in_points.sort()
median = in_points[len(in_points) // 2]
print(median)
