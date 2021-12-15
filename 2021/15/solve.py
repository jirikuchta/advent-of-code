#!/usr/bin/env python
# https://adventofcode.com/2021/day/15

from math import inf
from queue import PriorityQueue

vertices = {}
start_vertex = complex()
end_vertex = complex()

for y, row in enumerate(open("input.txt").read().strip().split("\n")):
    for x, risk in enumerate(row):
        vertices[complex(y, x)] = int(risk)
        end_vertex = complex(y, x)

results = {k: inf for k in vertices.keys()}
results[start_vertex] = 0

q = PriorityQueue()
q.put((vertices[start_vertex], str(start_vertex)))

visited = []

while not q.empty():
    _, vertex = q.get()
    vertex = complex(vertex)

    visited.append(vertex)

    neighbors = [
        vertex + complex("1"),
        vertex + complex("1j"),
        vertex + complex("-1"),
        vertex + complex("-1j")
    ]

    for neighbor in neighbors:
        if neighbor not in vertices:
            continue

        if neighbor in visited:
            continue

        old_risk = results[neighbor]
        new_risk = results[vertex] + vertices[neighbor]

        if new_risk < old_risk:
            q.put((new_risk, str(neighbor)))
            results[neighbor] = new_risk

# part1
print(results[end_vertex])
