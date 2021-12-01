#!/usr/bin/env python
# https://adventofcode.com/2021/day/1


def get_input():
    return [int(line) for line in open("input.txt")]


def part1(numbers):
    return sum(map(lambda a, b: b > a, numbers, numbers[1:]))


def part2(numbers):
    groups = map(lambda i: numbers[i:i+3], range(0, len(numbers)))
    sums = [sum(g) for g in groups if len(g) == 3]
    return part1(sums)


print(part1(get_input()))
print(part2(get_input()))
