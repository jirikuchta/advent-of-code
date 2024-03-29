#!/usr/bin/env python
# https://adventofcode.com/2021/day/11


def get_data():
    parsed = [[int(n) for n in line.strip()] for line in open("input.txt")]
    data = {}
    for y, _ in enumerate(parsed):
        for x, _ in enumerate(parsed[y]):
            data[complex(x, y)] = {"energy": parsed[y][x], "flashed": False}
    return data


DIRECTIONS = (complex(0, 1), complex(1, 1), complex(1, 0), complex(1, -1),
              complex(0, -1), complex(-1, -1), complex(-1, 0), complex(-1, 1))


def count(part):
    data = get_data()

    flashes = 0
    step = 0

    while True:
        step += 1

        for i in data.values():
            i["energy"] += 1
            i["flashed"] = False

        check = True
        while check:
            check = False

            for key, item in data.items():
                if item["energy"] < 10 or item["flashed"]:
                    continue

                item["energy"] = 0
                item["flashed"] = True

                for d in DIRECTIONS:
                    adjacent_item = data.get(key + d)
                    if adjacent_item and not adjacent_item["flashed"]:
                        adjacent_item["energy"] += 1

                flashes += 1
                check = True

        if part == 1 and step == 100:
            return flashes

        if part == 2 and all(map(lambda i: i["flashed"], data.values())):
            return step


print(f"Part1: {count(1)}")
print(f"Part2: {count(2)}")
