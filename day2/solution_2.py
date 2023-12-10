# https://adventofcode.com/2023/day/2

import re

# Finds the number of cubes for a color in a line, returns 0 if not found


def findCubes(color: str, line: str) -> int:
    cubeLine = re.findall(r'\b(?:[1-9]|1[0-9]|20)\s' + color + r'\b', line)

    if not cubeLine:
        return 0
    else:
        return int(cubeLine[0].split(' ')[0])


if __name__ == "__main__":
    f = open('input.txt')
    lines = f.readlines()

    max_sum = []
    for line in lines:
        # Removes the game id
        _, games_line = line.split(':')

        # Splits the games into rounds
        game_rounds = games_line.split(';')

        # Finds the max rgb values for each round
        max_rgb = [0, 0, 0]
        for game_round in game_rounds:
            r = findCubes('red', game_round)
            if r > max_rgb[0]:
                max_rgb[0] = r
            g = findCubes('green', game_round)
            if g > max_rgb[1]:
                max_rgb[1] = g
            b = findCubes('blue', game_round)
            if b > max_rgb[2]:
                max_rgb[2] = b

        # Calculates the product of the max rgb values
        prod = 1
        for i in range(len(max_rgb)):
            prod *= max_rgb[i]
        max_sum.append(prod)

    print(sum(max_sum))
