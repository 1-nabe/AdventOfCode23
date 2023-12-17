# https://adventofcode.com/2023/day/16

import time
import os

# Directions for each possible field the beam can encounter
directions = {'up': {'.': (-1, 0, 'up'), '|': (-1, 0, 'up'), '-': (0, 0, 'h_split'), '\\': (0, -1, 'left'), '/': (0, 1, 'right')},
              'down': {'.': (1, 0, 'down'), '|': (1, 0, 'down'), '-': (0, 0, 'h_split'), '\\': (0, 1, 'right'), '/': (0, -1, 'left')},
              'left': {'.': (0, -1, 'left'), '|': (0, 0, 'v_split'), '-': (0, -1, 'left'), '\\': (-1, 0, 'up'), '/': (1, 0, 'down')},
              'right': {'.': (0, 1, 'right'), '|': (0, 0, 'v_split'), '-': (0, 1, 'right'), '\\': (1, 0, 'down'), '/': (-1, 0, 'up')}
              }

if __name__ == "__main__":
    begin = time.perf_counter()
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    f = open(curr_dir + '/' + 'input.txt')
    lines = f.readlines()

    # Create matrix of chars
    matrix = []
    for line in lines:
        matrix.append(list(line.strip()))

    # Create a copy of the matrix to keep track of energized fields
    energized_matrix = []

    def clear_matrix():
        cleared_matrix = []
        for i in range(len(matrix)):
            new_row = [''] * len(matrix[0])
            cleared_matrix.append(new_row)
        return cleared_matrix

    def start_beam(start_index, direction):
        energized_matrix = clear_matrix()
        follow_path(start_index, direction, energized_matrix)
        sums.append(sum(x.count('#') for x in energized_matrix))

    def follow_path(index, curr_dir, energized_matrix):
        curr_index = index
        # Follow the path until the Beam leaves the matrix
        while curr_index[0] >= 0 and curr_index[0] < len(matrix) and curr_index[1] >= 0 and curr_index[1] < len(matrix[0]):
            # Update the current value
            curr_val = matrix[curr_index[0]][curr_index[1]]

            # For the current direction and value, get the next direction and index
            x, y, curr_dir = directions[curr_dir][curr_val]

            # If the current value is a split, follow both paths
            if curr_dir == 'h_split':
                if not energized_matrix[curr_index[0]][curr_index[1]] == '#':
                    follow_path(curr_index, 'left', energized_matrix)
                    follow_path(curr_index, 'right', energized_matrix)
                break
            elif curr_dir == 'v_split':
                if not energized_matrix[curr_index[0]][curr_index[1]] == '#':
                    follow_path(curr_index, 'up', energized_matrix)
                    follow_path(curr_index, 'down', energized_matrix)
                break
            else:
                # Energize the current field thats on the path of the beam
                energized_matrix[curr_index[0]][curr_index[1]] = '#'
                # Update the current index and value
                curr_index = (curr_index[0] + x, curr_index[1] + y)

    sums = []
    # For each field on the border, start a beam
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            start_index = (i, j)
            if j == 0:
                start_beam(start_index, 'right')
            if j == len(matrix[0]) - 1:
                start_beam(start_index, 'left')
            if i == 0:
                start_beam(start_index, 'down')
            if i == len(matrix) - 1:
                start_beam(start_index, 'up')

    # Energized Fields: 6883
    print(f"Part 1 - Energized Fields: {sums[0]}")

    # Energized Fields: 7228
    print(f"Part 2 - Max. Energized Fields: {max(sums)}")

    # Finished in: 0.481767s
    print(f"Finished in: {time.perf_counter() - begin:.6f}s")
