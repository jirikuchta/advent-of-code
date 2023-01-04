#!/usr/bin/env python
# https://adventofcode.com/2022/day/9

from copy import copy


def get_data():
    data = [line.strip().split() for line in open("input.txt")]
    for item in data:
        item[1] = int(item[1])
    return data


def part1(data):
    head_pos = [[0, 0]]
    tail_pos = [[0, 0]]

    for direction, steps in data:
        for _ in range(steps):
            new_head_pos = copy(head_pos[-1])
            new_tail_pos = copy(tail_pos[-1])

            if direction == "R":
                new_head_pos[0] += 1
            if direction == "L":
                new_head_pos[0] -= 1
            if direction == "D":
                new_head_pos[1] -= 1
            if direction == "U":
                new_head_pos[1] += 1

            x_diff = abs(new_head_pos[0] - tail_pos[-1][0])
            y_diff = abs(new_head_pos[1] - tail_pos[-1][1])
            if x_diff > 1 or y_diff > 1:
                new_tail_pos = copy(head_pos[-1])

            head_pos.append(new_head_pos)
            tail_pos.append(new_tail_pos)

    return len(set([f"{i[0]},{i[1]}" for i in tail_pos]))


def part2():
    pass


print(part1(get_data()))
print(part2())
