#!/usr/bin/env python3
# https://adventofcode.com/2020/day/18


def tokenize(expr):
    expr = expr.replace(" ", "").strip()

    tokens = []
    skip_chars = 0

    for i, token in enumerate(expr):

        if skip_chars > 0:
            skip_chars -= 1
            continue

        if token in ("+", "*"):
            tokens.append(token)
            continue

        if token == "(":
            sub_tokens, skip_chars = tokenize(expr[i+1:])
            tokens.append(sub_tokens)
            skip_chars += 1
            continue

        if token == ")":
            return tokens, i

        tokens.append(int(token))

    return tokens, skip_chars


def compute(tokens):
    operator = "+"
    result = 0

    for token in tokens:
        if token in ("+", "*"):
            operator = token
            continue

        if type(token) is list:
            token = compute(token)

        if operator == "*":
            result *= token
        else:
            result += token

    return result


def compute_additions(tokens):
    new_tokens = []
    skip_next = False

    for i, token in enumerate(tokens):

        if skip_next:
            skip_next = False
            continue

        if token == "+":
            next_token = tokens[i+1]
            if type(next_token) is list:
                next_token = compute(compute_additions(next_token))
            new_tokens = new_tokens[:-1] + [new_tokens.pop(-1) + next_token]
            skip_next = True
            continue

        if type(token) is list:
            token = compute(compute_additions(token))

        new_tokens.append(token)

    return new_tokens


def part1():
    return sum([compute(tokenize(expr))
               for expr in open("input.txt").readlines()])


def part2():
    return sum([compute(compute_additions(tokenize(expr)))
               for expr in open("input.txt").readlines()])


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
