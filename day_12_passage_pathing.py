from collections import defaultdict


def part_1(data):
    links = defaultdict(list)
    for line in data:
        a, b = line.strip().split("-")
        links[a].append(b)
        links[b].append(a)

    def dfs(node, discovered=set()):
        if node == "end":
            return 1
        paths = 0
        for neighbour in links[node]:
            if neighbour not in discovered:
                discovering = {neighbour} if neighbour == neighbour.lower() else set()
                paths += dfs(neighbour, discovered | discovering)
        return paths

    return dfs("start", {"start"})


def part_2(data):
    links = defaultdict(list)
    for line in data:
        a, b = line.strip().split("-")
        links[a].append(b)
        links[b].append(a)

    def dfs(node, discovered=set(), visited_twice=False):
        if node == "end":
            return 1
        paths = 0
        for neighbour in links[node]:
            if neighbour not in discovered:
                discovering = {neighbour} if neighbour == neighbour.lower() else set()
                paths += dfs(neighbour, discovered | discovering, visited_twice)
            elif not visited_twice and neighbour != "start":
                paths += dfs(neighbour, discovered, True)
        return paths

    return dfs("start", {"start"})


if __name__ == "__main__":
    with open("day_12_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
