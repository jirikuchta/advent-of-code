#!/usr/bin/env python
# https://adventofcode.com/2022/day/6

def find_marker(length):
    with open("input.txt") as file:
        data = file.read().strip()
    i = 0
    while len({char for char in data[i:i+length]}) < length:
        i += 1
    return i+length


print(find_marker(4))
print(find_marker(14))
