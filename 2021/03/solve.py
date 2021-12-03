#!/usr/bin/env python
# https://adventofcode.com/2021/day/3

from collections import Counter
from functools import reduce


def get_data():
    return [ln.strip() for ln in open("input.txt")]


def part1(data):
    data = [Counter(map(lambda ln: ln[pos], data))
            for pos in range(0, len(data[0]))]
    gamma = reduce(lambda a, b: a + b.most_common()[0][0], data, "")
    epsilon = reduce(lambda a, b: a + b.most_common()[-1][0], data, "")
    return int(gamma, 2) * int(epsilon, 2)


def part2(data, mode):
    for pos in range(0, len(data[0])):
        if len(data) == 1:
            break

        c = Counter(map(lambda i: i[pos], data))

        char = "0" if mode == "co2" else "1"
        if c.most_common()[0][1] != c.most_common()[-1][1]:
            char = c.most_common()[-1 if mode == "co2" else 0][0]

        data = list(filter(lambda i: i[pos] == char, data))

    return int(data[0], 2)


print(part1(get_data()))
print(part2(get_data(), "oxygen") * part2(get_data(), "co2"))
