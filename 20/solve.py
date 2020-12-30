#!/usr/bin/env python3
# https://adventofcode.com/2020/day/20

from functools import reduce


def parse_input():
    tiles = []
    for tile in open("input.txt").read().strip().split("\n\n"):
        rows = tile.split("\n")
        tile_id = rows[:1][0][5:-1]
        data = [[col == "#" for col in row] for row in rows[1:]]
        tiles.append(Tile(tile_id, data))
    return Grid(tiles)


class Grid:

    def __init__(self, tiles):
        self.tiles = self._arrange_tiles(tiles)

    def _arrange_tiles(self, tiles):
        return tiles

    def get_corner_tiles(self):
        return [t for t in self.tiles if len(self.get_adjacent_tiles(t)) == 2]

    def get_adjacent_tiles(self, tile):
        return list(filter(lambda t: t.id != tile.id and any(map(lambda b: t.has_border(b), tile.get_borders())), self.tiles))


class Tile:

    def __init__(self, id, data):
        self.id = int(id)
        self.data = data

    def flip_h(self):
        self.data.reverse()

    def flip_v(self):
        for row in self.data:
            row.reverse()

    def rotate_cw(self):
        data = [[] for row in self.data]
        for row in self.data:
            for i, col in enumerate(row):
                data[i].insert(0, col)
        self.data = data

    def get_borders(self):
        return [self.data[0], [row[-1] for row in self.data],
                self.data[-1], [row[0] for row in self.data]]

    def has_border(self, border):
        borders = self.get_borders()
        reversed_borders = [border[::-1] for border in borders]
        return border in borders or border in reversed_borders


def part1():
    grid = parse_input()
    return reduce(lambda a, b: a * b.id, grid.get_corner_tiles(), 1)


print(f"Part 1: {part1()}")
