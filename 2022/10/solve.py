#!/usr/bin/env python
# https://adventofcode.com/2022/day/10


def get_data():
    data = [line.strip().split() for line in open("input.txt")]
    for item in data:
        if len(item) == 2:
            item[1] = int(item[1])
    return data


def tick():
    cycle = 0
    x = 1

    for cmd in get_data():
        for _ in range({"noop": 1, "addx": 2}[cmd[0]]):
            cycle += 1
            yield cycle, x
        if cmd[0] == "addx":
            x += cmd[1]


def part1():
    res = 0

    for cycle, x in tick():
        if cycle > 220:
            break
        if divmod(cycle, 40)[1] == 20:
            res += x * cycle

    return res


def part2():
    sprite = [0, 2]
    img = "." * 40 * 6

    for cycle, x in tick():
        pass

    return "\n".join([img[i:i + 40] for i in range(0, len(img), 40)])


print(part1())
print(part2())
