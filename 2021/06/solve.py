#!/usr/bin/env python
# https://adventofcode.com/2021/day/6

from collections import Counter


def count(rounds):
    c = Counter([int(n) for n in open("input.txt").read().split(",")])
    numbers = [c.get(i) or 0 for i in range(0, 9)]

    for i in range(rounds):
        growth = numbers.pop(0)
        numbers[6] += growth
        numbers.append(growth)

    return sum(numbers)


print(count(80))
print(count(256))
