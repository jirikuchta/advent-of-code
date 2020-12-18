#!/usr/bin/env python3
# https://adventofcode.com/2020/day/17

from itertools import product
from copy import deepcopy


def expand_grid(grid):
    def create_y():
        return [False] * len(grid[0][0])

    grid.insert(0, [create_y() for i in range(0, len(grid[0]))])
    grid.append([create_y() for i in range(0, len(grid[0]))])

    for x in grid:
        x.insert(0, create_y())
        x.append(create_y())

    for x in grid:
        for y in x:
            y.insert(0, False)
            y.append(False)


def get_cube_state(x, y, z, grid):
    active = grid[x][y][z]
    active_neighbors = -1 if active else 0

    x_i = [x, x+1]
    if x > 0:
        x_i.append(x-1)
    y_i = [y, y+1]
    if y > 0:
        y_i.append(y-1)
    z_i = [z, z+1]
    if z > 0:
        z_i.append(z-1)

    for p in product(x_i, y_i, z_i):
        try:
            active_neighbors += 1 if grid[p[0]][p[1]][p[2]] else 0
        except IndexError:
            pass

    if active and active_neighbors not in (2, 3):
        return False

    if not active and active_neighbors == 3:
        return True

    return active


def count(cycles):
    grid = [[[ch == "#"] for ch in line.strip()]
            for line in open("input.txt").readlines()]

    for i in range(0, cycles):
        expand_grid(grid)

        grid_copy = deepcopy(grid)
        size = len(grid)
        size_z = len(grid[0][0])

        for p in product(range(0, size), range(0, size), range(0, size_z)):
            grid[p[0]][p[1]][p[2]] = get_cube_state(*p, grid_copy)

    c = 0
    for x in grid:
        for y in x:
            c += y.count(True)

    return c


print(f"Part 1: {count(6)}")
