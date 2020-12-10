#!/usr/bin/env python
# https://adventofcode.com/2020/day/10


def get_data():
    data = sorted([int(l) for l in open("inputs/day10.txt").readlines()])
    return [0] + data + [(data[-1] + 3)]


def part1():
    data = get_data()
    by_one, by_three = 0, 0
    for a, b in zip(data, data[1:]):
        by_one += 1 if b - a == 1 else 0
        by_three += 1 if b - a == 3 else 0
    return by_one * by_three


def part2():
    data = get_data()

    subresults = [1] + [0 for x in range(len(data) - 1)]

    for i, nr in enumerate(data):
        for y in range(1, 4):
            if data[i] + y in data:
                subresults[data.index(nr + y)] += subresults[i]

    return subresults[-1]


print(part1())
print(part2())
