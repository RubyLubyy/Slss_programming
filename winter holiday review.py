# Winter Holiday Review
# Author : Ruby
# Date : 8th January 2024

# Requirements:
# - create a function called winter_holiday()
# - take one parameter
#   - string
# - return a summary of an event from your holidays

import random


def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter holidays 2023/24

    Params:
        good_or_bad - string that indicates whether the event
            is good or bad

    Returns:
        an event that happened to you during the holidays
        the event is selected part"""

    good_events = [
        "I got Lego for Christmas",
        "I spent time with family and friends.",
        "I ate a ton of delicious food.",
        "I finished Supar Mario Wonder.",
    ]
    bad_events = [
        "I didn't get what I wanted for Christmas.",
        "I ate too much delicious food.",
    ]

    if good_or_bad.strip().lower() == "good":
        return random.choice(good_events)
    elif good_or_bad.strip().lower() == "bad":
        return random.choice(bad_events)
    else:
        return "Sorry, I only take good or bad events."


def main() -> None:
    # Runs all the things we want to test in our .py file
    print(winter_holiday("good"))
    print(winter_holiday("bad"))
    print(winter_holiday("boogabooga"))


# If we're running THIS FILE using Python
if __name__ == "__main__":
    main()
