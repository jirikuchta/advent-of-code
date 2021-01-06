#!/usr/bin/env python3
# https://adventofcode.com/2020/day/21

from typing import TypedDict, List, Tuple, Optional


class Allergen(TypedDict):
    name: str


class Ingredient(TypedDict):
    name: str
    allergen: Optional[Allergen]


class Food(TypedDict):
    ingredients: List[Ingredient]
    listed_allergens: List[Allergen]


def parse_input() -> Tuple[List[Food], List[Ingredient]]:
    ingredients: List[Ingredient] = []
    allergens: List[Allergen] = []
    foods: List[Food] = []

    for l in open("input.txt").readlines():
        ingredients_str, allergens_str = l.replace("(", "").replace(")", "").replace(",", "").split("contains ")
        food: Food = {"ingredients": [], "listed_allergens": []}

        for i_name in ingredients_str.strip().split(" "):
            try:
                ingredient = next(filter(lambda i: i["name"] == i_name, ingredients))
            except StopIteration:
                ingredient = {"name": i_name, "allergen": None}
                ingredients.append(ingredient)
            food["ingredients"].append(ingredient)

        for a_name in allergens_str.strip().split(" "):
            try:
                allergen = next(filter(lambda a: a["name"] == a_name, allergens))
            except StopIteration:
                allergen = {"name": a_name}
                allergens.append(allergen)
            food["listed_allergens"].append(allergen)

        foods.append(food)

    for allergen in allergens:
        allergen_foods = list(filter(lambda f: allergen in f["listed_allergens"], foods))
        for i in allergen_foods[0]["ingredients"]:
            if all(map(lambda f: i in f["ingredients"], allergen_foods)):
                i["allergen"] = allergen

    return foods, ingredients


def part1():
    foods, ingredients = parse_input()
    res = 0
    for food in foods:
        for ingredient in food["ingredients"]:
            if ingredient["allergen"] is None:
                res += 1
    return res


def part2():
    foods, ingredients = parse_input()
    ingredients = [i for i in ingredients if i["allergen"]]
    return ",".join([i["name"]for i in sorted(
        [i for i in ingredients if i["allergen"]],
        key=lambda i: i["allergen"]["name"])])


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
