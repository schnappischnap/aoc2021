def part_1(data):
    return simulate(data, 80)


def part_2(data):
    return simulate(data, 256)


def simulate(data, days):
    lanterns = [data.count(str(i)) for i in range(9)]
    for _ in range(days):
        lanterns = lanterns[1:] + lanterns[:1]
        lanterns[6] += lanterns[-1]
    return sum(lanterns)


if __name__ == "__main__":
    with open("day_06_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
