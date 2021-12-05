import re


def part_1(data):
    pattern = re.compile(r"\d+")
    points = set()
    overlaps = set()
    for line in data:
        x1, y1, x2, y2 = map(int, pattern.findall(line))
        dx = 1 if x2 > x1 else -1 if x1 > x2 else 0
        dy = 1 if y2 > y1 else -1 if y1 > y2 else 0
        if dx == 0 or dy == 0:
            distance = max(abs(x1 - x2), abs(y1 - y2)) + 1

            these_points = set((x1 + (dx * i), y1 + (dy * i)) for i in range(distance))
            overlaps.update(points & these_points)
            points.update(these_points)

    return len(overlaps)


def part_2(data):
    pattern = re.compile(r"\d+")
    points = set()
    overlaps = set()
    for line in data:
        x1, y1, x2, y2 = map(int, pattern.findall(line))
        dx = 1 if x2 > x1 else -1 if x1 > x2 else 0
        dy = 1 if y2 > y1 else -1 if y1 > y2 else 0
        distance = max(abs(x1 - x2), abs(y1 - y2)) + 1

        these_points = set((x1 + (dx * i), y1 + (dy * i)) for i in range(distance))
        overlaps.update(points & these_points)
        points.update(these_points)

    return len(overlaps)


if __name__ == "__main__":
    with open("day_05_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
