#!/usr/bin/env python3
# https://adventofcode.com/2020/day/17

from itertools import product
from copy import deepcopy


def expand_grid(grid, withW):
    size_y = len(grid[0][0])
    size_z = len(grid[0][0][0])

    def y():
        return [z() for i in range(0, size_y)]

    def z():
        return [False for i in range(0, size_z)]

    grid.insert(0, [y() for i in range(0, len(grid[0]))])
    grid.append([y() for i in range(0, len(grid[0]))])

    for x in grid:
        x.insert(0, y())
        x.append(y())

    for x in grid:
        for y in x:
            y.insert(0, z())
            y.append(z())

    if withW:
        for x in grid:
            for y in x:
                for z in y:
                    z.insert(0, False)
                    z.append(False)


def get_cube_state(x, y, z, w, grid):
    active = grid[x][y][z][w]
    active_neighbors = -1 if active else 0

    x_i = filter(lambda i: i > -1, [x-1, x, x+1])
    y_i = filter(lambda i: i > -1, [y-1, y, y+1])
    z_i = filter(lambda i: i > -1, [z-1, z, z+1])
    w_i = filter(lambda i: i > -1, [w-1, w, w+1])

    for p in product(x_i, y_i, z_i, w_i):
        try:
            active_neighbors += 1 if grid[p[0]][p[1]][p[2]][p[3]] else 0
        except IndexError:
            pass

    if active and active_neighbors not in (2, 3):
        return False

    if not active and active_neighbors == 3:
        return True

    return active


def count(cycles, withW):
    grid = [[[[ch == "#"]] for ch in line.strip()]
            for line in open("input.txt").readlines()]

    for i in range(0, cycles):
        expand_grid(grid, withW)

        grid_copy = deepcopy(grid)
        range_xy = range(0, len(grid))
        range_z = range(0, len(grid[0][0]))
        range_w = range(0, len(grid[0][0][0]))

        for p in product(range_xy, range_xy, range_z, range_w):
            grid[p[0]][p[1]][p[2]][p[3]] = get_cube_state(*p, grid_copy)

    result = 0

    for x in grid:
        for y in x:
            for z in y:
                result += z.count(True)

    return result


print(f"Part 1: {count(6, False)}")
print(f"Part 2: {count(6, True)}")
