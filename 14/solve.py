#!/usr/bin/env python3
# https://adventofcode.com/2020/day/14


def part1():
    mem = {}
    mask = None

    for line in open("input.txt").readlines():
        if line.startswith("mask"):
            mask = [ch for ch in line[6:].strip()][::-1]

        if line.startswith("mem"):
            bit = int(line[4:line.index("]")])
            value = int(line.split("=")[1].strip())

            for i, ch in enumerate(mask):
                if ch == "1":
                    value = value | (1 << i)

                if ch == "0":
                    value = value & ~(1 << i)

            mem[bit] = value

    return sum(mem.values())


print(f"Part 1: {part1()}")
