#!/usr/bin/env python

import re


def get_input():
    with open("inputs/day2.txt") as reader:
        return reader.readlines()


def part1(min, max, letter, password):
    occurrences = password.count(letter)
    return occurrences >= int(min) and occurrences <= int(max)


def part2(pos1, pos2, letter, password):
    return [password[int(pos1)-1], password[int(pos2)-1]].count(letter) == 1


if __name__ == "__main__":
    input = [re.split("-| |: ", line) for line in get_input()]
    print([part1(*data) for data in input].count(True))
    print([part2(*data) for data in input].count(True))
