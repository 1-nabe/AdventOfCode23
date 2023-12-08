# https://adventofcode.com/2023/day/3

import time
import numpy as np

symbols = ['*', '$', '+', '-', '%', '#', '&', '=', '/', '@']

if __name__ == "__main__":
    begin = time.perf_counter()
    f = open('input.txt')
    lines = f.readlines()
    M = np.array([list(line.strip()) for line in lines])
    
    def checkDigitLength(line, index):
        length = 1
        while lines[line][index + 1].isdigit():
            length += 1
            index += 1
        return length
    
    def checkSurrounding(line, index):
        length = checkDigitLength(lineId, index)

        up = -1
        down = 2
        left = -1
        right = 1
        
        if line == 0:
            up = 0
        if index + 2 > len(lines):
            down = len(lines) - 2
        if index == 0:
            left = 0
        if line + length > len(lines[line]):
            right = len(lines[line]) - line
        N = M[line+up:line+down, index+left:index+length+right]
        trues = np.in1d(N, symbols)

        return any(x for x in trues), length
    counter = 0
    motor_parts = []
    for lineId, line in enumerate(lines):
        for index, field in enumerate(line):
            if counter != 0:
                counter -= 1
                continue
            if field.isdigit():
                is_motor_part, length = checkSurrounding(lineId, index)
                if is_motor_part:
                    motor_parts.append(line[index:index + length])
                counter = length - 1
    
    print(f"Sum of motor parts: {sum([int(x) for x in motor_parts])}")
    print(f"Finished in: {time.perf_counter() - begin:.6f}s")