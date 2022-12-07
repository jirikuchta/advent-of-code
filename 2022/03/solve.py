#!/usr/bin/env python
# https://adventofcode.com/2022/day/3

from string import ascii_lowercase, ascii_uppercase


def get_data():
    return [line for line in open("input.txt")]


def get_priority(char):
    return (ascii_lowercase + ascii_uppercase).index(char) + 1


def get_common_char(strings):
    for char in strings[0]:
        if all(map(lambda part: char in part, strings)):
            return char


def part1(data):
    result = 0

    for line in data:
        size = int(len(line)/2)
        parts = [line[size:], line[:size]]
        result += get_priority(get_common_char(parts))

    return result


def part2(data):
    groups = [data[i:i+3] for i in range(0, len(data), 3)]
    return sum(get_priority(get_common_char(group)) for group in groups)


print(part1(get_data()))
print(part2(get_data()))
