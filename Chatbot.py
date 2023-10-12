# Chatbot
# Author: Ruby
# Date: 21th September,2023

import random
import time

# Greet the user
# Pause between lines
print("Hello, there 🤖")
time.sleep(2)
print("I'm a crude chatbot, here to talk to you.")
time.sleep(1.5)

# Get the user's name and store in a variable
user_name = input ("So... what's your name?")

# Respond with the user name
print(f"It's nice to meet u, {user_name}")
time.sleep(2)

# Ask the user what their favourite food
fave_food = input ("What is ur favourite food?")

# If they answer pasta, respond with something related
if fave_food == "pasta" :
    print("🍝")
    print("I think I love pasta too")
elif fave_food == "burgers" or fave_food == "Burgers":
    print("🍔")
    print("Mmmmm, burgers")
elif fave_food == "Sushi" or "sushi" : 
    print("🍣")
    print("Delicious")
else :
    # Respond with something that is NOT TOO repititive
    # Create a list of appropriate responses
    list_of_fave_food_response=[
        "Mmmmm, that sounds delicious."
        f"Yes,{fave_food} is one of my favourite food too."
        "Interesting, I have never tried that before."
    ]
    # Choose one to response randomly
    import random
    random_response = random.choice (list_of_fave_food_response)

    # Print put the response
    print(random_response)

