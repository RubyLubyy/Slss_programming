# Loop Practise
# Author : Ruby
# Date : Tue 10th Oct, 2023

# Create a List of groceries
Groceries = ["hot wheels", "lego", "ice cream", "video games"]

# Eg.   * item
#         ---
#       * item 
#         ---
for item in Groceries : 
    print(f"* {item}")
    print("  ---")

# Create a pyramid like this using a for loop
Stars = ["*", "**", "***", "****", "*****"]

for item in Stars :
    print(f"{item}")
    print("---")

# Problem:
# Createa new years eve countdown
# Requirements:
# * Start off at 10
# * Countdown every second and print the second taht it's at
# * Instead of reaching zero it says "Happy New Year"
# * Example output

import time

countdown = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "HAPPY NEW YEAR!"]

for items in countdown:
    print(f"{items}")
    print("---")
    time.sleep(1)


# 1. Print all even numbers between 
#    1200 and 1500 inclusive.
#    Use a for loop.

for i in range(1200, 1501, 2):
    print(i)

# 2. Print all odd numbers between
#    -150 and 0 inclusive.

for i in range(-149, -1, 2):
    print(i)

# Once you have your solution,
# copy and paste your answer in #i-made-this
