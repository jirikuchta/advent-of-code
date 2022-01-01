#!/usr/bin/env python
# https://adventofcode.com/2021/day/18

import json
from functools import reduce
from itertools import permutations
from math import floor, ceil


def split(n):
    if n.children:
        for i in n.children:
            if split(i):
                return True

    v = n.value
    if isinstance(v, int) and v > 9:
        n.update([floor(v / 2), ceil(v / 2)])
        return True

    return False


def explode(n, d=0):
    ch = n.children

    if not ch:
        return False

    if any(map(lambda i: isinstance(i.value, list), ch)):
        for i in ch:
            if explode(i, d+1):
                return True
        return False

    if d < 4:
        return False

    left_sibling = numeral_sibling(n, "left")
    right_sibling = numeral_sibling(n, "right")

    if left_sibling:
        left_sibling.update(left_sibling.value + ch[0].value)

    if right_sibling:
        right_sibling.update(right_sibling.value + ch[1].value)

    n.update(0)

    return True


def sum(n1, n2):
    n = Number([n1.value, n2.value])

    while True:
        if explode(n):
            continue

        if not split(n):
            break

    return n


def numeral_sibling(n, mode):
    i_number = 1 if mode == "left" else 0
    i_sibling = 1 if mode == "left" else 0
    i_children = 0 if mode == "left" else 1

    p = n.parent

    if p is None:
        return None

    if n.index == i_number:
        sibling = p.children[i_children]
    else:
        while p.index != i_number:
            p = p.parent
            if p is None or p.parent is None:
                return None
        sibling = p.parent.children[i_children]

    while sibling.children:
        sibling = sibling.children[i_sibling]

    return sibling


def magnitude(n):
    if n.children is None:
        return n.value
    return 3*magnitude(n.children[0]) + 2*magnitude(n.children[1])


class Number:

    def __init__(self, data, index=None, parent=None):
        self.index = index
        self.parent = parent
        self.update(data)

    @property
    def value(self):
        if self.children:
            return [i.value for i in self.children]
        return self.data

    def update(self, data):
        self.data = data
        self.children = None

        if isinstance(data, list):
            self.children = [Number(v, i, self) for i, v in enumerate(data)]


numbers = [Number(json.loads(line)) for line in open("input.txt")]

print(f"Part1: {magnitude(reduce(sum, numbers))}")
print(f"Part2: {max(magnitude(sum(*pair)) for pair in permutations(numbers, 2))}")
