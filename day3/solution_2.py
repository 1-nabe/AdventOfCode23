# https://adventofcode.com/2023/day/3

import time

if __name__ == "__main__":
    begin = time.perf_counter()
    f = open('input.txt')
    lines = f.readlines()

    def checkLineForGear(line, start, end):
        for i in range(start, end + 1):
            field = lines[line][i]
            if field == '*':
                return (line, i)
        return (0, 0)

    def checkDigitLength(line, index):
        length = 1
        while lines[line][index + 1].isdigit():
            length += 1
            index += 1
        return length

    def checkSurrounding(line, index):
        length = checkDigitLength(lineId, index)
        gear_index = []
        # Check if the previous character is a symbol
        if lines[line][index - 1] == '*':
            gear_index.append((line, index - 1))
        # Check if the last character is a symbol
        if lines[line][index + length] == '*':
            gear_index.append((line, index + length))
        # Check if the previous line contains a symbol, if it exists
        if line != 0:
            tmp_gear_index = checkLineForGear(
                line - 1, index - 1, index + length)
            if tmp_gear_index != (0, 0):
                gear_index.append(tmp_gear_index)
        if line != len(lines) - 1:
            tmp_gear_index = checkLineForGear(
                line + 1, index - 1, index + length)
            if tmp_gear_index != (0, 0):
                gear_index.append(tmp_gear_index)
        return gear_index, length

    counter = 0
    gear_dict = {}
    for lineId, line in enumerate(lines):
        for index, field in enumerate(line):
            if counter != 0:
                counter -= 1
                continue
            if field.isdigit():
                gear_index, length = checkSurrounding(lineId, index)
                if len(gear_index) != 0:
                    for gear in gear_index:
                        if gear in gear_dict:
                            gear_dict[gear].append(line[index:index + length])
                        else:
                            gear_dict[gear] = [line[index:index + length]]
                counter = length - 1

    sum = 0
    for key, value in gear_dict.items():
        if len(value) > 1:
            sum += int(value[0]) * int(value[1])

    print(f"Sum of gear ratio: {sum}")  # Sum of gear ratio: 69527306
    # Finished in: 0.002634s
    print(f"Finished in: {time.perf_counter() - begin:.6f}s")
