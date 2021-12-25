import itertools


def part_1(data):
    width = len(data[0].strip())
    height = len(data)

    right_herd = {(x, y) for y, line in enumerate(data) for x, v in enumerate(line) if v == ">"}
    down_herd = {(x, y) for y, line in enumerate(data) for x, v in enumerate(line) if v == "v"}

    for i in itertools.count(1):
        next_right_herd = set()
        next_down_herd = set()
        changed = False

        herds = right_herd | down_herd
        for x, y in right_herd:
            next_position = ((x + 1) % width, y)
            if next_position not in herds:
                changed = True
                next_right_herd.add(next_position)
            else:
                next_right_herd.add((x, y))

        herds = next_right_herd | down_herd
        for x, y in down_herd:
            next_position = (x, (y + 1) % height)
            if next_position not in herds:
                changed = True
                next_down_herd.add(next_position)
            else:
                next_down_herd.add((x, y))

        if not changed:
            return i

        down_herd = next_down_herd
        right_herd = next_right_herd

    return None


if __name__ == "__main__":
    with open("day_25_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
