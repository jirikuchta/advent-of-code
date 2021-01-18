#!/usr/bin/env python3
# https://adventofcode.com/2020/day/25


def parse_input():
    card_pk, door_pk = [int(l) for l in open("input.txt").readlines()]

    card_loop_size = 0
    while pow(7, card_loop_size, 20201227) != card_pk:
        card_loop_size += 1

    door_loop_size = 0
    while pow(7, door_loop_size, 20201227) != door_pk:
        door_loop_size += 1

    return card_pk, door_pk, card_loop_size, door_loop_size


def part1():
    card_pk, door_pk, card_loop_size, door_loop_size = parse_input()
    return pow(door_pk, card_loop_size, 20201227)


print(f"Part 1: {part1()}")
