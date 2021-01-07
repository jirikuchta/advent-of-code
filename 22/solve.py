#!/usr/bin/env python3
# https://adventofcode.com/2020/day/22


def parse_input():
    return tuple([int(n) for n in p.split("\n")[1:] if n]
                 for p in open("input.txt").read().split("\n\n"))


def part1():
    p1, p2 = parse_input()

    while len(p1) and len(p2):
        p1_card = p1.pop(0)
        p2_card = p2.pop(0)

        if p1_card > p2_card:
            p1.append(p1_card)
            p1.append(p2_card)
        else:
            p2.append(p2_card)
            p2.append(p1_card)

    winners_deck = next(filter(lambda p: len(p) > 0, (p1, p2)))

    res = 0
    for i, card in enumerate(winners_deck):
        res += card * (len(winners_deck) - i)
    return res


print(f"Part 1: {part1()}")
