#!/usr/bin/env python
# https://adventofcode.com/2022/day/8

from math import prod


def get_data():
    data = [list(map(lambda x: int(x), [*line.strip()]))
            for line in open("input.txt")]
    for i, row in enumerate(data):
        for j, height in enumerate(row):
            yield {
                "height": data[i][j],
                "view": {
                    "top": [x[j] for x in data[:i]],
                    "left": data[i][:j],
                    "bottom": [x[j] for x in data[i+1:]],
                    "right": data[i][j+1:]
                }
            }


def part1():
    count = 0
    for data in get_data():
        if len(data["view"]["top"]) == 0 or \
           len(data["view"]["left"]) == 0 or \
           len(data["view"]["bottom"]) == 0 or \
           len(data["view"]["right"]) == 0:
            count += 1
            continue

        if all(map(lambda x: x < data["height"], data["view"]["top"])) or \
           all(map(lambda x: x < data["height"], data["view"]["left"])) or \
           all(map(lambda x: x < data["height"], data["view"]["bottom"])) or \
           all(map(lambda x: x < data["height"], data["view"]["right"])):
            count += 1

    return count


def part2():
    score = 0
    for data in get_data():
        data["view"]["top"] = reversed(data["view"]["top"])
        data["view"]["left"] = reversed(data["view"]["left"])

        item_score = [0, 0, 0, 0]
        for y, direction in enumerate(data["view"].keys()):
            for item in data["view"][direction]:
                item_score[y] += 1
                if item >= data["height"]:
                    break
        score = max(score, prod([x for x in item_score if x > 0]))

    return score


print(part1())
print(part2())
