from functools import reduce


def part_1(data):
    closures = {"(": ")", "[": "]", "{": "}", "<": ">"}
    scoring = {")": 3, "]": 57, "}": 1197, ">": 25137}

    points = 0
    for line in data:
        expected = []
        for c in line.strip():
            if closure := closures.get(c):
                expected.append(closure)
            elif c != expected.pop():
                points += scoring[c]
                break
    return points


def part_2(data):
    closures = {"(": ")", "[": "]", "{": "}", "<": ">"}
    scoring = {")": 1, "]": 2, "}": 3, ">": 4}

    scores = []
    for line in data:
        expected = []
        for c in line.strip():
            if closure := closures.get(c):
                expected.append(closure)
            elif c != expected.pop():
                break
        else:
            scores.append(reduce(lambda x, y: x * 5 + scoring[y], reversed(expected), 0))

    return sorted(scores)[len(scores) // 2]


if __name__ == "__main__":
    with open("day_10_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
