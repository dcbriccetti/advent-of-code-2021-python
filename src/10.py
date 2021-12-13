from collections import deque
from typing import Iterator
import helpers

# Though I normally intend “bracket” to mean “square bracket”, here
# "bracket" means a parenthesis, square bracket, curly brace, or angle bracket.
open_brackets  = '([{<'
close_brackets = ')]}>'
lines = helpers.lines('../data/10.txt')

def first_error_in_line(line: str) -> None | str:
    'Return the first error in the given line, or None if there are no errors'

    def is_valid_bracket_pair(open_bracket: str, close_bracket: str) -> bool:
        open_bracket_index = open_brackets.index(open_bracket)
        expected_close_bracket = close_brackets[open_bracket_index]
        return close_bracket == expected_close_bracket

    open_brackets_stack = deque()

    for bracket in line:
        if bracket in open_brackets:
            open_brackets_stack.append(bracket)
        else:
            expected_open_bracket = open_brackets_stack.pop()
            if not is_valid_bracket_pair(expected_open_bracket, bracket):
                return bracket
    return None

def part1():
    illegal_bracket_points = [3, 57, 1197, 25137]

    def syntax_error_points() -> Iterator[int]:
        for line in lines:
            if bracket := first_error_in_line(line):
                point_index = close_brackets.index(bracket)
                yield illegal_bracket_points[point_index]

    print('Total syntax error score:', sum(syntax_error_points()))

def part2():
    points = [1, 2, 3, 4]

    def incompletes() -> Iterator[str]:
        return filter(lambda line: not first_error_in_line(line), lines)

    def repair_value(incomplete: str) -> int:
        def open_brackets_needing_closing(incomplete) -> str:
            open_bracket_stack = deque()
            for bracket in incomplete:
                if bracket in open_brackets:
                    open_bracket_stack.append(bracket)
                else:
                    open_bracket_stack.pop()
            return ''.join(reversed(open_bracket_stack))

        total = 0
        for bracket in open_brackets_needing_closing(incomplete):
            total = total * 5 + points[open_brackets.index(bracket)]
        return total

    completion_string_scores = list(map(repair_value, incompletes()))
    completion_string_scores.sort()
    median = completion_string_scores[len(completion_string_scores) // 2]
    print('Middle score:', median)

part1()
part2()
