#!/usr/bin/env python
# https://adventofcode.com/2021/day/15

from math import inf
from queue import PriorityQueue


def dijkstra(grid):
    start = (0, 0)
    end = (len(grid) - 1, len(grid[0]) - 1)

    q = PriorityQueue()
    q.put((grid[start[0]][start[1]], start))

    results = {}
    for row, _ in enumerate(grid):
        for col, _ in enumerate(grid[row]):
            results[(row, col)] = inf
    results[start] = 0

    visited = set()

    while not q.empty():
        vertex = q.get()[1]
        visited.add(vertex)

        for move in (-1, 0), (0, 1), (1, 0), (0, -1):
            row = vertex[0] + move[0]
            col = vertex[1] + move[1]
            neighbor = (row, col)

            if neighbor in visited:
                continue

            try:
                old_risk = results[neighbor]
                new_risk = results[vertex] + grid[row][col]
            except KeyError:
                continue  # out of grid

            if new_risk < old_risk:
                q.put((new_risk, neighbor))
                results[neighbor] = new_risk

    return results[end]


grid = [list(map(int, row.strip())) for row in open("input.txt")]
print(f"Part1: {dijkstra(grid)}")

rows_count = len(grid)
cols_count = len(grid[0])

for _ in range(4):
    for row in grid:
        tail = row[-rows_count:]
        row.extend((x + 1) if x < 9 else 1 for x in tail)

for _ in range(4):
    for row in grid[-cols_count:]:
        row = [(x + 1) if x < 9 else 1 for x in row]
        grid.append(row)

print(f"Par2: {dijkstra(grid)}")
