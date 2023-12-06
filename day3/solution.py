# https://adventofcode.com/2023/day/3

import time

symbols = ['*', '$', '+', '-', '%', '#', '&', '=', '/', '@']

if __name__ == "__main__":
    begin = time.perf_counter()
    f = open('input.txt')
    lines = f.readlines()

    def checkLineForSymbol(line, start, end):
        for i in range(start, end + 1):
            if lines[line][i] in symbols:
                return True
        return False
    
    def checkDigitLength(line, index):
        length = 1
        while lines[line][index + 1].isdigit():
            length += 1
            index += 1
        return length
    
    def checkSurrounding(line, index):
        length = checkDigitLength(lineId, index)

        # Check if the previous character is a symbol
        if lines[line][index - 1] in symbols:
            return True, length
        # Check if the last character is a symbol
        if lines[line][index + length] in symbols:
            return True, length
        # Check if the previous line contains a symbol, if it exists
        if line != 1 and checkLineForSymbol(line - 1, index - 1, index + length):
            return True, length
        # Check if the next line contains a symbol, if it exists
        if line != len(lines) - 1 and checkLineForSymbol(line + 1, index - 1, index + length):
            return True, length
        return False, length
    
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