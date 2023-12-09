# https://adventofcode.com/2023/day/9

import time

if __name__ == "__main__":
    begin = time.perf_counter()
    f = open('input.txt')
    lines = f.readlines()

    def calculate_difference(current_numbers):
        diff = []
        for i in range(1, len(current_numbers)):
            diff.append(current_numbers[i] - current_numbers[i - 1])
        return diff
    
    extrapolated_sum = 0
    for line in lines:
        last_numbers = []
        ended = False

        line = line.strip()
        current_numbers = [int(x) for x in line.split(' ')]
        while ended == False:
            last_numbers.append(current_numbers[-1])
            current_numbers = calculate_difference(current_numbers)
            
            unique_numbers = list(set(current_numbers))
            ended = len(unique_numbers) == 1 and unique_numbers[0] == 0
        
        extrapolated = 0
        for i in range(len(last_numbers)):
            extrapolated += last_numbers[i]
        extrapolated_sum += extrapolated

    print(f"Extrapolated sum: {extrapolated_sum}") # Extrapolated sum: 1955513104
    print(f"Finished in: {time.perf_counter() - begin:.6f}s") # Finished in: 0.004996s