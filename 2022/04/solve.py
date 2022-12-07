#!/usr/bin/env python
# https://adventofcode.com/2022/day/4


def get_data():
    return [[list(map(lambda x: int(x), range.split("-")))
            for range in line.split(",")]
            for line in open("input.txt")]


def fully_overlaps(pair):
    return ((pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]) or
            (pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]))


def partially_overlaps(pair):
    return not ((pair[0][0] > pair[1][1] or pair[0][1] < pair[1][0]) and
                (pair[1][0] > pair[0][1] or pair[1][1] < pair[0][0]))


def part1(data):
    return [fully_overlaps(pair) for pair in data].count(True)


def part2(data):
    return [partially_overlaps(pair) for pair in data].count(True)


print(part1(get_data()))
print(part2(get_data()))
