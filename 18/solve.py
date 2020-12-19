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


def part1():
    results = []

    for expr in open("input.txt").readlines():
        results.append(compute(tokenize(expr)))

    return sum(results)


print(f"Part 1: {part1()}")
