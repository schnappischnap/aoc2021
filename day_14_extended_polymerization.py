import itertools
from collections import Counter
from collections import defaultdict


def part_1(data):
    template, _, *raw_rules = [line.strip() for line in data]
    rules = {k: v for k, v in [line.split(" -> ") for line in raw_rules]}

    polymer = [c for c in template]
    for _ in range(10):
        new_polymer = [polymer[0]]
        for a, b in itertools.pairwise(polymer):
            new_polymer.extend([rules[a + b], b])
        polymer = new_polymer

    occurences = Counter(polymer).most_common()
    return occurences[0][1] - occurences[-1][1]


def part_2(data):
    template, _, *raw_rules = [line.strip() for line in data]
    rules = {k: v for k, v in [line.split(" -> ") for line in raw_rules]}

    pairs = defaultdict(int, {a + b: 1 for a, b in itertools.pairwise(template)})
    units = Counter(template)

    for _ in range(40):
        new_pairs = defaultdict(int)
        for pair, count in pairs.copy().items():
            new_pairs[pair[0] + rules[pair]] += count
            new_pairs[rules[pair] + pair[1]] += count
            units[rules[pair]] += count
        pairs = new_pairs

    occurences = units.most_common()
    return occurences[0][1] - occurences[-1][1]


if __name__ == "__main__":
    with open("day_14_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
