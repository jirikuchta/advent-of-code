#!/usr/bin/env python3
# https://adventofcode.com/2020/day/13

from functools import reduce
from itertools import count


def parse_data():
    ts, buses = open("input.txt").read().strip().split("\n")
    return int(ts), [None if b == "x" else int(b) for b in buses.split(",")]


def part1():
    arrival_ts, buses = parse_data()
    departures = map(lambda b: (b * ((arrival_ts // b) + 1), b),
                     filter(lambda b: b, buses))
    d_ts, bus_id = reduce(lambda a, b: a if a[0] < b[0] else b, departures)
    return (d_ts - arrival_ts) * bus_id


def part2():
    # was not able to solve :/
    # https://en.wikipedia.org/wiki/Chinese_remainder_theorem was presumably
    # supposed to be applied here. However, it's not the only approach.
    # Some guy on the internet used this solution:
    ts, buses = parse_data()
    step = 1
    for i, bus_id in enumerate(buses):
        if bus_id is None:
            continue
        ts = next(c for c in count(ts, step) if (c + i) % bus_id == 0)
        step *= bus_id
    return ts


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
