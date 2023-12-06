#!/usr/bin/env python
# https://adventofcode.com/2023/day/1

def get_data():
    return [line.strip() for line in open("input.txt")]


def part1(data):
    result = 0
    for line in data:
        numbers = [char for char in line if char.isdigit()]
        result += int(numbers[0] + numbers[-1])
    return result


def part2(data):
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    def translate(line):
        for i, word in enumerate(words):
            line = line.replace(word, f"{word[0]}{str(i+1)}{word[-1]}")
        return line

    return part1([translate(line) for line in data])


# print(part1(get_data()))
print(part2(get_data()))
