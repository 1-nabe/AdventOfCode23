from pathlib import Path
import time

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, 'input.txt')
EINPUT_PATH = Path(SCRIPT_PATH, 'input_example.txt')


def parse_input(lines):
    data_list = [line.split() for line in lines.splitlines()]
    return data_list


def parse_color_code(color_code):
    return parse_num_dir(color_code[7]), parse_hex(color_code[2:7])


def parse_hex(hex):
    return int(hex, 16)


def parse_num_dir(num):
    match int(num):
        case 0: return 'R'
        case 1: return 'D'
        case 2: return 'L'
        case 3: return 'U'


def get_next_point(point, dir, dist):
    match dir:
        case 'R': return (point[0] + dist, point[1])
        case 'L': return (point[0] - dist, point[1])
        case 'U': return (point[0], point[1] - dist)
        case 'D': return (point[0], point[1] + dist)


def shoelace_formal(all_points, sum_dist):
    sum = 0
    for i in (range(len(all_points) - 1)):
        sum += all_points[i][0] * all_points[i + 1][1]
        sum -= all_points[i][1] * all_points[i + 1][0]
    sum += sum_dist
    return ((sum // 2) + 1)


def parse_points(data):
    curr_point = (0, 0)
    all_points = [curr_point]
    sum_dist = 0
    for line in data:
        curr_point = get_next_point(curr_point, line[0], int(line[1]))
        sum_dist += int(line[1])
        all_points.append(curr_point)
    return shoelace_formal(all_points, sum_dist)


if __name__ == '__main__':
    begin = time.perf_counter()
    f = open(INPUT_PATH)
    parsed_data = parse_input(f.read())

    cubic_meters = parse_points(parsed_data)
    # Cubic meters of lava: 74074
    print(f"Part 1 - Cubic meters of lava: {cubic_meters}")

    # Finished in: 0.000640s
    print(f"Finished in: {time.perf_counter() - begin:.6f}s")

    new_parsed_data = [parse_color_code(x[2]) for x in parsed_data]
    cubic_meters = parse_points(new_parsed_data)
    # Cubic meters of lava:
    print(f"Part 2 - Cubic meters of lava: {cubic_meters}")

    # Finished in:
    print(f"Finished in: {time.perf_counter() - begin:.6f}s")
