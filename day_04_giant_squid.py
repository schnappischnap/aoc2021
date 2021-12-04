def part_1(data):
    raw_calls, *raw_boards = data.split("\n\n")
    calls = {value: index for index, value in enumerate(map(int, raw_calls.split(",")))}

    boards = []
    for raw_board in raw_boards:
        board = [[int(v) for v in line.split(" ") if v != ""] for line in raw_board.split("\n")]
        boards.append(
            {
                "values": [v for line in board for v in line], 
                "lines" : [*board, *zip(*board)]
            }
        )

    fewest_calls = 100
    score = 0
    for board in boards:
        for line in board["lines"]:
            last_call, call_count = max((v for v in calls.items() if v[0] in line), key=lambda p: p[1])
            if call_count < fewest_calls:
                fewest_calls = call_count
                score = (sum(v for v in board["values"] if calls[v] > call_count) * last_call)
    return score


def part_2(data):
    raw_calls, *raw_boards = data.split("\n\n")
    calls = {value: index for index, value in enumerate(map(int, raw_calls.split(",")))}

    boards = []
    for raw_board in raw_boards:
        board = [[int(v) for v in line.split(" ") if v != ""] for line in raw_board.split("\n")]
        boards.append(
            {
                "values": [v for line in board for v in line], 
                "lines" : [*board, *zip(*board)]
            }
        )

    most_calls = 0
    worst_score = 0
    for board in boards:
        fewest_calls = 100
        score = 0
        for line in board["lines"]:
            last_call, call_count = max((v for v in calls.items() if v[0] in line), key=lambda p: p[1])
            if call_count < fewest_calls:
                fewest_calls = call_count
                score = (sum(v for v in board["values"] if calls[v] > call_count) * last_call)
        if fewest_calls > most_calls:
            most_calls = fewest_calls
            worst_score = score
    return worst_score


if __name__ == "__main__":
    with open("day_04_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
