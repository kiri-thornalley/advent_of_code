# --
# Day 2: Gift Shop
import re

invalid_id = []

input = open("Input/day2_input.txt", "r")
    #split each range in the input, then turn into a tuple of integers
for line in input:
    ranges =line.strip().split(",")
    parsed_ranges = [tuple(map(int, r.split("-"))) for r in ranges]
    # print(parsed_ranges)

    # now turn each tuple into a list of integers, using list comprehension
    product_ids = [number for start,end in parsed_ranges for number in range (start, end+1)]
    #print(product_ids) # this is a flat list of all the product_ids that are in the database.

    for id in product_ids:
        id = str(id)
        match = re.fullmatch(r"(\d+)\1+", id) # match one or more digits that occurs once in the id
        if match: 
            id = int(id)
            invalid_id.append(id)
            print(f"Invalid ID detected {id}")
    total_sum = sum(invalid_id)
    print(f"The total sum of all invalid ids is: {total_sum}")
