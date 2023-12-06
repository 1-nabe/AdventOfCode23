# https://adventofcode.com/2023/day/4

import sys

def cleanLine(line: str) -> tuple(str, str):
    tmp, cleanLine = line.split(':')
    winNum, myNum = cleanLine.split('|')
    winLines = winNum.split()
    myLines = myNum.split()
    return winLines, myLines

if __name__ == "__main__":
    sys.argv[1] if sys.argv[1] else 'example.txt'
    f = open('input.txt')
    lines = f.readlines()

    winsSum = 0
    copies = [1] * len(lines)
    lineCount = 0
    for line in lines:
        # Wins for the current Card (Double per win)
        lineWins = 0

        # Clean the line
        winNums, myNums = cleanLine(line)
        
        # Check for wins
        count = 0
        for num in myNums:
            if num in winNums:
                count += 1
                if(lineWins == 0):
                    lineWins = 1
                else:
                    lineWins *= 2
        for i in range(1, count + 1):
            copies[lineCount + i] += 1 * copies[lineCount]

        # Add the wins to the sum
        winsSum += lineWins
        lineCount += 1

    # Count the cards
    cardCount = 0
    for copy in copies:
        cardCount += copy

    print("Part 1: " + str(winsSum)) # 21919
    print("Part 2: " + str(cardCount)) # 9881048