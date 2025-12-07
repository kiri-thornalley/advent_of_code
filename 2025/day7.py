# --
# Day 7: Laboratories
# --
import numpy as np

total_splits = 0

filename = "Input/day7_test.txt"
grid = np.loadtxt(filename, dtype="str")
grid = [list(row) for row in grid]
# print(grid)

# how big is the grid?
m, n = len(grid), len(grid[0])
# print(m,n)

# use set to hold splitter locs for speed
all_splitters = set()

for i in range(m):
    # find tachyon beam manifold, marked a S in input
    if i ==0:
        all_splitters.add(grid[i].index("S"))
        continue
    search_positions = set()
    for position in all_splitters:
        # if splitter found
        if grid[i][position] == "^":
            search_positions.add(position - 1)
            search_positions.add(position + 1)
            total_splits += 1
        else:
            search_positions.add(position)
    all_splitters = search_positions

print(f"The beam is split {total_splits} times!")

