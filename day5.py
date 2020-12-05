#!/usr/bin/env python
# https://adventofcode.com/2020/day/5

import math


def get_input():
    return ((line[:7], line[7:].strip()) for line in open("inputs/day5.txt"))


def count(input, min, max):
    for char in input:
        if char in ("F", "L"):
            max = min + ((max - min) // 2)
        if char in ("B", "R"):
            min = math.ceil(min + ((max - min) / 2))
    return min


def part1():
    result = 0

    for item in get_input():
        row = count(item[0], 0, 127)
        column = count(item[1], 0, 7)
        result = max(row * 8 + column, result)

    return result


def part2():
    seats_grid = [[False] * 8 for i in range(128)]
    taken_seats_ids = []

    for item in get_input():
        row = count(item[0], 0, 127)
        column = count(item[1], 0, 7)
        seats_grid[row][column] = True
        taken_seats_ids.append(row * 8 + column)

    for i, row in enumerate(seats_grid):
        if all(row):
            continue

        for j, seat in enumerate(row):
            if seat:
                continue

            seat_id = i * 8 + j
            if seat_id + 1 in taken_seats_ids and seat_id - 1 in taken_seats_ids:
                return seat_id


print(part1())
print(part2())
