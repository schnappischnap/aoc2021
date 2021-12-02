def part_1(data):
    depth = 0
    position = 0
    
    for line in data:
        match line.split():
            case ["forward", amount]:
                position += int(amount)
            case ["down", amount]:
                depth += int(amount)
            case ["up", amount]:
                depth -= int(amount)

    return position * depth


def part_2(data):
    depth = 0
    position = 0
    aim = 0

    for line in data:
        match line.split():
            case ["forward", amount]:
                position += int(amount)
                depth += aim * int(amount)
            case ["down", amount]:
                aim += int(amount)
            case ["up", amount]:
                aim -= int(amount)

    return position * depth


if __name__ == "__main__":
    with open("day_02_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
