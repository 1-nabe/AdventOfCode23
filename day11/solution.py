# https://adventofcode.com/2023/day/11

from collections import deque
import time
import numpy as np
import itertools


def shortest_path(pair):
    start = pair[0]
    end = pair[1]


def expand_universe(lines):
    new_lines = []
    for i, line in enumerate(lines):
        unique = set(line)
        new_lines.append(line)
        if len(unique) == 1:
            new_lines.append(line)
    return np.array(new_lines)


if __name__ == "__main__":
    begin = time.perf_counter()
    f = open('input_example.txt')
    lines = f.readlines()

    for i, line in enumerate(lines):
        lines[i] = list(line.strip())

    # Expand rows
    lines = expand_universe(lines)
    np_lines = np.array(lines)
    # Rotate array by 90 degrees
    rotated_lines = np.rot90(np_lines, k=1, axes=(1, 0))
    # Expand rows (columns)
    rotated_lines = expand_universe(rotated_lines)
    # Rotate array back by 90 degrees
    fully_expanded_lines = np.rot90(rotated_lines, k=1, axes=(0, 1))

    # Find all galaxies and pair them
    galaxies = np.where(fully_expanded_lines == '#')
    galaxy_index = np.asarray(galaxies).T.tolist()
    galaxy_pairs = list(itertools.combinations(galaxy_index, 2))

    # Define possible moves: up, down, left, right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(fully_expanded_lines), len(fully_expanded_lines[0])

    def shortest_path(start, end):
        # Initialize visited set to keep track of visited cells
        visited = set()

        # Initialize queue for BFS
        # Each element is a tuple: (cell, distance)
        queue = deque([(start, 0)])

        while queue:
            (current_cell, distance) = queue.popleft()

            if current_cell == end:
                return distance

            if current_cell in visited:
                continue

            visited.add(current_cell)

            # Explore possible moves
            for move in moves:
                new_cell = (current_cell[0] + move[0],
                            current_cell[1] + move[1])

                # Check if the new cell is within bounds and is not blocked
                if 0 <= new_cell[0] < rows and 0 <= new_cell[1] < cols and fully_expanded_lines[new_cell[0]][new_cell[1]] != 1:
                    queue.append((new_cell, distance + 1))

        # If no path is found
        return -1

    distances = 0
    for pair in galaxy_pairs:
        result = shortest_path(
            (pair[0][0], pair[0][1]), (pair[1][0], pair[1][1]))
        print(f"Pair: {pair} - Distance: {result}")
        distances += result

    print(f"Distances: {distances}")
    # Distances: 10494813
    print(f"Finished in: {time.perf_counter() - begin:.6f}s")
    # Finished in: 2585.824295s
