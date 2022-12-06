#!/usr/bin/env python
# https://adventofcode.com/2022/day/2


SEQ = "ABC"

RULES = {char: {
    "defeats": SEQ[i-1],
    "loses": SEQ[i-2]
} for i, char in enumerate(SEQ)}


def get_data():
    return [line.split() for line in open("input.txt")]


def calc_score(my_choice, result):
    score = SEQ.index(my_choice) + 1
    if result == "win":
        score += 6
    if result == "draw":
        score += 3
    return score


def part1(data):
    score = 0

    for turn in data:
        opponent_choice = turn[0]
        my_choice = SEQ["XYZ".index(turn[1])]
        result = "lost"
        if opponent_choice == my_choice:
            result = "draw"
        if RULES[my_choice]["defeats"] == opponent_choice:
            result = "win"
        score += calc_score(my_choice, result)

    return score


def part2(data):
    score = 0

    for turn in data:
        opponent_choice = turn[0]
        if turn[1] == "X":
            result = "lost"
            my_choice = RULES[opponent_choice]["defeats"]
        if turn[1] == "Y":
            result = "draw"
            my_choice = opponent_choice
        if turn[1] == "Z":
            result = "win"
            my_choice = RULES[opponent_choice]["loses"]
        score += calc_score(my_choice, result)

    return score


print(part1(get_data()))
print(part2(get_data()))
