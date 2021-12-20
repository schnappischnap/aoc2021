def solve(data, part2 = False):
    algorithm, image = data.split("\n\n")
    algorithm = ["1" if c == "#" else "0" for c in algorithm]
    pixels = {
        (x, y): "1" if pixel == "#" else "0"
        for y, row in enumerate(image.split("\n"))
        for x, pixel in enumerate(row)
    }

    for i in range(50 if part2 else 2):
        next_pixels = dict()
        default_pixel = "0" if i % 2 == 0 else "1"

        for x, y in pixels:
            for neighbour in neighbours(x, y):
                index = "".join(
                    pixels.get((nx, ny), default_pixel)
                    for nx, ny in neighbours(*neighbour)
                )
                next_pixels[neighbour] = algorithm[int(index, 2)]

        pixels = next_pixels

    return sum(p == "1" for p in pixels.values())


def neighbours(x, y):
    return [(x + dx, y + dy) for dy in range(-1, 2) for dx in range(-1, 2)]


if __name__ == "__main__":
    with open("day_20_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(solve(inp)))
        print("Part 2: " + str(solve(inp, part2=True)))
