import math
from queue import PriorityQueue


def part_1(data):
    grid = [[int(i) for i in line.strip()] for line in data]

    pq = PriorityQueue()
    distance = {(x, y): math.inf for x in range(len(grid)) for y in range(len(grid[x]))}
    distance[(0, 0)] = 0
    pq.put((0, (0, 0)))

    while not pq.empty():
        _, (x, y) = pq.get()

        if (x, y) == (len(grid) - 1, len(grid[x]) - 1):
            return distance[(x, y)]

        for nx, ny in neighbours(grid, x, y):
            alternate = distance[(x, y)] + grid[nx][ny]
            if alternate < distance[(nx, ny)]:
                distance[(nx, ny)] = alternate
                pq.put((alternate, (nx, ny)))


def part_2(data):
    grid = [
        [((int(i) + (j + k - 1)) % 9) + 1 for j in range(5) for i in line.strip()]
        for k in range(5) for line in data
    ]

    pq = PriorityQueue()
    distance = {(x, y): math.inf for x in range(len(grid)) for y in range(len(grid[x]))}
    distance[(0, 0)] = 0
    pq.put((0, (0, 0)))

    while not pq.empty():
        _, (x, y) = pq.get()

        if (x, y) == (len(grid) - 1, len(grid[x]) - 1):
            return distance[(x, y)]

        for nx, ny in neighbours(grid, x, y):
            alternate = distance[(x, y)] + grid[nx][ny]
            if alternate < distance[(nx, ny)]:
                distance[(nx, ny)] = alternate
                pq.put((alternate, (nx, ny)))


def neighbours(grid, x, y):
    return [
        (x + dx, y + dy)
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]
        if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[x])
    ]


if __name__ == "__main__":
    with open("day_15_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
