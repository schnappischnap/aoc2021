import numpy as np
import re
from collections import Counter


def part_1(data):
    grid = np.zeros((100, 100, 100), bool)

    for line in data:
        switch = line.startswith("on")
        x1, x2, y1, y2, z1, z2 = map(lambda v: int(v) + 50, re.findall("-?\d+", line))

        if not all(0 <= v <= 100 for v in [x1, x2, y1, y2, z1, z2]):
            continue

        grid[x1 : x2 + 1, y1 : y2 + 1, z1 : z2 + 1] = switch

    return grid.sum()


def part_2(data):
    cubes = Counter()

    for line in data:
        switch1 = 1 if line.startswith("on") else -1
        x1, x2, y1, y2, z1, z2 = map(lambda v: int(v) + 50, re.findall("-?\d+", line))

        new_cubes = Counter()
        for (x3, x4, y3, y4, z3, z4), switch2 in cubes.items():
            # Intersection of cubes.
            ix1, ix2 = max(x1, x3), min(x2, x4)
            iy1, iy2 = max(y1, y3), min(y2, y4)
            iz1, iz2 = max(z1, z3), min(z2, z4)

            if ix1 <= ix2 and iy1 <= iy2 and iz1 <= iz2:
                new_cubes[(ix1, ix2, iy1, iy2, iz1, iz2)] -= switch2
        
        if switch1 == 1:
            new_cubes[(x1, x2, y1, y2, z1, z2)] += 1

        cubes.update(new_cubes)
        
    return sum((x2-x1+1) * (y2-y1+1) * (z2-z1+1) * sign 
               for (x1, x2, y1, y2, z1, z2), sign in cubes.items())


if __name__ == "__main__":
    with open("day_22_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
