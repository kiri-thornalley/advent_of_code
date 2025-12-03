# --
# Day 1: Secret Entrance
# --

# Part 1 - the dial starts at 50, and has the numbers 0-99. L turns dial towards smaller numbers, R towards larger numbers.
# The password is equal to the number of times that the dial actually lands on 0. 

# Part 2 - the dial again starts at 50, but the password is actually equal to the number of times the dial passes through 0 on its way to it's new position

dial = 50
reaches_zero = 0
passthrough_zero = 0

with open("day1_input.txt") as input:
    for line in input:
        movement = int(line[1:])
        for i in range(movement):
            if line[0] == "L":
                dial = (dial - 1)%100 
                #print(f"Current position is: {dial}")
            else:
                dial = (dial + 1)%100
            if dial == 0:
                passthrough_zero +=1
        if dial ==0:
            reaches_zero +=1
    
        #print(f"The dial's new position is: {dial}")

    print(f"The password for part 1 is: {reaches_zero}")
    print(f"The password for part 2 is: {passthrough_zero}")

