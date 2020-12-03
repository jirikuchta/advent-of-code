#!/usr/bin/env python
# https://adventofcode.com/2020/day/3

from functools import reduce


def count(move_x, move_y):
    x, i, result = 0, 0, 0
    grid = ([char == "#" for char in line.strip()]
            for line in open("inputs/day3.txt"))

    for line in grid:
        if i % move_y == 0:
            result += 1 if line[x % len(line)] else 0
            x += move_x
        i += 1

    return result


print(count(3, 1))
print(reduce(lambda a, b: a*count(*b), [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]], 1))
