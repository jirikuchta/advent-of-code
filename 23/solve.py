#!/usr/bin/env python3
# https://adventofcode.com/2020/day/23

from functools import reduce


def parse_input():
    return [int(n) for n in open("input.txt").read() if n.strip()]


def play(cups, moves):
    curr_cup = cups[0]

    for i in range(0, moves):
        picks = [cups.pop((cups.index(curr_cup) + 1) % len(cups)) for p in range(0, 3)]

        if any(map(lambda c: c < curr_cup, cups)):
            dest_cup = max([c for c in cups if c < curr_cup])
        else:
            dest_cup = max(cups)

        dest_cup_i = cups.index(dest_cup)
        cups = cups[:dest_cup_i + 1] + picks + cups[dest_cup_i + 1:]
        curr_cup = cups[(cups.index(curr_cup) + 1) % len(cups)]

    return cups


def part1(moves):
    cups = parse_input()
    r = play(cups, moves)
    return reduce(lambda a, b: a + str(b), r[r.index(1) + 1:] + r[:r.index(1)], "")


# def part2(moves):
#     cups = parse_input()
#     cups += cups + list(range(max(cups) + 1, 1000000+1))
#     r = play(cups, moves)
#     return r[r.index(1) + 1] * r[r.index(1) + 2]


print(f"Part 1: {part1(100)}")
# print(f"Part 2: {part2(10000000)}")
