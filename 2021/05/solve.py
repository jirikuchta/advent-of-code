#!/usr/bin/env python
# https://adventofcode.com/2021/day/5

from collections import Counter


def get_data(exclude_diagoval):
    data = [[[int(n) for n in i.split(",")] for i in ln.split("->")]
            for ln in open("input.txt")]

    if exclude_diagoval:
        data = list(filter(
            lambda i: i[0][0] == i[1][0] or i[0][1] == i[1][1], data))

    return data


def expand_line(line):
    start_x, end_x = [line[0][0], line[1][0]]
    start_y, end_y = [line[0][1], line[1][1]]
    step_x = step_y = 1

    if start_x > end_x:
        step_x = -1
        end_x -= 1
    else:
        end_x += 1

    if start_y > end_y:
        step_y = -1
        end_y -= 1
    else:
        end_y += 1

    xr = range(start_x, end_x, step_x)
    yr = range(start_y, end_y, step_y)

    return [[
        xr[i] if len(xr) > i else xr[0],
        yr[i] if len(yr) > i else yr[0]
    ] for i in range(max(len(xr), len(yr)))]


def count_overlaps(data):
    lines = [expand_line(ln) for ln in data]
    c = Counter([complex(point[0], point[1])
                for line in lines for point in line])
    return len(list(filter(lambda i: i > 1, c.values())))


print(f"Part 1: {count_overlaps(get_data(True))}")
print(f"Part 2: {count_overlaps(get_data(False))}")
