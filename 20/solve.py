#!/usr/bin/env python3
# https://adventofcode.com/2020/day/20


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


def part1():
    grid = parse_input()
    return grid.tiles[0].id * grid.tiles[2].id * grid.tiles[6].id * grid.tiles[8].id


print(f"Part 1: {part1()}")
