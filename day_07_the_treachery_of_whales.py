import statistics


def part_1(data):
    data = [int(i) for i in data.split(",")]
    target = round(statistics.median(data))
    return sum(abs(target - i) for i in data)


def part_2(data):
    data = [int(i) for i in data.split(",")]
    return min(
        sum((abs(i-j) * (abs(i-j)+1) // 2) for j in data) 
        for i in range(max(data))
    )


if __name__ == "__main__":
    with open("day_07_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
