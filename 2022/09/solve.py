#!/usr/bin/env python
# https://adventofcode.com/2022/day/9

MOVES = {"R": 1, "L": -1, "U": 1, "D": -1}


def get_data():
    data = [line.strip().split() for line in open("input.txt")]
    for item in data:
        item[1] = int(item[1])
    return data


def move(data, chain_length):
    ch = [[0, 0] for i in range(chain_length)]
    visited = set()

    for move, steps in data:
        for _ in range(steps):
            ch[0][0 if move in ("R", "L") else 1] += MOVES[move]
            for i in range(1, len(ch)):
                x_dist = ch[i-1][0] - ch[i][0]
                y_dist = ch[i-1][1] - ch[i][1]
                if abs(x_dist) > 1 or abs(y_dist) > 1:
                    ch[i][0] += (ch[i-1][0] > ch[i][0]) - (ch[i-1][0] < ch[i][0])
                    ch[i][1] += (ch[i-1][1] > ch[i][1]) - (ch[i-1][1] < ch[i][1])
            visited.add(tuple(ch[-1]))

    return len(set(visited))


print(move(get_data(), 2))
print(move(get_data(), 10))
