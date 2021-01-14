#!/usr/bin/env python3
# https://adventofcode.com/2020/day/24


import re


def parse_input():
    tiles = []
    for tile_dirs in [re.findall("(nw|ne|sw|se|w|e)", line)
                      for line in open("input.txt").readlines()]:
        tile = [0, 0]
        for tile_dir in tile_dirs:
            if tile_dir == "nw":
                tile[0] -= 0.5
                tile[1] += 1
            if tile_dir == "ne":
                tile[0] += 0.5
                tile[1] += 1
            if tile_dir == "sw":
                tile[0] -= 0.5
                tile[1] -= 1
            if tile_dir == "se":
                tile[0] += 0.5
                tile[1] -= 1
            if tile_dir == "w":
                tile[0] -= 1
            if tile_dir == "e":
                tile[0] += 1
        tiles.append([float(tile[0]), float(tile[1])])
    return tiles


def part1():
    tiles = parse_input()
    return len(list(filter(lambda t: tiles.count(t) == 1, tiles)))


print(f"Part 1: {part1()}")
