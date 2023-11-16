# Calculating similarity score
# Author : Ruby
# 9th Nov, 2023

# Calculate similarity score between two people

# Create two lists that represent the movies that they like
ubials_fave_movies = [
    "the matrix",
    "avengers: infinity war",
    "infernal affairs",
    "rogue one",
    "the empires strikes back"
]

ben_fave_movies = [
    "thomas and friends, big world big adventure",
    "paddington 2",
    "avengers: infinity war",
    "rogue one"
]

similarity_score = 0

# For every movie in the first list
    # If that movie is in the second list
        # Increase similarity score if movie are the same
for movie in ubials_fave_movies : 
    if movie in ben_fave_movies :
        similarity_score += 1

# Display the results
print(f"The similarity score betweem the users is:")
print(similarity_score)