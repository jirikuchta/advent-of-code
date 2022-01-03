#!/usr/bin/env python
# https://adventofcode.com/2021/day/17

import re
from itertools import product


area_min_x, area_max_x, area_min_y, area_max_y = \
    map(int, re.findall(r"(-?\d+)", open("input.txt").read()))


def hit(x, y):
    return area_min_x <= x <= area_max_x \
       and area_min_y <= y <= area_max_y


def overshot(x, y):
    return x > area_max_x \
        or y < area_min_y


velocities = product(range(-200, 200), repeat=2)
hit_velocities = []
max_y = 0

for v in velocities:
    move = (v[0], v[1])
    pos = (v[0], v[1])
    v_max_y = 0

    while True:
        if hit(*pos):
            hit_velocities.append(v)
            max_y = max(max_y, v_max_y)
            break

        if overshot(*pos):
            break

        move = (max(move[0] - 1, 0), move[1] - 1)
        pos = (pos[0] + move[0], pos[1] + move[1])
        v_max_y = max(v_max_y, pos[1])


print(f"Part1: {max_y}")
print(f"Part2: {len(hit_velocities)}")
