import re


def part_1(data):
    target = list(map(int, re.findall(r"(-?\d+)", data)))
    _, x_max, y_min, _ = target
    
    # return -y_min * ((-y_min -1) // 2)

    max_height = 0
    for x in range(x_max + 1):
        for y in range(y_min, abs(y_min)):
            if (height := simulate(x, y, target)) and height > max_height:
                max_height = height
    return max_height


def part_2(data):
    target = list(map(int, re.findall(r"(-?\d+)", data)))
    _, x_max, y_min, _ = target

    return sum(
        simulate(x, y, target) is not False
        for x in range(x_max + 1)
        for y in range(y_min, abs(y_min))
    )


def simulate(dx, dy, target):
    x_min, x_max, y_min, y_max = target
    x, y = 0, 0
    max_height = 0
    while x < x_max and y > y_min:
        x += dx
        y += dy

        if y > max_height:
            max_height = y

        if x_min <= x <= x_max and y_min <= y <= y_max:
            return max_height

        dx = dx - dx // abs(dx) if dx != 0 else 0
        dy = dy - 1
        
    return False


if __name__ == "__main__":
    with open("day_17_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
