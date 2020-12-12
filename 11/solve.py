#!/usr/bin/env python
# https://adventofcode.com/2020/day/11

from functools import reduce
from copy import deepcopy


def count(max_seats_occupied, max_visibility):
    data = [[False if ch == "L" else None for ch in l.strip()]
            for l in open("input.txt").readlines()]

    def search_direction(start_row, start_col, move_row, move_col):
        distance = 0

        while True:
            distance += 1
            row = start_row + move_row * distance
            col = start_col + move_col * distance

            if row < 0 or col < 0:
                return False

            try:
                if data[row][col] is not None:
                    return data[row][col]
            except IndexError:
                return False

            if max_visibility is not None and max_visibility == distance:
                return False

    while True:
        changed = False
        new_state = deepcopy(data)

        for row in range(len(data)):
            for col in range(len(data[row])):

                if data[row][col] is None:
                    continue

                visible_seats = [
                    search_direction(row, col, -1, 0),
                    search_direction(row, col, -1, 1),
                    search_direction(row, col, 0, 1),
                    search_direction(row, col, 1, 1),
                    search_direction(row, col, 1, 0),
                    search_direction(row, col, 1, -1),
                    search_direction(row, col, 0, -1),
                    search_direction(row, col, -1, -1)]

                if data[row][col] is False and visible_seats.count(True) == 0:
                    new_state[row][col] = True
                elif visible_seats.count(True) > max_seats_occupied:
                    new_state[row][col] = False

                if new_state[row][col] != data[row][col]:
                    changed = True

        data = new_state

        if not changed:
            return reduce(lambda a, b: a + b.count(True), data, 0)


print(f"Part 1: {count(3, 1)}")
print(f"Part 2: {count(4, None)}")
