#!/usr/bin/env python
# https://adventofcode.com/2021/day/1


def get_data():
    return [line.split() for line in open("input.txt")]


def part1(data):
    return sum(map(lambda a, b: b > a, data, data[1:]))


def part2(data):
    groups = map(lambda i: data[i:i+3], range(0, len(data)))
    sums = [sum(g) for g in groups if len(g) == 3]
    return part1(sums)


print(part1(get_data()))
print(part2(get_data()))
