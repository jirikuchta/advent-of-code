#!/usr/bin/env python3
# https://adventofcode.com/2020/day/19

import re
from itertools import product, chain


def parse_input():
    rules_text, messages_text = open("input.txt").read().split("\n\n")

    messages = [line for line in messages_text.split("\n") if line]

    rules = {}
    for line in rules_text.split("\n"):
        k, v = line.split(":")
        k = int(k)

        if re.search("[a-z]", v) is not None:
            rules[k] = tuple(v.replace("\"", "").strip())
            continue

        value = []
        for item in v.split("|"):
            value.append([int(i) for i in item.strip().split(" ")])
        rules[k] = tuple(value)

    return rules, messages


def resolve_rule(rule, rules):

    if type(rule) is int:
        rule = rules.get(rule)

    if type(rule) is list:
        rule = list(resolve_rule(i, rules) for i in rule)

        if all(map(lambda i: type(i) is tuple, rule)):
            rule = tuple("".join(p) for p in product(*rule))

    if type(rule) is tuple:
        rule = tuple(resolve_rule(i, rules) for i in rule)

        if all(map(lambda i: type(i) is tuple, rule)):
            rule = tuple(chain(*rule))

    return rule


def part1():
    rules, messages = parse_input()
    rule = resolve_rule(0, rules)
    return len(list(filter(lambda m: m in rule, messages)))


print(f"Part 1: {part1()}")
