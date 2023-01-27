#!/usr/bin/env python
# https://adventofcode.com/2022/day/11

from operator import iadd, imul
from math import floor


monkeys = []


class Monkey:

    def __init__(self, data):
        lines = [line.strip() for line in data.split("\n")]
        self._id = lines[0][7]
        self._items = [int(id) for id in lines[1][16:].split(",")]
        self._op = iadd if lines[2][21] == "+" else imul
        self._op_value = "old" if lines[2][23:] == "old" else int(lines[2][23:])
        self._factor = int(lines[3][19:])
        self._if_true = int(lines[4][25:])
        self._if_false = int(lines[5][26:])
        self._counter = 0

    def play(self):
        while len(self._items):
            self._pass(self._inspect())

    def add_item(self, item):
        self._items.append(item)

    def get_counter(self):
        return self._counter

    def _inspect(self):
        self._counter += 1
        item = self._items.pop(0)
        item = self._op(item, item if self._op_value == "old" else self._op_value)
        return floor(item / 3)

    def _pass(self, item):
        if item % self._factor == 0:
            monkeys[self._if_true].add_item(item)
        else:
            monkeys[self._if_false].add_item(item)


def init():
    global monkeys
    with open("input.txt") as file:
        monkeys = [Monkey(data) for data in file.read().split("\n\n")]


def part1(rounds):
    init()
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.play()

    return imul(*sorted([m.get_counter() for m in monkeys], reverse=True)[:2])


def part2():
    pass


print(part1(20))
print(part2())
