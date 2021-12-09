import math


def part_1(data):
    cave = [[int(i) for i in line.strip()] for line in data]
    w, h = len(cave), len(cave[0])
    return sum(cave[x][y] + 1
               for x in range(w)
               for y in range(h)
               if all(cave[x][y] < cave[nx][ny] for nx, ny in neighbours(cave, x, y)))


def part_2(data):
    cave = [[int(i) for i in line.strip()] for line in data]
    w, h = len(cave), len(cave[0])

    def search(x, y):
        size = 0
        queue = neighbours(cave, x, y)
        seen = set()
        while queue:
            x2, y2 = queue.pop()
            if (x2, y2) not in seen:
                seen.add((x2, y2))
                if cave[x2][y2] < 9:
                    size += 1
                    queue.extend(neighbours(cave, x2, y2))
        return size

    basins = []
    for x in range(w):
        for y in range(h):
            if all(cave[x][y] < cave[nx][ny] for nx, ny in neighbours(cave, x, y)):
                basins.append(search(x, y))
    return math.prod(v for v in sorted(basins)[-3:])


def neighbours(grid, x, y):
    return [
        (x + dx, y + dy)
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]
        if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[x])
    ]


if __name__ == "__main__":
    with open("day_09_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
