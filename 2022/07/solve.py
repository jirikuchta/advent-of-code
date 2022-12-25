#!/usr/bin/env python
# https://adventofcode.com/2022/day/7

def get_data():
    dirs = {"/": 0}
    files = {}
    path = []

    for line in open("input.txt"):
        parts = line.split()
        item_path = "/" + "/".join(path[1:] + [parts[1]])
        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "..":
                    path = path[:-1]
                else:
                    path.append(parts[2])
        elif parts[0] == "dir":
            dirs[item_path] = 0
        else:
            files[item_path] = int(parts[0])

    for d in dirs.keys():
        dirs[d] = sum([f_size for f, f_size in files.items()
                       if f.startswith(d)])

    return dirs, files


def part1(dirs, files):
    return sum(size for size in dirs.values() if size <= 100000)


def part2(dirs, files):
    return sorted([size for size in dirs.values()
                   if size >= abs(70000000 - 30000000 - dirs["/"])])[0]


print(part1(*get_data()))
print(part2(*get_data()))
