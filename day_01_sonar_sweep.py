import itertools


def part_1(data):
    return sum(b > a for a, b in itertools.pairwise(data))


def part_2(data):
    windows = zip(data, data[1:], data[2:])
    return sum(sum(b) > sum(a) for a, b in itertools.pairwise(windows))


if __name__ == "__main__":
    with open("day_01_input.txt", "r") as f:
        inp = [int(i) for i in f]
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
