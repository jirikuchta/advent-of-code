#!/usr/bin/env python3
# https://adventofcode.com/2020/day/22


def parse_input():
    return tuple([int(n) for n in p.split("\n")[1:] if n]
                 for p in open("input.txt").read().split("\n\n"))


def play(decks, recursive=False):
    turns = []

    while all(map(lambda d: len(d) > 0, decks)):
        if recursive and canonize_decks(decks) in turns:
            return decks[0], []

        turns.append(canonize_decks(decks))

        p1_card = decks[0].pop(0)
        p2_card = decks[1].pop(0)
        winner = "p1" if p1_card > p2_card else "p2"

        if recursive and len(decks[0]) >= p1_card and len(decks[1]) >= p2_card:
            res = play([decks[0][:p1_card], decks[1][:p2_card]], True)
            winner = "p1" if len(res[0]) > 0 else "p2"

        if winner == "p1":
            decks[0].append(p1_card)
            decks[0].append(p2_card)
        else:
            decks[1].append(p2_card)
            decks[1].append(p1_card)

    return decks


def canonize_decks(decks):
    return "|".join([",".join(map(lambda i: str(i), deck)) for deck in decks])


def get_result(recursive):
    p1_deck, p2_deck = play(parse_input(), recursive)
    winners_deck = next(filter(lambda p: len(p) > 0, (p1_deck, p2_deck)))
    res = 0
    for i, card in enumerate(winners_deck):
        res += card * (len(winners_deck) - i)
    return res


print(f"Part 1: {get_result(False)}")
print(f"Part 2: {get_result(True)}")
