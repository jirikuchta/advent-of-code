#!/usr/bin/env python3
# https://adventofcode.com/2020/day/16

from functools import reduce


def parse_input():
    fields, my_ticket, nearby_tickets = open("input.txt").read().split("\n\n")

    fields = [{
        "name": l[:l.index(":")],
        "ranges": [[int(r.split("-")[0]), int(r.split("-")[1])]
                   for r in l[l.index(":") + 1:].replace(" ", "").split("or")]
    } for l in fields.split("\n")]

    my_ticket = [int(n) for n in my_ticket.split("\n")[1].split(",")]

    nearby_tickets = [[int(n) for n in l.split(",")]
                      for l in nearby_tickets.strip().split("\n")[1:]]

    return fields, my_ticket, nearby_tickets


def part1():
    fields, my_ticket, nearby_tickets = parse_input()
    all_ranges = reduce(lambda a, b: a + b["ranges"], fields, [])
    all_numbers = reduce(lambda a, b: a + b, nearby_tickets, [])
    return sum(filter(lambda n: not any(map(lambda r: r[0] <= n <= r[1],
                      all_ranges)), all_numbers))


print(f"Part 1: {part1()}")
