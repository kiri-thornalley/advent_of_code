# --
# Christmas Tree Farm
# --

# Part 1: Parse puzzle input and calculate how many of the regions in the list can successfully fit all the presents listed?

# Note: From the results reported by Blankestijn (https://theses.liacs.nl/pdf/2018-2019-BlankestijnMAN.pdf) Brute force absolutely will not work on the actual puzzle input we have been given. 

def parsing_input(file): 
    """ Parse input to get a list of present shapes, packing regions and the identity and quantity of presents that the elves will try and fit into the packing region. 
    Parameters:
        file (str): puzzle input
    Returns:
        present_shapes (dict): the shape and size of the presents
        packing_region: the area in which to pack the presents
        presents (list): list of presents to fit into packing region, index gives shape, number gives quantity
        """

    with open(file) as input:
        lines = [line.rstrip("\n") for line in input]

    # --
    # parse the shapes of the presents, and convert to coordinates
    # --
    present_shapes = {}
    packing_regions = []

    i = 0
    n = len(lines)

    while i < n:
        line = lines[i].strip()

        # --
        # parse the shapes of the presents, and convert to coordinates
        # --

        if line.endswith(":") and line[:-1].isdigit():
            shape_id = int(line[:-1])
            i += 1

            rows = []
            while i < n and lines[i].strip() and not lines[i].strip().endswith(":"):
                rows.append(lines[i].rstrip("\n"))
                i += 1

            coords = []
            for y, row in enumerate(rows):
                for x, ch in enumerate(row):
                    if ch == '#':
                        coords.append((x, y))

            if coords:
                min_x = min(x for x, _ in coords)
                min_y = min(y for _, y in coords)
                coords = [(x - min_x, y - min_y) for x, y in coords]

            present_shapes[shape_id] = coords
            continue

        if not line:
            i += 1
            continue

        # --
        # Parse the packing region and the number of presents to fit within
        # --

        if "x" in line and ":" in line:
            size_part, presents_part = line.split(":")
            w_str, h_str = size_part.split("x")

            width = int(w_str)
            height = int(h_str)
            presents = list(map(int, presents_part.strip().split()))

            packing_regions.append({
                "width": width,
                "height": height,
                "presents": presents
            })

        i += 1

    return present_shapes, packing_regions

def area_check(present_shapes, packing_regions):
    """
    Calculate the area of the packing region and the area covered by the presents in the list. If covered area will exceed the available area in the packing region, this puzzle is impossible to solve. 
    args:
        present_shapes: List of present shapes
        packing_regions: Dictionary containing packing region dimensions
    returns:
        bool: Returns false if the puzzle is impossible to solve.
    """
    packing_region_area = packing_regions["width"] * packing_regions["height"]

    total_present_area = 0
    for shape_id, count in enumerate(packing_regions["presents"]):
        if count == 0:
            continue
        shape_area = len(present_shapes[shape_id])
        total_present_area += count * shape_area
    return total_present_area <= packing_region_area


def presents_to_fit(present_shapes, packing_regions):
    """
    Calculate if the presents fit the packing region
    """
    presents_fit = 0
    
    # can quickly skip regions if area of presents > packing region)
    for region in packing_regions:
        if not area_check(present_shapes, region):
            print(f"Region is too small for the presents.")
            continue
        else:
    # neither of the two previous guard clauses have failed, so there must be a solution.
            presents_fit += 1
    return presents_fit

if __name__ == "__main__":
    file = "2025/Input/day12_input.txt"
    present_shapes, packing_regions = parsing_input(file)
    presents_fit = presents_to_fit(present_shapes, packing_regions)

    print(f"There are {presents_fit}/{len(packing_regions)} regions that can fit all of the presents listed!")


