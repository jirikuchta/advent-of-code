#!/usr/bin/env python
# https://adventofcode.com/2022/day/7

from copy import copy


def get_data():
    dirs = {"/": {"path": []}}
    files = {}
    path = []

    for line in open("input.txt"):
        parts = line.split()
        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "..":
                    path = path[:-1]
                else:
                    path.append(parts[2])
        elif parts[0] == "dir":
            dirs[parts[1]] = {"path": copy(path)}
        else:
            files[parts[1]] = {"size": int(parts[0]), "path": copy(path)}

    return dirs, files


def part1(dirs, files):
    sizes = {}
    for dir_name in dirs.keys():
        sizes[dir_name] = sum([f["size"] for f in files.values() if dir_name in f["path"]])
    return sum(size for size in sizes.values() if size <= 100000)


print(part1(*get_data()))
