# https://adventofcode.com/2023/day/6

import re

def race(times, distances):
    solution = 1
    for i in range(len(times)):
        possibilities = 0
        for t in range(1, times[i]):
            if t * (times[i] - t) > distances[i]:
                possibilities += 1
        solution *= possibilities
    return solution

if __name__ == "__main__":
    f = open('input.txt')
    lines = f.readlines()

    timeStrings = re.findall(r'\d+', lines[0])
    distanceStrings = re.findall(r'\d+', lines[1])
    # Part 1
    times, distances = [[],[]]
    for i in range(len(timeStrings)):
        times.append(int(timeStrings[i]))
        distances.append(int(distanceStrings[i]))
    solution = race(times, distances)
    print(f"Part 1: {solution}")

    # Part 2
    time, distance = ['', '']
    for i in range(len(timeStrings)):
        time += timeStrings[i]
        distance += distanceStrings[i]
    solution = race([int(time)], [int(distance)])
    print(f"Part 2: {solution}")