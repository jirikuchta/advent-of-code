#!/usr/bin/env python3
# https://adventofcode.com/…/14


def read_input():
    mask = None
    for line in open("input.txt").readlines():
        if line.startswith("mask"):
            mask = [ch for ch in line[6:].strip()][::-1]

        if line.startswith("mem"):
            bit = int(line[4:line.index("]")])
            value = int(line.split("=")[1].strip())
            yield mask, bit, value


def part1():
    mem = {}

    for mask, bit, value in read_input():
        for i, ch in enumerate(mask):
            if ch == "1":
                mem[bit] = value | (1 << i)

            if ch == "0":
                mem[bit] = value & ~(1 << i)

    return sum(mem.values())


def part2():
    mem = {}

    for mask, bit, value in read_input():
        for i, ch in enumerate(mask):
            if ch == "1":
                bit = bit | (1 << i)

        mem_bits = [bit]

        for i, ch in enumerate(mask):
            if ch == "X":
                tmp = []
                for mem_bit in mem_bits:
                    tmp.append(mem_bit | (1 << i))
                    tmp.append(mem_bit & ~(1 << i))
                mem_bits += tmp

        for mem_bit in set(mem_bits):
            mem[mem_bit] = value

    return sum(mem.values())


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
