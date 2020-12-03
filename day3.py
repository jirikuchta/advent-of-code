#!/usr/bin/env python

from functools import reduce


def get_input():
    with open("inputs/day3.txt") as reader:
        return reader.readlines()


grid = [[char == "#" for char in line.strip()] for line in get_input()]


def count(move_x, move_y):
    x = 0
    y = 0
    result = 0

    while y < len(grid):
        result += 1 if grid[y][x % len(grid[y])] else 0
        x += move_x
        y += move_y

    return result


print(f"Part 1: {count(3, 1)}")
print(f"Part 2: {reduce(lambda a,b: a*count(*b), [[1,1],[3,1],[5,1],[7,1],[1,2]], 1)}")
