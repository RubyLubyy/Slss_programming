# SFUs Best - Similarity Score
# Author: Ruby
# 10th November 2023

# Load data from a file
# "Read" it in a meaningful
# Link our Sim Score algo to the data

# Create a "profile" of likes (fave places in SFU)
profile = [
    "Bubble World",
    "Chef Hung",
    "Uncle Fatih's",
    "Guadalupe (MBC)",
    "Steve's Poke Bar"
]

# Initialize top score and their name
most_similar_score = 0
most_similar_name = " "
least_similar_score = float('inf')  # Initialize to positive infinity
least_similar_name = " "

with open("./data.csv") as f:
    # Throw away the header
    header = f.readline()

    for line in f:
        # Convert the string to a list
        current_likes = line.strip().split(",")

        # Store the person's name
        current_name = current_likes[0]  # Assuming the name is the first element
        
        # Initialize the current sim score
        current_sim_score = 0

        # Sim score algorithm
        for item in profile:
            if item in current_likes:
                current_sim_score += 1
        
        # Print the results from this line of data
        print(f"{current_name} - Score: {current_sim_score}")

        # Update the most similar person
        if current_sim_score > most_similar_score:
            most_similar_score = current_sim_score
            most_similar_name = current_name

        # Update the least similar person
        if current_sim_score < least_similar_score:
            least_similar_score = current_sim_score
            least_similar_name = current_name

print("🏅🏅🏅🏅 Most similar person! 🏅🏅🏅🏅")
print(f"{most_similar_name} - Score: {most_similar_score}")

print("👎👎👎 Least similar person! 👎👎👎")
print(f"{least_similar_name} - Score: {least_similar_score}")
