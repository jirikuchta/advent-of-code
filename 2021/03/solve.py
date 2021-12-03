#!/usr/bin/env python
# https://adventofcode.com/2021/day/3

from collections import Counter


def get_data():
    return [ln.strip() for ln in open("input.txt")]


def part1(mode):
    data = get_data()
    counters = [Counter([i[pos] for i in data])
                for pos in range(0, len(data[0]))]
    res = [c.most_common()[0 if mode == "gamma" else -1][0] for c in counters]
    return int("".join(res), 2)


def part2(mode):
    data = get_data()

    for pos in range(0, len(data[0])):
        if len(data) == 1:
            break

        c = Counter([ln[pos] for ln in data])

        char = "0" if mode == "co2" else "1"
        if c.most_common()[0][1] != c.most_common()[-1][1]:
            char = c.most_common()[-1 if mode == "co2" else 0][0]

        data = list(filter(lambda i: i[pos] == char, data))

    return int(data[0], 2)


print(part1("gamma") * part1("epsilon"))
print(part2("oxygen") * part2("co2"))
