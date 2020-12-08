#!/usr/bin/env python
# https://adventofcode.com/2020/day/8

from functools import reduce


def get_data():
    return [line.strip().split(" ")
            for line in open("inputs/day8.txt").readlines()]


def part1():
    data = get_data()
    i = 0

    while data[i]:
        cmd, value = data[i]
        yield int(value) if cmd == "acc" else 0
        data[i] = None
        i += int(value) if cmd == "jmp" else 1


def part2():
    return []


def walk(generator):
    return reduce(lambda a, b: a + b, generator(), 0)


print(walk(part1))
print(walk(part2))
