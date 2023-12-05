# AOC Day 1
# Author : Ruby
# 30th November 2023

# There is one elf carrying the most calories
# How many does that one hv?

# Create a list that holds all the calories of elves

# Empty List
elves = 0

# Open the flie
with open("./aoc2022day1.txt") as f :
    # Calories of the current elf
    current_cals = 0

    for line in f : 
        # if there is something in the line
        if line.strip() : 
            current_cals += int(line.strip())
        else :
            # dump current_cals into elves list
            elves.append(current_cals)
            # reset current_cals for next elves
            current_cals = 0

print (elves)

# find the biggest calories in the list
biggest_cals = 0
for elf in elves:
    if elf > biggest_cals:
        biggest_cals = elf
