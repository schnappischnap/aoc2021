import operator as op
import functools


def solve(data):
    packet = "{:0{l}b}".format(int(data, 16), l=len(data) * 4)
    return read_packet(packet)[1:]


def read_packet(packet, i=0):
    version_sum = 0

    version = int(packet[i + 0 : i + 3], 2)
    type_id = int(packet[i + 3 : i + 6], 2)
    i += 6

    if type_id == 4:
        literal = ""
        running = True
        while running:
            running = packet[i] == "1"
            literal += packet[i + 1 : i + 5]
            i += 5
        return i, version, int(literal, 2)
    else:
        values = []
        if packet[i] == "0":
            length = int(packet[i + 1 : i + 16], 2)
            i += 16
            stop_i = i + length
            while i < stop_i:
                i, v, value = read_packet(packet, i)
                values.append(value)
                version_sum += v
        else:
            packet_count = int(packet[i + 1 : i + 12], 2)
            i += 12
            for _ in range(packet_count):
                i, v, value = read_packet(packet, i)
                values.append(value)
                version_sum += v
        func = [op.add, op.mul, min, max, None, op.gt, op.lt, op.eq][type_id]
        return i, version_sum + version, functools.reduce(func, values)


if __name__ == "__main__":
    with open("day_16_input.txt", "r") as f:
        inp = f.read().strip()
        part_1, part_2 = solve(inp)
        print("Part 1: " + str(part_1))
        print("Part 2: " + str(part_2))
