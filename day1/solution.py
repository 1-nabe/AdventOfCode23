import re

if __name__ == "__main__":
    sys.argv[1] if sys.argv[1] else 'example.txt'
    f = open('input.txt')
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