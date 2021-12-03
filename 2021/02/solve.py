#!/usr/bin/env python
# https://adventofcode.com/2021/day/2


def get_data():
    return list(map(lambda i: [i[0], int(i[1])],
                    [line.split() for line in open("input.txt")]))


def part1(data):
    x = map(lambda i: i[1],
            filter(lambda i: i[0] == "forward", data))
    y = map(lambda i: -i[1] if i[0] == "up" else i[1],
            filter(lambda i: i[0] != "forward", data))
    return sum(x) * sum(y)


def part2(data):
    x, y, aim = [0, 0, 0]
    for direction, steps in data:
        if direction == "forward":
            x += steps
            y += aim * steps
        else:
            aim = aim + (-steps if direction == "up" else steps)
    return x * y


print(part1(get_data()))
print(part2(get_data()))
