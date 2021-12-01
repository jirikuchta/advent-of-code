#!/usr/bin/env python3
# https://adventofcode.com/2020/day/15


def count(turns):
    history = {}
    turn = 0
    last_number = None

    def add_number(n):
        nonlocal history, turn, last_number
        if n not in history:
            history[n] = []
        history[n].append(turn)
        last_number = n
        turn += 1

    for n in open("input.txt").read().split(","):
        add_number(int(n))

    while turn < turns:
        if len(history[last_number]) > 1:
            add_number(turn - history[last_number][-2] - 1)
        else:
            add_number(0)

    return last_number


print(f"Part 1: {count(2020)}")
print(f"Part 2: {count(30000000)}")
