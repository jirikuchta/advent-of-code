#!/usr/bin/env python3
# https://adventofcode.com/2020/day/21

from typing import TypedDict, List


class Allergen(TypedDict):
    name: str


class Ingredient(TypedDict):
    name: str
    allergens: List[Allergen]


class Food(TypedDict):
    ingredients: List[Ingredient]
    listed_allergens: List[Allergen]


def parse_input() -> List[Food]:
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
                ingredient = {"name": i_name, "allergens": []}
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
                i["allergens"].append(allergen)

    return foods


def part1():
    foods = parse_input()
    res = 0
    for food in foods:
        for ingredient in food["ingredients"]:
            if len(ingredient["allergens"]) == 0:
                res += 1
    return res


print(f"Part 1: {part1()}")
