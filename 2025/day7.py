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

# --
# Part 2
# --

# I think we're going to get a lot of repeated calculations here, so lets try caching (memoization) before my PC goes lol no, let's not do that and/or the program takes 3 million years to finish. 

import numpy as np
import functools
import time

# import data
filename = "Input/day7_input.txt"
lines = np.loadtxt(filename, dtype=str)
grid = [list(row) for row in lines]

# why as tuple? we need this for caching.
grid_tuple = tuple(tuple(row) for row in grid)

# how big is the grid?
ROWS, COLS = len(grid), len(grid[0])

def find_manifold(grid):
    """Return coordinates (r,c) of the tachyon manifold, where the tachyon particles start """
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "S":
                return (r, c)
    raise ValueError("No 'S' found in grid")

@functools.cache
def find_timelines(row, column, grid_tuple, ROWS, COLS):
    """
    Starting from the tachyon manifold, progress through the grid until the particle reaches a splitter "^" where the particle will split, or exit the bottom of the grid. 
    args:
        row, column : coordinates of the tachyon manifold
        grid_tuple (tuple): search grid in hashable format for caching
        ROWS, COLS: dimentions of the search grid
    """
    rr, cc = row, column
    while True:
        rr += 1  # move down one row

        # if out of bounds, the timeline terminates (count 1)
        if rr >= ROWS or cc < 0 or cc >= COLS:
            return 1

        cell = grid_tuple[rr][cc]
        if cell == ".":
            continue
        if cell == "^":
            # tachyon splitter found, split the timeline at this point, and explore how many timelines exist from this point. Yes, this is recursive, hence the caching decorator. No, I don't know how long this would take to complete on my potato of a rig without caching. 
            left = find_timelines(rr, cc - 1, grid_tuple, ROWS, COLS)
            right = find_timelines(rr, cc + 1, grid_tuple, ROWS, COLS)
            return left + right

start_time = time.time() 
start = find_manifold(grid)
timelines = find_timelines(start[0], start[1], grid_tuple, ROWS, COLS)
print(f"A single tachyon particle will experience {timelines:,} timelines.")
end_time = time.time()
print(f"{end_time-start_time:4f} to complete.")
