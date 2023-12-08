#!/usr/bin/env python
# https://adventofcode.com/2023/day/2

def get_data():
    data = []

    for line in open("input.txt"):
        header, colors = line.strip().split(":")

        game_data = {
            "id": int(header.split()[1]),
            "red": 0, "blue": 0, "green": 0
        }

        for color in colors.replace(";", ",").split(","):
            count, color = color.strip().split()
            game_data[color] = max(game_data[color], int(count))

        data.append(game_data)

    return data


def part1(data):
    return sum(map(lambda i: i["id"],
               filter(lambda i: i["red"] < 13 and i["blue"] < 14 and i["green"] < 15, data)))


def part2(data):
    return sum(map(lambda i: i["red"] * i["blue"] * i["green"], data))


print(part1(get_data()))
print(part2(get_data()))
