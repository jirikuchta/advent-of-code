#!/usr/bin/env python
# https://adventofcode.com/2021/day/8

from itertools import permutations, chain


wire_orders = tuple(permutations("abcdefg"))

digits = ("1110111", "0010010", "1011101", "1011011", "0111010",
          "1101011", "1101111", "1010010", "1111111", "1111011")


def get_data():
    entries = [ln.split(" | ") for ln in open("input.txt")]
    return [[entry[0].split(), entry[1].split()] for entry in entries]


def digit_from_signal(signal, wire_order):
    values = ["0"]*7
    for ch in signal:
        values[wire_order.index(ch)] = "1"

    digit = "".join(values)
    if digit in digits:
        return str(digits.index(digit))


def get_wire_order(signals):
    for wo in wire_orders:
        if all([digit_from_signal(s, wo) is not None for s in signals]):
            return wo


def out_numbers():
    res = []
    for signals, out in get_data():
        wire_order = get_wire_order(signals)
        res.append([digit_from_signal(s, wire_order) for s in out])
    return res


print(len(list(filter(lambda n: int(n) in (1, 4, 7, 8), chain.from_iterable(out_numbers())))))
print(sum([int("".join(ls)) for ls in out_numbers()]))
