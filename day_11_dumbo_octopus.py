import itertools


def part_1(data):
    dumbos = [[int(i) for i in line.strip()] for line in data]
    flashes = 0

    for _ in range(100):
        dumbos = [[i + 1 for i in row] for row in dumbos]
        flashing = [(x, y) for x, row in enumerate(dumbos) for y, v in enumerate(row) if v > 9]

        while flashing:
            flashes += 1
            x, y = flashing.pop()
            for nx, ny in neighbours(dumbos, x, y):
                dumbos[nx][ny] += 1
                if dumbos[nx][ny] == 10:
                    flashing.append((nx, ny))

        dumbos = [[0 if i > 9 else i for i in row] for row in dumbos]

    return flashes


def part_2(data):
    dumbos = [[int(i) for i in line.strip()] for line in data]

    for i in itertools.count(1):
        dumbos = [[i + 1 for i in row] for row in dumbos]
        flashing = [(x, y) for x, row in enumerate(dumbos) for y, v in enumerate(row) if v > 9]
        flashes = 0

        while flashing:
            flashes += 1
            x, y = flashing.pop()
            for nx, ny in neighbours(dumbos, x, y):
                dumbos[nx][ny] += 1
                if dumbos[nx][ny] == 10:
                    flashing.append((nx, ny))

        dumbos = [[0 if i > 9 else i for i in row] for row in dumbos]

        if flashes == 100:
            return i


def neighbours(grid, x, y):
    return [
        (x + dx, y + dy)
        for dx in range(-1, 2)
        for dy in range(-1, 2)
        if (dx, dy) != (0, 0)
        and 0 <= x + dx < len(grid)
        and 0 <= y + dy < len(grid[x + dx])
    ]


if __name__ == "__main__":
    with open("day_11_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
