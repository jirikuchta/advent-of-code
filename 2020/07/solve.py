#!/usr/bin/env python
# https://adventofcode.com/2020/day/7

import re
from functools import reduce


def get_data():
    result = {}
    for line in open("input.txt").readlines():
        res = re.findall("(?:^|(\\d+)\\s+)([^\\s]+\\s{1}[^\\s]+)", line)
        result[res[0][1]] = {item[1]: int(item[0]) for item in res[1:]}
    return result


def part1(name):
    data = get_data()

    def check(bag):
        return name in data[bag] or any([check(i) for i in data[bag]])

    return [check(bag) for bag in data].count(True)


def part2(name):
    data = get_data()

    def count(bag):
        return reduce(lambda a, b: a + data[bag][b] + count(b) * data[bag][b],
                      data[bag], 0)

    return count(name)


print(part1("shiny gold"))
print(part2("shiny gold"))
