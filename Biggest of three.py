# Biggest of three
# Author : Ruby
# Date : 27th Nov 2023

def biggest_of_three(num_one: float, num_two: float, num_three: float) -> float:
    """Returns the biggest of three given numbers.

    Params:
    num_one - the first number
    num_two - the second number
    num_three - the third number

    Returns:
    the biggest of the three numbers
    """
    if num_one > num_two and num_one > num_three:
        return num_one
    elif num_two > num_three:
        return num_two
    else:
        return num_three


print(biggest_of_three(1000, 100, 10))
print(biggest_of_three(100, 1000, 10))
print(biggest_of_three(10, 100, 1000))
