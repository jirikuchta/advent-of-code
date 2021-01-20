#!/usr/bin/env python3
# https://adventofcode.com/2020/day/20

import math
from functools import reduce


def parse_input():
    tiles = []
    for tile in open("input.txt").read().strip().split("\n\n"):
        rows = tile.split("\n")
        tile_id = rows[:1][0][5:-1]
        data = [[col == "#" for col in row] for row in rows[1:]]
        tiles.append(Tile(tile_id, data))
    return tiles


def make_grid(tiles, flip_top_left_tile=False):
    grid_size = int(math.sqrt(len(tiles)))
    res = [[None for j in range(0, grid_size)] for i in range(0, grid_size)]
    res[0][0] = get_top_left_tile(tiles, flip_top_left_tile)
    mutual_border = res[0][0].borders["left"]

    for row in range(0, grid_size):
        for col in range(1, grid_size):
            pass

    return Grid(res)


def get_top_left_tile(tiles, flip=False):
    tile = [t for t in tiles if len(get_adjacent_tiles(t, tiles)) == 2][0]
    adjacent_tiles = get_adjacent_tiles(tile, tiles)

    def correctly_rotated():
        has_right_adjacent_tile = any(map(
            lambda t: t.has_border(t.borders["right"], "left"),
            adjacent_tiles))

        has_bottom_adjacent_tile = any(map(
            lambda t: t.has_border(t.borders["bottom"], "top"),
            adjacent_tiles))

        return has_right_adjacent_tile and has_bottom_adjacent_tile

    if flip:
        tile.flip_h()

    while not correctly_rotated():
        tile.rotate_90_cw()

    return tile


def get_adjacent_tiles(tile, tiles, side=None):
    return [t for t in tiles if
            any(map(lambda b: t.id != tile.id and t.has_border(b, side),
                tile.borders.values()))]


class Grid:
    def __init__(self, tiles):
        self.tiles = tiles

    @property
    def corners(self):
        return (self.tiles[0][0], self.tiles[0][-1],
                self.tiles[-1][0], self.tiles[-1][-1])


class Tile:
    def __init__(self, id, data):
        self.id = int(id)
        self._data = data

    @property
    def data(self):  # data without borders
        return [row[1:-1] for row in self._data[1:-1]]

    @property
    def borders(self):
        return {
            "top": self._data[0],
            "right": [row[-1] for row in self._data],
            "bottom": self._data[-1],
            "left": [row[0] for row in self._data]}

    def flip_h(self):
        self._data.reverse()

    def rotate_90_cw(self):
        data = [[] for row in self._data]
        for row in self._data:
            for i, col in enumerate(row):
                data[i].insert(0, col)
        self._data = data

    def has_border(self, border, side=None):
        borders = [self.borders[side]] if side else self.borders.values()
        for tile_border in borders:
            if tile_border == border:
                return True

            if tile_border[::-1] == border:
                return True

        return False


def part1():
    grid = make_grid(parse_input())
    return reduce(lambda a, b: a * b.id, grid.corners, 1)


print(f"Part 1: {part1()}")
