#!/usr/bin/env python3
# https://adventofcode.com/2020/day/21

from typing import TypedDict, List, Tuple, Set, Optional


class Ingredient(TypedDict):
    name: str
    allergen: Optional[str]
    allergen_candidates: Set[str]


class Food(TypedDict):
    ingredients: List[Ingredient]
    listed_allergens: Set[str]


def parse_input() -> Tuple[List[Ingredient], List[Food]]:
    allergens: Set[str] = set()
    ingredients: List[Ingredient] = []
    foods: List[Food] = []

    for line in open("input.txt").readlines():
        line = line.replace("(", "").replace(")", "").replace(",", "")
        ingredients_str, allergens_str = line.split("contains ")
        food: Food = {"ingredients": [], "listed_allergens": set()}

        for i_name in ingredients_str.strip().split(" "):

            try:
                i = next(filter(lambda i: i["name"] == i_name, ingredients))
            except StopIteration:
                i = {"name": i_name, "allergen": None, "allergen_candidates": set()}
                ingredients.append(i)
            food["ingredients"].append(i)

        for a_name in allergens_str.strip().split(" "):
            allergens.add(a_name)
            food["listed_allergens"].add(a_name)

        foods.append(food)

    for a in allergens:
        a_foods = list(filter(lambda f: a in f["listed_allergens"], foods))
        for i in a_foods[0]["ingredients"]:
            if all(map(lambda f: i in f["ingredients"], a_foods)):
                i["allergen_candidates"].add(a)

    while any(map(lambda i: len(i["allergen_candidates"]), ingredients)):
        allergen = None
        for i in ingredients:
            if len(i["allergen_candidates"]) == 1:
                allergen = list(i["allergen_candidates"])[0]
                i["allergen"] = allergen
        if allergen:
            for i in ingredients:
                try:
                    i["allergen_candidates"].remove(allergen)
                except KeyError:
                    pass

    return ingredients, foods


def part1():
    ingredients, foods = parse_input()
    res = 0
    for food in foods:
        for ingredient in food["ingredients"]:
            if ingredient["allergen"] is None:
                res += 1
    return res


def part2():
    ingredients, foods = parse_input()
    ingredients = [i for i in ingredients if i["allergen"]]
    return ",".join([i["name"]for i in sorted(
        [i for i in ingredients if i["allergen"]],
        key=lambda i: i["allergen"])])


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
