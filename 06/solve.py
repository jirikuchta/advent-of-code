#!/usr/bin/env python
# https://adventofcode.com/2020/day/6


def part1():
    result = 0
    for g in open("input.txt").read().split("\n\n"):
        result += len(set(ch for ch in g.replace("\n", "")))
    return result


def part2():
    result = 0
    for g in open("input.txt").read().split("\n\n"):
        all_answers = g.replace("\n", "")
        group_length = g.strip("\n").count("\n") + 1
        for ch in set(all_answers):
            result += 1 if all_answers.count(ch) == group_length else 0
    return result


print(part1())
print(part2())
