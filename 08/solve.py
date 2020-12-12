#!/usr/bin/env python
# https://adventofcode.com/2020/day/8

from functools import reduce


def get_data():
    return [line.strip().split(" ")
            for line in open("input.txt").readlines()]


def part1():
    data = get_data()
    i = 0
    while data[i]:
        cmd, value = data[i]
        yield int(value) if cmd == "acc" else 0
        data[i] = None
        i += int(value) if cmd == "jmp" else 1


def part2():
    cmd_occurence = None

    def get_altered_data():
        data = get_data()
        if cmd_occurence is not None:
            cmds = list(filter(lambda i: i[0] in ("jmp", "nop"), data))
            cmds[cmd_occurence][0] = "jmp" if cmds[cmd_occurence][0] == "nop" else "nop"
        return data

    while True:
        data = get_altered_data()
        i = 0
        acc = 0

        try:
            while data[i]:
                cmd, value = data[i]
                add = int(value) if cmd == "acc" else 0
                yield add
                acc += add
                data[i] = None
                i += int(value) if cmd == "jmp" else 1
            else:
                yield -acc
                if cmd_occurence is None:
                    cmd_occurence = 0
                else:
                    cmd_occurence += 1
        except Exception:
            break


print(reduce(lambda a, b: a + b, part1(), 0))
print(reduce(lambda a, b: a + b, part2(), 0))
