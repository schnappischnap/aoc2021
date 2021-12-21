import itertools
import functools


def part_1(data):
    positions = list(int(line.strip()[-1]) for line in data)
    scores = [0, 0]

    for i in itertools.count():
        player = i % 2
        roll = 6 + (9 * i)
        positions[player] = ((positions[player] + roll - 1) % 10) + 1
        scores[player] += positions[player]
        if scores[player] >= 1000:
            return scores[player - 1] * (i + 1) * 3

    return None


def part_2(data):
    positions = list(int(line.strip()[-1]) for line in data)
    return max(play_round(positions[0], positions[1]))


@functools.cache
def play_round(p1_pos, p2_pos, p1_score=0, p2_score=0):
    if p1_score >= 21:
        return 1, 0
    elif p2_score >= 21:
        return 0, 1

    scores = (0, 0)
    for dice in itertools.product([1, 2, 3], repeat=3):
        new_p1_pos = ((p1_pos + sum(dice) - 1) % 10) + 1
        new_p1_score = p1_score + new_p1_pos
        wins = play_round(p2_pos, new_p1_pos, p2_score, new_p1_score)
        scores = (scores[0] + wins[1], scores[1] + wins[0])
    return scores


if __name__ == "__main__":
    with open("day_21_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
