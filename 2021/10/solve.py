#!/usr/bin/env python
# https://adventofcode.com/2021/day/10

from collections import deque
from statistics import median


def get_data():
    return [line.strip() for line in open("input.txt")]


OPENING = "([{<"
CLOSING = ")]}>"


def get_missing_brackets(line):
    q = deque()
    for char in line:
        if char in OPENING:
            q.append(char)
            continue

        if char != CLOSING[OPENING.index(q.pop())]:
            raise SyntaxError(char)

    q.reverse()
    return "".join([CLOSING[OPENING.index(i)] for i in q])


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
