# https://adventofcode.com/2023/day/1

import sys
import re

number_word_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
string_int_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

# Get the digit from the string
def get_digit(n) -> str:
    try:
        return string_int_dict[n]
    except KeyError:
        return n

if __name__ == "__main__":
    sys.argv[1] if sys.argv[1] else 'example.txt'
    f = open('input.txt')
    lines = f.readlines()
    
    sum = 0
    for line in lines:
        # Find all the digits and digit strings in the line
        digits = re.findall(r'(?=(' + '|'.join(number_word_list + [str(i) for i in range(10)]) + r'))', line)

        # Construct the correct digit from the first and last digits of the line
        final_digit = int(get_digit(digits[0]) + get_digit(digits[-1]))
        
        # Add the digit to the sum
        sum += final_digit

    print(sum)