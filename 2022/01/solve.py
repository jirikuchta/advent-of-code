#!/usr/bin/env python
# https://adventofcode.com/2021/day/1


def get_data():
    with open("input.txt") as file:
        groups = file.read().strip().split("\n\n")
    return [list(map(lambda i: int(i), group.split())) for group in groups]


def part1(data):
    return max([sum(x) for x in data])


def part2(data):
    return sum(sorted([sum(x) for x in data])[-3:])


print(part1(get_data()))
print(part2(get_data()))
