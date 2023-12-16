# https://adventofcode.com/2023/day/16

import time

# Directions for each pipe
directions = {'up': {'.': (-1, 0, 'up'), '|': (-1, 0, 'up'), '-': (0, 0, 'h_split'), '\\': (0, -1, 'left'), '/': (0, 1, 'right')},
              'down': {'.': (1, 0, 'down'), '|': (1, 0, 'down'), '-': (0, 0, 'h_split'), '\\': (0, 1, 'right'), '/': (0, -1, 'left')},
              'left': {'.': (0, -1, 'left'), '|': (0, 0, 'v_split'), '-': (0, -1, 'left'), '\\': (-1, 0, 'up'), '/': (1, 0, 'down')},
              'right': {'.': (0, 1, 'right'), '|': (0, 0, 'v_split'), '-': (0, 1, 'right'), '\\': (1, 0, 'down'), '/': (-1, 0, 'up')}
              }

if __name__ == "__main__":
    begin = time.perf_counter()
    f = open('input.txt')
    lines = f.readlines()

    # Create matrix of chars
    matrix = []
    for line in lines:
        matrix.append(list(line.strip()))

    # Create a copy of the matrix to keep track of energized fields
    energized_matrix = [row[:] for row in matrix]

    def follow_path(index, curr_dir):
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
                    follow_path(curr_index, 'left')
                    follow_path(curr_index, 'right')
                break
            elif curr_dir == 'v_split':
                if not energized_matrix[curr_index[0]][curr_index[1]] == '#':
                    follow_path(curr_index, 'up')
                    follow_path(curr_index, 'down')
                break
            else:
                # Energize the current field thats on the path of the beam
                energized_matrix[curr_index[0]][curr_index[1]] = '#'
                # Update the current index and value
                curr_index = (curr_index[0] + x, curr_index[1] + y)

    # Follow the path of the beam, starting at the top left corner to the right
    follow_path((0, 0), 'right')

    # Count the number of energized fields
    energized_fields = sum(x.count('#') for x in energized_matrix)

    # Energized Fields: 6883
    print(f"Energized Fields: {energized_fields}")

    # Finished in: 0.002555s
    print(f"Finished in: {time.perf_counter() - begin:.6f}s")
