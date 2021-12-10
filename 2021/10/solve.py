#!/usr/bin/env python
# https://adventofcode.com/2021/day/10

from collections import deque
from statistics import median


def get_data():
    return [line.strip() for line in open("input.txt")]


BRACKETS = "([{<>}])"


def get_closing_bracket(opening_bracket):
    opening_bracket_i = BRACKETS.index(opening_bracket)
    return BRACKETS[-(opening_bracket_i + 1)]


def get_missing_brackets(line):
    q = deque()
    for char in line:
        if char in BRACKETS[:4]:
            q.append(char)
            continue

        if char != get_closing_bracket(q.pop()):
            raise SyntaxError(char)

    res = ""
    while q:
        res += get_closing_bracket(q.pop())
    return res


def part1(data):
    illegal_chars = ""
    for line in data:
        try:
            get_missing_brackets(line)
        except SyntaxError as e:
            illegal_chars += str(e)

    return sum([{")": 3, "]": 57, "}": 1197, ">": 25137}[char]
               for char in illegal_chars])


def part2(data):
    missing_brackets = []
    for line in data:
        try:
            missing_brackets.append("".join(get_missing_brackets(line)))
        except SyntaxError:
            pass

    scores = []
    for item in missing_brackets:
        score = 0
        for char in item:
            score = score * 5 + [")", "]", "}", ">"].index(char) + 1
        scores.append(score)

    return median(scores)


print(part1(get_data()))
print(part2(get_data()))
