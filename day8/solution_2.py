# https://adventofcode.com/2023/day/8

import time
import re
import math
import numpy as np

if __name__ == "__main__":
    begin = time.perf_counter()
    f = open('input.txt')
    lines = f.readlines()

    instructions = lines.pop(0).strip()
    mapped_instructions = [1 if char == 'R' else 0 for char in instructions]
    lines.pop(0)

    nodes = {}
    start_nodes = []
    for i, line in enumerate(lines):
        matches = re.findall(r'\b[a-zA-Z]{3}\b', line)
        nodes[matches[0]] = [matches[1], matches[2]]
        if matches[0][2] == 'A':
            start_nodes.append(matches[0])

    print(start_nodes)

    all_steps = []
    for curr in start_nodes:
        steps = 0
        while curr[2] != 'Z':
            for direction in mapped_instructions:
                curr = nodes[curr][direction]
                steps += 1
        all_steps.append(steps)

    print(f"Steps: {np.lcm.reduce(all_steps)}")  # Steps: 18215611419223
    # Finished in: 0.013985s
    print(f"Finished in: {time.perf_counter() - begin:.6f}s")
