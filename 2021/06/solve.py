#!/usr/bin/env python
# https://adventofcode.com/2021/day/6


def count(rounds):
    data = [int(n) for n in open("input.txt").read().split(",")]
    numbers = [data.count(i) for i in range(9)]

    for i in range(rounds):
        growth = numbers.pop(0)
        numbers[6] += growth
        numbers.append(growth)

    return sum(numbers)


print(count(80))
print(count(256))
