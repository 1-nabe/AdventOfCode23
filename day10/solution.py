# https://adventofcode.com/2023/day/10

import time
import numpy as np
import sys

# Directions for each pipe
directions = {'up': {'|': (-1, 0, 'up'), '7': (0, -1, 'left'), 'F': (0, 1, 'right')},
              'down': {'|': (1, 0, 'down'), 'J': (0, -1, 'left'), 'L': (0, 1, 'right')},
              'left': {'-': (0, -1, 'left'), 'L': (-1, 0, 'up'), 'F': (1, 0, 'down')},
              'right': {'-': (0, 1, 'right'), '7': (1, 0, 'down'), 'J': (-1, 0, 'up')}
              }

# Dictionary for mapping the chars to the correct symbols
mapping_symbols = {
    "F": "\u250F",
    "J": "\u251B",
    "L": "\u2517",
    "7": "\u2513",
    "|": "\u2503",
    "-": "\u2501",
}


def findFirstPipe(matrix, index):
    x, y = index
    # Check if ontop of the start is a connecting pipe
    curr_val = matrix[x-1][y]
    if curr_val in directions['up'].keys():
        return curr_val, (x-1, y), 'up'

    # Else check if under the start is a connecting pipe
    curr_val = matrix[x+1][y]
    if curr_val in directions['down'].keys():
        return curr_val, (x+1, y), 'down'

    # Else check if on the left of the start is a connecting pipe
    curr_val = matrix[x][y-1]
    if curr_val in directions['left'].keys():
        return curr_val, (x, y-1), 'left'

    # Else check if on the right of the start is a connecting pipe
    curr_val = matrix[x][y+1]
    if curr_val in directions['right'].keys():
        return curr_val, (x, y+1), 'right'


if __name__ == "__main__":
    begin = time.perf_counter()
    f = open('input.txt')
    lines = f.readlines()

    # Create matrix of chars
    matrix = []
    for line in lines:
        matrix.append(list(line.strip()))

    # Convert to numpy array and find start index
    np_array = np.array(matrix)
    index = np.where(np_array == 'S')
    start_index = (int(index[0][0]), int(index[1][0]))

    # Create new array with same shape as the og matrix
    new_array = np.full_like(np_array, ' ')
    new_array[start_index[0]][start_index[1]] = 'S'

    # Find the first pipe from the start index
    curr_val, curr_index, curr_dir = findFirstPipe(matrix, start_index)
    new_array[curr_index[0]][curr_index[1]] = curr_val

    # Follow the path until the end is found. Count the needed steps
    steps = 1
    while True:
        # For the current direction and value, get the next direction and index
        x, y, curr_dir = directions[curr_dir][curr_val]
        # Update the current index and value
        curr_index = (curr_index[0] + x, curr_index[1] + y)
        # Update the current value
        curr_val = matrix[curr_index[0]][curr_index[1]]
        steps += 1
        new_array[curr_index[0]][curr_index[1]
                                 ] = mapping_symbols.get(curr_val, 'S')
        # Check if the current value is the start. If so, we are done
        if curr_val == 'S':
            break

    # Print the array, that only contains the path
    np.set_printoptions(threshold=sys.maxsize)
    print(new_array)

    # Steps: 6738
    print(f"Steps: {int(steps/2)}")
    # Finished in: 0.006241s
    print(f"Finished in: {time.perf_counter() - begin:.6f}s")
