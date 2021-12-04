import numpy as np


def part_1(data):
    raw_calls, *raw_boards = data.split("\n\n")
    calls = [int(i) for i in raw_calls.split(",")]

    boards = np.loadtxt(raw_boards, int).reshape(-1, 5, 5)
    for i in calls:
        boards[boards == i] = -1
        marked = boards == -1
        for board in boards:
            marked = board == -1
            if any(marked.all(0) | marked.all(1)):
                return sum(board[~marked]) * i


def part_2(data):
    raw_calls, *raw_boards = data.split("\n\n")
    calls = [int(i) for i in raw_calls.split(",")]

    boards = np.loadtxt(raw_boards, int).reshape(-1, 5, 5)
    uncompleted_boards = [board for board in boards]
    for i in calls:
        boards[boards == i] = -1
        marked = boards == -1

        next_uncompleted_boards = []
        for board in uncompleted_boards:
            marked = board == -1
            if not any(marked.all(0) | marked.all(1)):
                next_uncompleted_boards.append(board)
        uncompleted_boards = next_uncompleted_boards[:]

        if len(uncompleted_boards) == 0:
            return sum(board[~marked]) * i


if __name__ == "__main__":
    with open("day_04_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
