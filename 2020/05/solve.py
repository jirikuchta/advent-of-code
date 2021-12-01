#!/usr/bin/env python
# https://adventofcode.com/2020/day/5

import math


def get_input():
    return ((line[:7], line[7:].strip()) for line in open("input.txt"))


def count(input, max):
    min = 0
    for char in input:
        if char in ("F", "L"):
            max = min + ((max - min) // 2)
        if char in ("B", "R"):
            min = math.ceil(min + ((max - min) / 2))
    return min


def part1():
    result = 0

    for item in get_input():
        row = count(item[0], 127)
        column = count(item[1], 7)
        result = max(row * 8 + column, result)

    return result


def part2():
    seats_grid = [[False] * 8 for i in range(128)]
    seats_ids = []

    for item in get_input():
        row = count(item[0], 127)
        column = count(item[1], 7)
        seats_grid[row][column] = True
        seats_ids.append(row * 8 + column)

    for i, row in enumerate(seats_grid):
        for j, taken in enumerate(row):
            if not taken:
                id = i * 8 + j
                if id + 1 in seats_ids and id - 1 in seats_ids:
                    return id


print(part1())
print(part2())
