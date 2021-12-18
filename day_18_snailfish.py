# https://github.com/benediktwerner/AdventOfCode/blob/master/2021/day18/sol.py
# Sorry for the eval.

import math
import itertools
import functools


def part_1(data):
    snailfish = functools.reduce(add, [eval(line) for line in data])
    return magnitude(snailfish)


def part_2(data):
    data = [eval(line) for line in data]
    return max(magnitude(add(a, b)) for a, b in itertools.permutations(data, 2))


def add_left(fish, value):
    if value is None:
        return fish
    if isinstance(fish, int):
        return fish + value
    return [add_left(fish[0], value), fish[1]]


def add_right(fish, value):
    if value is None:
        return fish
    if isinstance(fish, int):
        return fish + value
    return [fish[0], add_right(fish[1], value)]


def explode(fish, depth=0):
    if isinstance(fish, int):
        return False, None, fish, None  # pmsl

    l, r = fish
    if depth == 4:
        return True, l, 0, r

    exploded, l2, l, r2 = explode(l, depth + 1)
    if exploded:
        return True, l2, [l, add_left(r, r2)], None

    exploded, l2, r, r2 = explode(r, depth + 1)
    if exploded:
        return True, None, [add_right(l, l2), r], r2

    return False, None, fish, None


def split(fish):
    if isinstance(fish, int):
        if fish > 9:
            return True, [math.floor(fish / 2), math.ceil(fish / 2)]
        return False, fish

    l, r = fish
    splitted, l = split(l)
    if splitted:
        return True, [l, r]
        
    splitted, r = split(r)
    return splitted, [l, r]


def add(a, b):
    snailfish = [a, b]
    changed = True
    while changed:
        changed, _, snailfish, _ = explode(snailfish)
        if changed:
            continue
        changed, snailfish = split(snailfish)
    return snailfish


def magnitude(fish):
    if isinstance(fish, int):
        return fish
    return 3 * magnitude(fish[0]) + 2 * magnitude(fish[1])


if __name__ == "__main__":
    with open("day_18_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
