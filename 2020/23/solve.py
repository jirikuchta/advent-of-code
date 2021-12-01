#!/usr/bin/env python3
# https://adventofcode.com/2020/day/23


# Pff, this one was hard to make it finish in reasonable time.
# Little bit messy but done under 30s.


def parse_input():
    cups = open("input.txt").read().strip()
    return {int(cups[i]): int(cups[(i + 1) % len(cups)])
            for i, _ in enumerate(cups)}, int(cups[0]), int(cups[-1])


def play(cups, cup, moves):
    max_cup = len(cups.keys())

    for i in range(0, moves):
        picks = [cups[cup], cups[cups[cup]], cups[cups[cups[cup]]]]

        try:
            dest_cup = max(filter(lambda c: c not in picks and c > 0,
                                  [cup - i for i in range(1, 5)]))
        except ValueError:
            dest_cup = max(filter(lambda c: c not in picks and c != cup and c > 0,
                                  [max_cup - i for i in range(0, 4)]))

        cups[cup] = cups[picks[2]]
        cups[picks[2]] = cups[dest_cup]
        cups[picks[1]] = picks[2]
        cups[picks[0]] = picks[1]
        cups[dest_cup] = picks[0]

        cup = cups[cup]

    return cups


def part1(moves):
    cups, first_cup, last_cup = parse_input()
    r = play(cups, first_cup, moves)

    result = ""
    i = 1
    while True:
        result += str(r[i])
        i = r[i]
        if i == 1:
            return result


def part2(moves):
    cups, first_cup, last_cup = parse_input()
    max_cup = max(cups.keys())

    for i in range(max_cup + 1, 1000000):
        cups[i] = i + 1
    cups[last_cup] = max_cup + 1
    cups[1000000] = first_cup

    r = play(cups, first_cup, moves)

    return r[1], r[r[1]], r[1] * r[r[1]]


print(f"Part 1: {part1(100)}")
print(f"Part 2: {part2(10000000)}")
