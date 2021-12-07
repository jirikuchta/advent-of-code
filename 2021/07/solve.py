#!/usr/bin/env python
# https://adventofcode.com/2021/day/7


def count(fn):
    data = [int(n) for n in open("input.txt").read().split(",")]
    return min([sum([fn(x, y) for y in data]) for x in range(max(data))])


print(count(lambda x, y: abs(x - y)))
print(count(lambda x, y: sum(range(abs(x - y) + 1))))
