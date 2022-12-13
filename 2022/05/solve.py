#!/usr/bin/env python
# https://adventofcode.com/2022/day/5

from string import ascii_uppercase


def get_data():
    with open("input.txt") as file:
        raw_stacks, raw_instructions = file.read().split("\n\n")

    raw_stacks = raw_stacks.split("\n")
    raw_instructions = raw_instructions.strip().split("\n")

    stacks = []
    for i, stack_key in enumerate(raw_stacks[-1]):
        if stack_key.isdigit():
            stack = []
            for line in raw_stacks[:-1]:
                if i < len(line) and line[i] in ascii_uppercase:
                    stack.insert(0, line[i])
            stacks.append(stack)

    instructions = []
    for line in raw_instructions:
        instructions.append({
            "count": int(line.split()[1]),
            "from": int(line.split()[3])-1,
            "to": int(line.split()[5])-1
        })

    return stacks, instructions


def part1(stacks, instructions):
    for i in instructions:
        for _ in range(i["count"]):
            stacks[i["to"]].append(stacks[i["from"]].pop())
    return "".join([stack[-1] for stack in stacks])


def part2(stacks, instructions):
    for i in instructions:
        stacks[i["to"]] += stacks[i["from"]][-i["count"]:]
        stacks[i["from"]] = stacks[i["from"]][:-i["count"]]
    return "".join([stack[-1] for stack in stacks])


print(part1(*get_data()))
print(part2(*get_data()))
