# --
# Day 4: Printing Department
# --
import numpy as np

# This looks to be a possible modification of Conway's game of life, but with far simpler rules - or atleast it does for part 1...

filename = "Input/day4_input.txt"
grid = np.loadtxt(filename, dtype="str")


def find_removable_rolls_part1(grid):
    """
    Finds all the removable rolls of paper in a single pass.
    params:
       grid (np.array): grid for processing
    returns:
        none
    """
    m, n = len(grid), len(grid[0])

    # directions of all 8 possible neighbours for each cell
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    # Convert grid to integers for easier processing
    int_grid = [[1 if c == "@" else 0 for c in row] for row in grid]

    # find and then mark the removable cells
    to_remove = []

    # iterate over the matrix
    for i in range(m):
        for j in range(n):
            neighbours = 0

            if int_grid[i][j] == 1:
                # check the neighbours
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    # if neighbour is in matrix and is occupied
                    if 0 <= x < m and 0 <= y < n and int_grid[x][y] == 1:
                        neighbours += 1
                # if fewer than 4 occupied neighbouring squares, the roll can be removed
                if neighbours < 4:
                    to_remove.append((i, j))

    # mark removable cells with 'x', on the original input grid
    output_grid = [list(row) for row in grid]
    for i, j in to_remove:
        output_grid[i][j] = "x"

    # Print the resulting grid
    for row in output_grid:
        print("".join(row))
    print(f" We have removed {len(to_remove)} rolls!")


def find_removable_rolls_part2(grid):
    """
    Finds all the removable rolls of paper in multiple passes.
    params:
       grid (np.array): grid for processing
    returns:
        none

    """
    m, n = len(grid), len(grid[0])

    # directions of all 8 possible neighbours for each cell
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    # Convert grid to integers
    int_grid = [[1 if c == "@" else 0 for c in row] for row in grid]

    # Whilst this code runs, keep a count of how many rolls we are able to remove
    total_removed = 0

    while (
        True
    ):  # whilst there are rolls still available to be removed, keep looping this code
        to_remove = []

        # find removable cells for this iteration
        for i in range(m):
            for j in range(n):
                if (
                    int_grid[i][j] == 1
                ):  # if this is an occupied cell, count how many neighbours are occupied
                    neighbours = 0
                    # check the neighbours
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        if 0 <= x < m and 0 <= y < n and int_grid[x][y] == 1:
                            neighbours += 1
                    # if fewer than 4 occupied neighbouring cells, the roll can be removed.
                    if neighbours < 4:
                        to_remove.append((i, j))
        # if no further rolls to remove, stop looping
        if not to_remove:
            break

        # remove the cells found this iteration
        for i, j in to_remove:
            int_grid[i][j] = 0

        # and then add how many cells we removed in this iteration to the total
        total_removed += len(to_remove)

    # Convert back to output format and print
    # output_grid = [['@' if cell == 1 else '.' for cell in row] for row in int_grid]
    # for row in output_grid:
    #    print("".join(row))
    print(f"We have removed {total_removed} rolls!")


if __name__ == "__main__":
    find_removable_rolls_part1(grid)
    find_removable_rolls_part2(grid)
