#!/usr/bin/env python
# https://adventofcode.com/2020/day/4

import re
from functools import reduce


def parse_input():
    result = []

    with open("inputs/day4.txt") as file:
        data = file.read()

    for item in data.replace(" ", "\n").strip().split("\n\n"):
        passport = {}
        for pair in item.split("\n"):
            key, value = pair.split(":")
            passport[key] = value
        result.append(passport)

    return result


def part1_validation(passport):
    mandatory_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    return all([field in passport for field in mandatory_fields])


def part2_validation(passport):
    def validate_year(value, min, max):
        return re.match("^\\d{4}$", value) and min <= int(value) <= max

    def validate_hgt(value):
        r = re.match("^(\\d{2,3})(cm|in)$", value)

        try:
            height = int(r.group(1))
            unit = r.group(2)
        except Exception:
            return False

        if unit == "cm" and not 150 <= height <= 193:
            return False

        if unit == "in" and not 59 <= height <= 76:
            return False

        return True

    if not part1_validation(passport):
        return False

    if not validate_year(passport["byr"], 1920, 2002):
        return False

    if not validate_year(passport["iyr"], 2010, 2020):
        return False

    if not validate_year(passport["eyr"], 2020, 2030):
        return False

    if not validate_hgt(passport["hgt"]):
        return False

    if not re.match("^#[0-9a-f]{6}$", passport["hcl"]):
        return False

    if passport["ecl"] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        return False

    if not re.match("^\\d{9}$", passport["pid"]):
        return False

    return True


def count_valid_passports(passports, validator):
    return reduce(lambda c, p: c + (1 if validator(p) else 0), passports, 0)


passports = parse_input()
print(count_valid_passports(passports, part1_validation))
print(count_valid_passports(passports, part2_validation))
