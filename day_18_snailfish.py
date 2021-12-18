import itertools
import functools
import re


def part_1(data):
    data = [line.strip() for line in data]
    return magnitude(functools.reduce(add, data))


def part_2(data):
    data = [line.strip() for line in data]
    return max(magnitude(add(a, b)) for a, b in itertools.permutations(data, 2))


def add(fish, new_fish):
    fish = "[" + fish + "," + new_fish + "]"

    while True:
        depths = itertools.accumulate(1 if v == "[" else -1 if v == "]" else 0 for v in fish)
        start = next((i for i, depth in enumerate(depths) if depth == 5), None)

        if start:
            stop = fish.index("]", start)
            left, right = fish[:start], fish[stop+1:]
            a, b = map(int, fish[start + 1 : stop].split(","))

            match = re.search("\d+", left[::-1])
            if match:
                value = int(match.group()[::-1]) + a
                left = left[:-match.end()] + str(value) + left[-match.start():]

            match = re.search("\d+", right)
            if match:
                value = int(match.group()) + b
                right = right[: match.start()] + str(value) + right[match.end() :]

            fish = left + "0" + right
        elif match := re.search("\d\d+", fish):
            value = int(match.group())
            fish = re.sub("\d\d+", f"[{value//2},{(value+1)//2}]", fish, 1)
        else:
            break

    return fish


def magnitude(fish):
    while True:
        if match := re.search("\[(\d+),(\d+)\]", fish):
            a, b = map(int, match.groups())
            fish = fish[: match.start()] + str(a * 3 + b * 2) + fish[match.end() :]
        else:
            break

    return int(fish)


if __name__ == "__main__":
    with open("day_18_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
