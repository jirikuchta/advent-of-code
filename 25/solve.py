#!/usr/bin/env python3
# https://adventofcode.com/2020/day/25


def get_loop_size(pk):
    value = 1
    for loop_size in range(1, 20201227):
        value = (value * 7) % 20201227
        if value == pk:
            break
    return loop_size


def part1():
    card_pk, door_pk = [int(l) for l in open("input.txt").readlines()]
    return pow(door_pk, get_loop_size(card_pk), 20201227)


print(f"Part 1: {part1()}")
