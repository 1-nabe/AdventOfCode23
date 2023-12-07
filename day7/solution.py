# https://adventofcode.com/2023/day/6

from collections import defaultdict
import time

types = {'Five': 7, 'Four': 6, 'Full House': 5, 'Three': 4, 'Two': 3, 'One': 2, 'High': 1}

def check_type(counts):
    values = list(counts.values())
    values.sort(reverse=True)

    if values[0] == 5:
        return types['Five']
    elif values[0] == 4:
        return types['Four']
    elif values[0] == 3:
        if values[1] == 2:
            return types['Full House']
        else:
            return types['Three']
    elif values[0] == 2:    
        if values[1] == 2:
            return types['Two']
        else:
            return types['One']
    else:
        return types['High']
     

def count_chars(line):
        char_counts = defaultdict(int)

        for char in line:
            char_counts[char] += 1

        return char_counts

if __name__ == "__main__":
    begin = time.perf_counter()
    f = open('input.txt')
    lines = f.readlines()

    results = []
    for line in lines:
        line, bet = line.split(' ')
        result = count_chars(line)
        results.append((line, int(bet), result))

    ranks = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    for result in results:
        rank = check_type(result[2])
        ranks[rank].append(result)
    
    hand_value = 1
    sum = 0
    card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    for key, value in ranks.items():
        if not value:
            continue
        elif len(value) == 1:
            sum += value[0][1] * hand_value
            print(f"{hand_value}, {value[0][0]} : {value[0][1]}")
            hand_value += 1
        else:
            cards = {}
            for val in value:
                cards[val[0]] = (val[1], val[2])
            strings = [x[0] for x in value]
            # Sort initially based on the first character
            sorted_cards = sorted(strings, key=lambda x: card_values[x[0]] if not x[0].isdigit() else int(x[0]))
            # Sort based on the values of characters at each position
            sorted_cards = sorted(sorted_cards, key=lambda x: [card_values[char] if not char.isdigit() else int(char) for char in x])
            for card in sorted_cards:
                curr_card = cards[card]
                sum += curr_card[0] * hand_value
                print(f"{hand_value}, {card} : {curr_card[0]}")
                hand_value += 1

    print(f"Sum: {sum}")
    print(f"Finished in: {time.perf_counter() - begin:.6f}s")