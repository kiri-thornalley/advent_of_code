# --
# Day 5: Cafeteria
# --

# Part 1: From the input given, calculate how many of the available ingredients are fresh.

# get input. split into fresh ingredient ID ranges, and ingredients.
fresh_ingredient_IDs = []
ingredients = []

with open("Input/day5_input.txt") as input:

    for line in input:
        line = line.strip()
        if not line:
            continue
        if "-" in line:
            fresh_ingredient_IDs.append(line)
        else:
            ingredients.append(line)

    # Debugging:
    # print(f"Here are the fresh ingredient ID ranges:\n {fresh_ingredient_IDs}")
    # print(f"Here are the ingredients:\n {ingredients}")


# turn each range into a tuple and we don't expand them out because the OS cried when I did that.
parsed_ranges = [tuple(map(int, item.split("-"))) for item in fresh_ingredient_IDs]
# print(parsed_ranges)

# for each ingredient_id, check in list of ranges
ingredients_fresh = 0

for item in ingredients:
    ingredient_id = int(item)
    for start, end in parsed_ranges:
        if start <= ingredient_id <= end:
            ingredients_fresh += 1
            break

print(f"There are {ingredients_fresh} fresh ingredients!")

# Part 2: From the input given, how many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?

fresh_id_count = 0
# sort the ranges
parsed_ranges.sort()

# merge overlap
merged_ranges = []

current_start, current_end = parsed_ranges[0]
for start, end in parsed_ranges[1:]:
    if start <= current_end + 1:
        current_end = max(current_end, end)
    else:
        merged_ranges.append((current_start, current_end))
        current_start, current_end = start, end

merged_ranges.append((current_start, current_end))  # this one appends the final range

# count how big the interval of each range is.
fresh_id_count += sum(end - start + 1 for start, end in merged_ranges)

print(f"Total fresh ingredient IDs in all ranges: {fresh_id_count}")
