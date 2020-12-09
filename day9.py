#!/usr/bin/env python
# https://adventofcode.com/2020/day/8

from itertools import combinations


def get_data():
    return [int(line) for line in open("inputs/day9.txt").readlines()]


def part1():
    preamble = 25
    data = get_data()
    for i, n in enumerate(data[preamble:], preamble):
        if all([sum(c) != n for c in combinations(data[i - preamble:i], 2)]):
            return n


def part2():
    data = get_data()
    part1_res = part1()

    for i in range(len(data)):
        r = 2
        while r < len(data):
            seq = data[i:i+r]
            if sum(seq) == part1_res:
                return min(seq) + max(seq)
            r += 1


print(part1())
print(part2())
