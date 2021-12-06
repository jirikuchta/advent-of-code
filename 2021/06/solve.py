#!/usr/bin/env python
# https://adventofcode.com/2021/day/6


def count(rounds):
    data = [int(n) for n in open("input.txt").read().split(",")]
    counts = [data.count(i) for i in range(9)]

    for i in range(rounds):
        growth = counts.pop(0)
        counts[6] += growth
        counts.append(growth)

    return sum(counts)


print(count(80))
print(count(256))
