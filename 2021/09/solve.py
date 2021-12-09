#!/usr/bin/env python
# https://adventofcode.com/2021/day/9

from math import prod
from collections import deque


def get_data():
    grid = [[9]+[int(n) for n in line.strip()]+[9]
            for line in open("input.txt")]
    grid.insert(0, [9]*len(grid[0]))
    grid.append([9]*len(grid[0]))
    return grid


def part1(grid):
    low_points = []
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            adjacent_points = [
                grid[y-1][x], grid[y][x+1],
                grid[y+1][x], grid[y][x-1]]
            if grid[y][x] < min(adjacent_points):
                low_points.append(grid[y][x])
    return sum([n + 1 for n in low_points])


def part2(grid):
    basins_sizes = []
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            size = 0
            q = deque([(x, y)])
            while q:
                x, y = q.popleft()
                if grid[y][x] == 9:
                    continue
                size += 1
                grid[y][x] = 9
                for d in directions:
                    new_x = x + d[0]
                    new_y = y + d[1]
                    if grid[new_y][new_x] < 9:
                        q.append((new_x, new_y))
            basins_sizes.append(size)

    return prod(sorted(basins_sizes, reverse=True)[:3])


print(part1(get_data()))
print(part2(get_data()))
