#!/usr/bin/env python
# https://adventofcode.com/2021/day/12

from functools import cache
from copy import copy


@cache
def get_data():
    data = {}
    for line in open("input.txt"):
        start, end = line.strip().split("-")
        if start not in data:
            data[start] = set()
        if end not in data:
            data[end] = set()
        data[start].add(end)
        data[end].add(start)
    return data


def solve(path, part):
    data = get_data()
    paths = []

    for node in data.get(path[-1], set()):
        if node in path and node.upper() != node:
            if part == 1:
                continue

            if part == 2:
                if node == "start":
                    continue

                small_caves = [i for i in path if i.upper() != i]
                if any(small_caves.count(i) > 1 for i in small_caves):
                    continue

        cpath = copy(path)
        cpath.append(node)

        if node == "end":
            paths.append(cpath)
            continue

        paths += solve(cpath, part)

    return paths


print(f"Part1: {len(solve(['start'], 1))}")
print(f"Part2: {len(solve(['start'], 2))}")
