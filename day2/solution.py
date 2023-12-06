# https://adventofcode.com/2023/day/2

import re

# The maximum number of cubes for each color
rgb_config = [12, 13, 14]

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

    sum = 0
    lineId = 0
    for line in lines:
        impossible = False
        lineId += 1
        # Removes the game id
        _, games_line = line.split(':')

        # Splits the games into rounds
        game_rounds = games_line.split(';') 

        for game_round in game_rounds:
            rgb = []

            rgb.append(findCubes('red', game_round))
            rgb.append(findCubes('green', game_round))
            rgb.append(findCubes('blue', game_round))
            
            for i in range(len(rgb)):
                if rgb[i] > rgb_config[i]:
                    impossible = True
                    continue

        if not impossible:
            print("Line " + str(lineId) + " is possible!")
            sum += lineId

    print(sum)