#!/usr/bin/env python
# https://adventofcode.com/2021/day/17

import re
import json
from math import floor, ceil
from functools import reduce


def explode(n):
    pair = None
    depth = 0

    for i, ch in enumerate(n):
        if ch == "[":
            depth += 1
        if ch == "]":
            depth -= 1
        if depth == 5:
            pair = n[i:i+n[i:].index("]")+1]
            break

    if not pair:
        return n

    a, b = json.loads(pair)

    def repl(m):
        def left(lm):
            return str(int(lm.groups()[0]) + a) + lm.groups()[1]

        def right(rm):
            return str(int(rm.groups()[0]) + b)

        return "".join([
            re.sub("(\\d+)([^\\d])?$", left, m.groups()[0], 1),
            "0",
            re.sub("(\\d+)", right, m.groups()[2], 1)
        ])

    return re.sub(f"(.*)({re.escape(pair)})(.*)", repl, n, 1)


def split(n):
    def repl(m):
        n = m.groups()[0]
        return f"[{floor(int(n) / 2)}, {ceil(int(n) / 2)}]"
    return re.sub("(\\d{2,})", repl, n, 1)


def sum(a, b):
    n = f"[{a}, {b}]" if a else b

    while True:
        updated = explode(n)
        changed = updated != n
        n = updated
        if not changed:
            break

    while True:
        updated = split(n)
        changed = updated != n
        n = updated
        if not changed:
            break
        sum(None, n)

    return n


print("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")
print(reduce(sum, [line.strip() for line in open("input.txt")]))
