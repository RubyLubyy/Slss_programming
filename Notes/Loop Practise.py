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

