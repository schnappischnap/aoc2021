from collections import Counter


def part_1(data):
    gamma = "".join(Counter(bits).most_common()[0][0] for bits in zip(*data))
    epsilon = "".join("1" if i == "0" else "0" for i in gamma)
    return int(gamma, 2) * int(epsilon, 2)


def part_2(data):
    oxygen = data[:]
    for i in range(12):
        bit_counts = Counter(line[i] for line in oxygen)
        most_common_bit = "0" if bit_counts["0"] > bit_counts["1"] else "1"
        oxygen = [line for line in oxygen if line[i] == most_common_bit]

    co2 = data[:]
    for i in range(12):
        bit_counts = Counter(line[i] for line in co2)
        least_common_bit = "1" if bit_counts["1"] < bit_counts["0"] else "0"
        co2 = [line for line in co2 if line[i] == least_common_bit]
        if len(co2) == 1:
            break

    return int(oxygen[0], 2) * int(co2[0], 2)


if __name__ == "__main__":
    with open("day_03_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
