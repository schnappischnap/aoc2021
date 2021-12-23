import functools
import math


def part_1(data):
    rooms = tuple(tuple(data[j][i] for j in range(2, 4)) for i in range(3, 10, 2))
    hallways = tuple(None for _ in range(11))

    return solve(rooms, hallways)


def part_2(data):
    rooms = tuple(tuple(data[j][i] for j in range(2, 4)) for i in range(3, 10, 2))
    extra = [("D", "D"), ("C", "B"), ("B", "A"), ("A", "C")]
    rooms = tuple(room[:1] + extra[i] + room[1:] for i, room in enumerate(rooms))
    hallways = tuple(None for _ in range(11))

    return solve(rooms, hallways, 4)


@functools.cache
def solve(rooms, hallways, room_size=2):
    # Solved
    if rooms == (("A",) * room_size, ("B",) * room_size, ("C",) * room_size, ("D",) * room_size):
        return 0

    best_cost = math.inf
    costs = {"A": 1, "B": 10, "C": 100, "D": 1000}

    # Try moving from hallway to room
    for position, amphipod in enumerate(hallways):
        if amphipod is None:
            continue

        destination_room_index = ord(amphipod) - 65

        destination_room = rooms[destination_room_index]
        if any(v != None and v != amphipod for v in destination_room):
            continue

        destination_position = (destination_room_index + 1) * 2
        min_position = min(position, destination_position)
        max_position = max(position, destination_position)
        if sum(hallways[i] != None for i in range(min_position, max_position + 1)) > 1:
            continue

        empty_spaces = destination_room.count(None)
        new_room = ((None,) * (empty_spaces-1) + (amphipod,) + destination_room[empty_spaces:])
        steps = abs(destination_position - position) + empty_spaces
        cost = steps * costs[amphipod]

        next_cost = solve(rooms[:destination_room_index] + (new_room,) + rooms[destination_room_index+1:],
                          hallways[:position] + (None,) + hallways[position+1:],
                          room_size)

        if cost + next_cost < best_cost:
            best_cost = cost + next_cost

    # Try moving from room to hallway
    for room_index, room in enumerate(rooms):
        will_move = False
        for amphipod in room:
            if amphipod is not None and ord(amphipod) - 65 != room_index:
                will_move = True
        if not will_move:
            continue

        empty_spaces = room.count(None)
        amphipod = room[empty_spaces]
        position = (room_index + 1) * 2
        for destination in [0, 1, 3, 5, 7, 9, 10]:
            steps = abs(destination - position) + empty_spaces + 1
            cost = steps * costs[amphipod]

            min_position = min(position, destination)
            max_position = max(position, destination)
            if not all(hallways[i] == None for i in range(min_position, max_position + 1)):
                continue

            new_room = (None,) * (empty_spaces+1) + room[empty_spaces+1:]

            next_cost = solve(rooms[:room_index] + (new_room,) + rooms[room_index+1:],
                              hallways[:destination] + (amphipod,) + hallways[destination+1:],
                              room_size)

            if cost + next_cost < best_cost:
                best_cost = cost + next_cost

    return best_cost


if __name__ == "__main__":
    with open("day_23_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
