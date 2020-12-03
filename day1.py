#!/usr/bin/env python
# https://adventofcode.com/2020/day/1


def get_input():
    return [int(line) for line in open("inputs/day1.txt")]


def part1(numbers):
    for i, n1 in enumerate(numbers):
        for n2 in numbers[i+1:]:
            if n1+n2 == 2020:
                return n1*n2


def part2(numbers):
    for i, n1 in enumerate(numbers):
        for i2, n2 in enumerate(numbers[i+1:]):
            for n3 in numbers[i2+1:]:
                if n1+n2+n3 == 2020:
                    return n1*n2*n3


print(part1(get_input()))
print(part2(get_input()))
