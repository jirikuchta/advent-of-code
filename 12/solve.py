#!/usr/bin/env python3
# https://adventofcode.com/2020/day/12


def part1():
    state = {"x": 0, "y": 0, "dir": "E"}

    for line in open("input.txt").readlines():
        cmd = state["dir"] if line[0] == "F" else line[0]
        arg = int(line[1:])

        if cmd in "LR":
            i = "NESW".index(state["dir"])
            i += (arg / 90) * (-1 if cmd == "L" else 1)
            state["dir"] = "NESW"[int(i) % 4]

        if cmd in "NESW":
            axis = "x" if cmd in "EW" else "y"
            state[axis] += arg * (-1 if cmd in "WS" else 1)

    return abs(state["x"]) + abs(state["y"])


def part2():
    waypoint_pos = {"x": 10, "y": 1}
    ship_pos = {"x": 0, "y": 0}

    for line in open("input.txt").readlines():
        cmd = line[0]
        arg = int(line[1:])

        if cmd == "F":
            ship_pos["x"] = ship_pos["x"] + waypoint_pos["x"] * arg
            ship_pos["y"] = ship_pos["y"] + waypoint_pos["y"] * arg

        if cmd in "LR":
            for i in range(1, int(arg / 90) + 1):
                waypoint_pos = {
                    "x": waypoint_pos["y"] * (-1 if cmd == "L" else 1),
                    "y": waypoint_pos["x"] * (-1 if cmd == "R" else 1)}

        if cmd in "NESW":
            axis = "x" if cmd in "EW" else "y"
            waypoint_pos[axis] += arg * (-1 if cmd in "WS" else 1)

    return abs(ship_pos["x"]) + abs(ship_pos["y"])


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
