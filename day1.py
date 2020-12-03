#!/usr/bin/env python


def get_input():
    with open("inputs/day1.txt") as reader:
        return [int(i) for i in reader.readlines()]


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


input = get_input()
print(part1(input))
print(part2(input))
