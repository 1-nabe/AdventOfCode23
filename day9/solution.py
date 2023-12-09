# https://adventofcode.com/2023/day/9

import time

def calculate_difference(current_numbers):
        diff = []
        for i in range(1, len(current_numbers)):
            diff.append(current_numbers[i] - current_numbers[i - 1])
        return diff
    
def extrapolate(lines):
    extrapolated_sum = 0
    for line in lines:
        first_numbers = []
        last_numbers = []
        ended = False

        current_numbers = line
        while ended == False:
            first_numbers.append(current_numbers[0])
            last_numbers.append(current_numbers[-1])
            current_numbers = calculate_difference(current_numbers)

            unique_numbers = list(set(current_numbers))
            ended = len(unique_numbers) == 1 and unique_numbers[0] == 0
        
        extrapolated = 0
        for i in range(len(last_numbers)):
            extrapolated += last_numbers[i]
        extrapolated_sum += extrapolated
    return extrapolated_sum

if __name__ == "__main__":
    begin = time.perf_counter()
    f = open('input.txt')
    lines = f.readlines()
    lines = [list(map(int, line.split())) for line in lines]
    
    print(f"Part 1 - Extrapolated future sum: {extrapolate(lines)}") # Extrapolated future sum: 1955513104
    print(f"Part 2 - Extrapolated past sum: {extrapolate([list(reversed(line)) for line in lines])}") # Extrapolated past sum: 1131
    print(f"Finished in: {time.perf_counter() - begin:.6f}s") # Finished in: 0.008111s