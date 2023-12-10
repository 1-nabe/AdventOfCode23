# https://adventofcode.com/2023/day/8

import time
import re

if __name__ == "__main__":
    begin = time.perf_counter()
    f = open('input.txt')
    lines = f.readlines()

    instructions = lines.pop(0).strip()
    mapped_instructions = [1 if char == 'R' else 0 for char in instructions]
    lines.pop(0)

    nodes = {}
    for i, line in enumerate(lines):
        matches = re.findall(r'\b[a-zA-Z]{3}\b', line)
        nodes[matches[0]] = [matches[1], matches[2]]

    curr = 'AAA'
    end = 'ZZZ'
    steps = 0
    while curr != end:
        for direction in mapped_instructions:
            curr = nodes[curr][direction]
            steps += 1

    print(f"Steps: {steps}")  # Steps: 12361
    # Finished in: 0.002538s
    print(f"Finished in: {time.perf_counter() - begin:.6f}s")
