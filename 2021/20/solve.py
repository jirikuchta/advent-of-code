#!/usr/bin/env python
# https://adventofcode.com/2021/day/20


key_data, img_data = open("input.txt").read().split("\n\n")

key = key_data.replace("\n", "")
img = [[c for c in r] for r in img_data.strip().split("\n")]


def display(grid):
    return "\n".join(["".join(map(str, row)) for row in grid])


def decode(data):
    bn = "".join(["".join(map(str, row)) for row in data])
    n = int(bn.replace(".", "0").replace("#", "1"), 2)
    return key[n]


def pad(img, v):
    for i in range(3):
        img.insert(0, [v]*len(img[0]))
        img.append([v]*len(img[0]))
        for row in img:
            row.insert(0, v)
            row.append(v)
    return img


def enhance(img, steps):
    for i in range(steps):
        img = pad(img, "#" if i % 2 == 1 and key[0] == "#" else ".")
        enhanced = []

        for y in range(1, len(img) - 1):
            row = []
            for x in range(1, len(img[0]) - 1):
                row.append(decode([
                    img[y-1][x-1:x+2],
                    img[y][x-1:x+2],
                    img[y+1][x-1:x+2]
                ]))
            enhanced.append(row)
        img = enhanced
    return img


print(f"Part1:\n{display(enhance(img, 2)).count('#')}")
print(f"Part2:\n{display(enhance(img, 50)).count('#')}")
