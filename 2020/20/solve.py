#!/usr/bin/env python3
# https://adventofcode.com/2020/day/20

import math
import re
from functools import reduce


def parse_input():
    tiles = []
    for tile in open("input.txt").read().strip().split("\n\n"):
        rows = tile.split("\n")
        tile_id = rows[:1][0][5:-1]
        data = [[col for col in row] for row in rows[1:]]
        tiles.append(Tile(tile_id, data))
    return tiles


def arrange_tiles(tiles, flip_top_left_tile=False):
    grid_size = int(math.sqrt(len(tiles)))
    res = [[None for j in range(0, grid_size)] for i in range(0, grid_size)]

    for row in range(0, grid_size):
        for col in range(0, grid_size):
            if row == 0 and col == 0:
                tile = get_top_left_tile(tiles, flip_top_left_tile)
            else:
                try:
                    if col == 0:
                        tile = get_adjacent_tile(
                            res[row-1][0].borders["bottom"], "top", tiles)
                    else:
                        tile = get_adjacent_tile(
                            res[row][col-1].borders["right"], "left", tiles)
                except Exception:
                    return arrange_tiles(tiles, True)
            res[row][col] = tile
            tiles = list(filter(lambda t: t.id != tile.id, tiles))

    return res


def get_top_left_tile(tiles, flip=False):
    tile = [t for t in tiles if len(get_adjacent_tiles(t, tiles)) == 2][0]
    adjacent_tiles = get_adjacent_tiles(tile, tiles)

    def correctly_rotated():
        has_right_adjacent_tile = any(map(
            lambda t: t.has_border(tile.borders["right"]), adjacent_tiles))

        has_bottom_adjacent_tile = any(map(
            lambda t: t.has_border(tile.borders["bottom"]), adjacent_tiles))

        return has_right_adjacent_tile and has_bottom_adjacent_tile

    if flip:
        tile.flip_h()

    while not correctly_rotated():
        tile.rotate_90_cw()

    return tile


def get_adjacent_tiles(tile, tiles):
    return [t for t in tiles if
            any(map(lambda b: t.id != tile.id and t.has_border(b),
                tile.borders.values()))]


def get_adjacent_tile(border, side, tiles, flip=False):
    tile = next(filter(lambda t: t.has_border(border), tiles))

    if flip:
        tile.flip_h()

    for i in range(0, 4):
        if tile.borders[side] == border:
            break
        tile.rotate_90_cw()
    else:
        return get_adjacent_tile(border, side, tiles, True)

    return tile


class DataGrid:

    def __init__(self, data):
        self._data = data

    def __str__(self):
        return "\n".join(["".join(row) for row in self._data])

    @property
    def data(self):
        return self._data

    def flip_h(self):
        self._data.reverse()

    def rotate_90_cw(self):
        data = [[] for row in self._data]
        for row in self._data:
            for i, col in enumerate(row):
                data[i].insert(0, col)
        self._data = data


class Tile(DataGrid):

    def __init__(self, id, data):
        self.id = int(id)
        super().__init__(data)

    @property
    def data(self):  # no borders
        return [row[1:-1] for row in self._data[1:-1]]

    @property
    def borders(self):
        return {
            "top": self._data[0],
            "right": [row[-1] for row in self._data],
            "bottom": self._data[-1],
            "left": [row[0] for row in self._data]}

    def has_border(self, border):
        for tile_border in self.borders.values():
            if tile_border == border:
                return True

            if tile_border[::-1] == border:
                return True

        return False


def part1():
    tiles = parse_input()
    corner_tiles = filter(lambda t: len(get_adjacent_tiles(t, tiles)) == 2, tiles)
    return reduce(lambda a, b: a * b.id, corner_tiles, 1)


def part2(flip=False):
    """ This is how monsters look like
                      #
    #    ##    ##    ###
     #  #  #  #  #  #
    """
    cre = [
        re.compile(r".{18}#."),
        re.compile(r"#.{4}(?:##.{4}){2}###"),
        re.compile(r"(?=(.(?:#.{2}){6}.))")]

    tiles = arrange_tiles(parse_input())

    data = []
    for tiles_row in tiles:
        for i in range(0, len(tiles[0][0].data)):
            data.append(reduce(lambda r, t: r + t.data[i], tiles_row, []))

    grid = DataGrid(data)

    if flip:
        grid.flip_h()

    for _ in range(0, 4):
        monsters = 0
        for i in range(2, len(grid.data)):
            for match in cre[2].finditer("".join(grid.data[i])):
                if (cre[0].match("".join(grid.data[i - 2])[match.start():]) and
                        cre[1].match("".join(grid.data[i - 1])[match.start():])):
                    monsters += 1

        if monsters > 0:
            return str(grid).count("#") - monsters * 15

        grid.rotate_90_cw()

    if not flip:
        return part2(True)


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
