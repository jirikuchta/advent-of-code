#!/usr/bin/env python
# https://adventofcode.com/2021/day/14

from collections import Counter


data = [line.strip() for line in open("input.txt")]
tpl = data[0]
rules = {rule[:2]: rule[-1] for rule in data[2:]}


def expand(steps):
    c = Counter([tpl[i:i+2] for i in range(len(tpl[:-1]))])

    for i in range(steps):
        for pair, count in list(c.items()):
            c[pair[0] + rules[pair]] += count
            c[rules[pair] + pair[1]] += count
            c[pair] -= count

    return c


def count(counter):
    c = Counter()

    for pair, count in counter.items():
        c.update({pair[0]: count})
    c.update(tpl[-1])

    counts = sorted(c.values())
    return (counts[-1] - counts[0])


print(f"Part1: {count(expand(10))}")
print(f"Part2: {count(expand(40))}")
