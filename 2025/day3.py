# --
#Day 3: Lobby
# --

import itertools

final_joltage = []
file = "Input/day3_input.txt"

# Find maximum joltage for the battery banks. 
with open(file) as input:
    for battery in input:
        battery = battery.rstrip("\n")

        possible_joltage = []
        for joltage in list(itertools.combinations(battery, 2)):
            joltage = ''.join(joltage)
            possible_joltage.append(joltage)
        #print(possible_joltage)
        # sort list of possible joltages so that the largest possible value occupies position 0.
        possible_joltage.sort(reverse=True)
        #print(f"Ordered possible joltages: {possible_joltage}")
        final_joltage.append(possible_joltage[0])
    #print(final_joltage)
    # turn every entry in final_joltage into an interger, then add all the entries in the list
    final_joltage = list(map(int, final_joltage))
    total_joltage = sum(final_joltage)
    print(f"The total joltage in this battery bank when 2 batteries are used is: {total_joltage} jolts.")

# --
# Part 2: itertools.combinations(battery,12) works for the test input, borks process if we try to use the real input. Not a surprise when we realise that is O(n^12) time complexity, and 2x10^18 possible combinations. So lets rewrite things to use a Greedy algorithm.
# --

total_joltage = []
with open(file) as input:
    for battery in input:
        battery = battery.strip("\n")
        final_joltage = []
        batteries_needed = 12 
        start_index = 0
        while batteries_needed > 0:
            # shrink search space
            end = len(battery) - batteries_needed +1
            # choose the largest digit. key= tells program to compare the digits, not the indexes
            best_position = max(range(start_index,end), key=lambda i: battery[i])
            # append the digit
            final_joltage.append(battery[best_position])
            
            # move the search window forward by 1, and reduce the number of batteries remaining. 
            start_index = best_position +1
            batteries_needed -=1
        # join all the strings into a single number
        final_joltage = ''.join(final_joltage)
        #print(f"Printing final joltage: {final_joltage}")
        total_joltage.append(final_joltage)

    #print(f"Total_joltage {total_joltage}")
    # turn every entry in final_joltage into an interger, then add all the entries in the list
    total_joltage = sum(map(int, total_joltage))
    print(f"The total joltage in this battery bank when 12 batteries are used is: {total_joltage} jolts.")









