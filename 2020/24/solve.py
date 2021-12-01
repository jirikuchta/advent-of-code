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
        tiles.append(tile)

    black_tiles = list(filter(lambda t: tiles.count(t) % 2 == 1, tiles))

    return tiles, black_tiles


def part1():
    tiles, black_tiles = parse_input()
    return len(black_tiles)


def part2(days):
    tiles, black_tiles = parse_input()

    def get_adjacent_tiles(tile):
        adjacent_tiles = [
            [tile[0] + 0.5, tile[1] + 1],
            [tile[0] + 1, tile[1]],
            [tile[0] + 0.5, tile[1] - 1],
            [tile[0] - 0.5, tile[1] - 1],
            [tile[0] - 1, tile[1]],
            [tile[0] - 0.5, tile[1] + 1]]

        adjacent_black_tiles = []
        adjacent_white_tiles = []

        for adjacent_tile in adjacent_tiles:
            if adjacent_tile in black_tiles:
                adjacent_black_tiles.append(adjacent_tile)
            else:
                adjacent_white_tiles.append(adjacent_tile)

        return adjacent_white_tiles, adjacent_black_tiles

    for day in range(0, days):
        tmp_black_tiles = []

        for tile in black_tiles:
            adjacent_white_tiles, adjacent_black_tiles = get_adjacent_tiles(tile)

            if len(adjacent_black_tiles) in (1, 2):
                if tile not in tmp_black_tiles:
                    tmp_black_tiles.append(tile)

            for white_tile in adjacent_white_tiles:
                if len(get_adjacent_tiles(white_tile)[1]) == 2:
                    if white_tile not in tmp_black_tiles:
                        tmp_black_tiles.append(white_tile)

        black_tiles = tmp_black_tiles

    return len(black_tiles)


print(f"Part 1: {part1()}")
print(f"Part 2: {part2(100)}")
