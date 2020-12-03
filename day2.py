#!/usr/bin/env python
# https://adventofcode.com/2020/day/2

import re


def get_input():
    return (re.split("-| |: ", line) for line in open("inputs/day2.txt"))


def part1(min, max, letter, password):
    return int(min) <= password.count(letter) <= int(max)


def part2(pos1, pos2, letter, password):
    return [password[int(pos1)-1], password[int(pos2)-1]].count(letter) == 1


print([part1(*data) for data in get_input()].count(True))
print([part2(*data) for data in get_input()].count(True))
