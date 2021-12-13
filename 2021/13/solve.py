#!/usr/bin/env python
# https://adventofcode.com/2021/day/13

import re

data = open("input.txt").read().strip().split("\n\n")

dots = [[int(n) for n in re.findall(r'\d+', line)]
        for line in data[0].split("\n")]

folds = [[line[11], int(line[13:])]
         for line in data[1].split("\n")]

for fold in folds:
    folded_dots = []

    for dot in dots:
        if fold[0] == "y" and dot[1] > fold[1]:
            dot[1] = fold[1] - (dot[1] - fold[1])

        if fold[0] == "x" and dot[0] > fold[1]:
            dot[0] = fold[1] - (dot[0] - fold[1])

        if dot not in folded_dots:
            folded_dots.append(dot)

    dots = folded_dots

    # part 1
    if fold == folds[0]:
        print(len(dots))

# part 2
max_x = max(d[0] for d in dots)+1
max_y = max(d[1] for d in dots)+1
rows = [["x" if [x, y] in dots else " " for x in range(max_x)]
        for y in range(max_y)]
print("\n".join("".join(row) for row in rows))
