def part_1(data):
    output = [v.strip() for line in data for v in line.split(" | ")[1].split(" ")]
    return sum(len(v) in [2, 3, 4, 7] for v in output)


def part_2(data):
    result = 0
    for line in data:
        line = [set(v.strip()) for v in line.replace("|", "").split()]
        inputs, outputs = line[:10], line[10:]

        four = next(pattern for pattern in inputs if len(pattern) == 4)
        seven = next(pattern for pattern in inputs if len(pattern) == 3)
        
        output_value = []
        for output in outputs:
            match(len(output), len(four & output), len(seven & output)):
                case 2, _, _: output_value.append("1")
                case 3, _, _: output_value.append("7")
                case 4, _, _: output_value.append("4")
                case 5, 2, _: output_value.append("2")
                case 5, 3, 3: output_value.append("3")
                case 5, 3, 2: output_value.append("5")
                case 6, 4, _: output_value.append("9")
                case 6, 3, 3: output_value.append("0")
                case 6, 3, 2: output_value.append("6")
                case 7, _, _: output_value.append("8")

        result += int("".join(output_value))

    return result


if __name__ == "__main__":
    with open("day_08_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
