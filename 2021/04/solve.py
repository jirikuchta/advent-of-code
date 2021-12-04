#!/usr/bin/env python
# https://adventofcode.com/2021/day/4

def get_data():
    with open("input.txt") as file:
        data = file.read().strip().split("\n\n")

    numbers = [int(n) for n in data.pop(0).strip().split(",")]
    boards = [[[int(n) for n in row.split()]
               for row in board.split("\n")] for board in data]

    return numbers, boards


def is_winning_board(board, numbers):
    cols = [[row[i] for row in board] for i in range(len(board[0]))]
    full_row = any([all(map(lambda n: n in numbers, row)) for row in board])
    full_col = any([all(map(lambda n: n in numbers, col)) for col in cols])
    return full_row or full_col


def calc_result(board, draw_numbers):
    unmarked_numbers = [n for row in board
                        for n in row if n not in draw_numbers]
    return sum(unmarked_numbers) * draw_numbers[-1]


def part1(numbers, boards):
    draw_numbers = []
    for i in range(len(numbers)):
        draw_numbers = numbers[:i]
        for board in boards:
            if is_winning_board(board, draw_numbers):
                return calc_result(board, draw_numbers)


def part2(numbers, boards):
    draw_numbers = []
    last_win_draw_numbers = []
    winning_boards = []
    for i in range(len(numbers)):
        draw_numbers = numbers[:i]

        for board_i, board in enumerate(boards):
            if is_winning_board(board, draw_numbers):
                winning_boards.append(board)
                last_win_draw_numbers = draw_numbers
                del boards[board_i]

    return calc_result(winning_boards[-1], last_win_draw_numbers)


print(part1(*get_data()))
print(part2(*get_data()))
