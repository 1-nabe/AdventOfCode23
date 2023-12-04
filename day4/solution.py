f = open('day4Input.txt')
lines = f.readlines()
winsSum = 0
copies = [1] * len(lines)
lineCount = 0
for line in lines:
    print(str(lineCount) + ":")
    # Wins for the current Card (Double per win)
    lineWins = 0

    # Clean the line
    tmp, cleanLine = line.split(':')
    winNum, myNum = cleanLine.split('|')
    winLines = winNum.split()
    myLines = myNum.split()
    
    # Check for wins
    count = 0
    for num in myLines:
        if num in winLines:
            count += 1
            if(lineWins == 0):
                lineWins = 1
            else:
                lineWins *= 2
    print("   " + str(count))
    for i in range(1, count + 1):
        copies[lineCount + i] += 1 * copies[lineCount]
    print("   " + str(copies))

    # Add the wins to the sum
    winsSum += lineWins
    lineCount += 1

# Count the cards
cardCount = 0
for copy in copies:
    cardCount += copy

print("Cards: " + str(cardCount)) # 9881048
print("Summe: " + str(winsSum)) # 21919