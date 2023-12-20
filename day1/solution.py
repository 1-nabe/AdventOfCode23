# https://adventofcode.com/2023/day/1

from pathlib import Path
import re

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, 'input.txt')
EINPUT_PATH = Path(SCRIPT_PATH, 'input_example.txt')

if __name__ == "__main__":
    f = open(SCRIPT_PATH)
    lines = f.readlines()

    sum = 0
    for line in lines:
        # Find all the digits in the line
        digits = re.findall(r'\d+', line)

        # Construct the correct digit from the first and last digits of the line
        final_digit = int(digits[0] + digits[-1])

        # Add the digit to the sum
        sum += final_digit

    print(sum)
