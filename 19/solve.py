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


def part2():
    rules, messages = parse_input()
    valid_messages = 0

    # message is valid if it begins with at least 2 occurences of rule 42
    # followed with at least 1 occurence of rule 31
    rule_0_rules = (
        {"id": 42, "min_matches": 2, "matches": 0},
        {"id": 31, "min_matches": 1, "matches": 0})

    for m in messages:
        for rule in rule_0_rules:
            rule["matches"] = 0

        for rule in rule_0_rules:
            r = resolve_rule(rule["id"], rules)
            chunk_length = len(r[0])
            chunk_valid = True

            while chunk_valid:
                chunk = m[:chunk_length]
                chunk_valid = chunk in r

                if chunk_valid:
                    rule["matches"] += 1
                    m = m[chunk_length:]
                    continue

                if chunk and rule["matches"] < rule["min_matches"]:
                    # invalid message
                    break

                if not chunk:  # end of message
                    if rule["id"] != rule_0_rules[-1]["id"]:
                        break

                    if rule["matches"] < rule["min_matches"]:
                        break

                    if rule["matches"] >= rule_0_rules[0]["matches"]:
                        break

                    valid_messages += 1
            else:
                continue
            break

    return valid_messages


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
