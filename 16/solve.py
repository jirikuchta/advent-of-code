#!/usr/bin/env python3
# https://adventofcode.com/2020/day/16

from functools import reduce


def parse_input():
    fields, my_ticket, nearby_tickets = open("input.txt").read().split("\n\n")

    fields = [{
        "name": l[:l.index(":")],
        "ranges": [
            [int(r.split("-")[0]), int(r.split("-")[1])]
            for r in l[l.index(":") + 1:].replace(" ", "").split("or")
        ]} for l in fields.split("\n")]

    my_ticket = [int(n) for n in my_ticket.split("\n")[1].split(",")]

    nearby_tickets = [
        [int(n) for n in l.split(",")]
        for l in nearby_tickets.strip().split("\n")[1:]
    ]

    return fields, my_ticket, nearby_tickets


def in_ranges(n, ranges):
    return any(map(lambda r: r[0] <= n <= r[1], ranges))


def part1():
    fields, my_ticket, nearby_tickets = parse_input()
    all_ranges = reduce(lambda a, b: a + b["ranges"], fields, [])
    all_numbers = reduce(lambda a, b: a + b, nearby_tickets, [])
    return sum(filter(lambda n: not in_ranges(n, all_ranges), all_numbers))


def part2():
    fields, my_ticket, nearby_tickets = parse_input()
    all_ranges = list(reduce(lambda a, b: a + b["ranges"], fields, []))
    valid_tickets = list(filter(lambda t: all(map(
        lambda n: in_ranges(n, all_ranges), t)), nearby_tickets))

    for field in fields:
        field["index_candidates"] = []
        for i in range(0, len(my_ticket)):
            numbers = list(map(lambda t: t[i], valid_tickets))
            if all([in_ranges(n, field["ranges"]) for n in numbers]):
                field["index_candidates"].append(i)

    while True:
        found = False

        for field in fields:
            other_fields_index_candidates = list(reduce(
                lambda a, b: a + b["index_candidates"],
                filter(lambda f: f["name"] != field["name"], fields), []))

            for i in field["index_candidates"]:
                if i not in other_fields_index_candidates:
                    field["index_candidates"] = []
                    field["index"] = i
                    found = True

        if not found:
            break

    return reduce(
        lambda r, f: r * my_ticket[f["index"]],
        filter(lambda f: f["name"].startswith("departure"), fields), 1)


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
