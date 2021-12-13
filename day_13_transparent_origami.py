import numpy as np


def part_1(data):
    raw_dots, raw_folds = data.split("\n\n")
    dots = [tuple(map(int, line.split(","))) for line in raw_dots.split("\n")]

    fold_axis = raw_folds[11]
    fold_position = int(raw_folds.split()[2][2:])

    new_dots = set()
    for x, y in dots:
        nx = x if fold_axis == "y" else fold_position - abs(x - fold_position)
        ny = y if fold_axis == "x" else fold_position - abs(y - fold_position)
        new_dots.add((nx, ny))
    
    return len(new_dots)


def part_2(data):
    raw_dots, raw_folds = data.split("\n\n")
    dots = set(tuple(map(int, line.split(","))) for line in raw_dots.split("\n"))
    folds = [tuple(line.split(" ")[-1].split("=")) for line in raw_folds.split("\n")]

    for fold_axis, fold_position in folds:
        new_dots = set()
        fold_position = int(fold_position)
        for x, y in dots:
            nx = x if fold_axis == "y" else fold_position - abs(x - fold_position)
            ny = y if fold_axis == "x" else fold_position - abs(y - fold_position)
            new_dots.add((nx, ny))
        dots = new_dots
    
    max_x = max(x for x, _ in dots) + 1
    max_y = max(y for _, y in dots) + 1
    return "\n" + "\n".join("".join("#" if (x, y) in dots else " " for x in range(max_x+1)) 
                            for y in range(max_y+1))


if __name__ == "__main__":
    with open("day_13_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
