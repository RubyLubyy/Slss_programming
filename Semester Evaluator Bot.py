# Semester Evaluator Bot
# Auhtor : Ruby
# Date : 6th Nov, 2023

# Ask how many courses is the user taking
print ("How many course are you taking?")
num_course = input()

# Number of questions = Number in input
for i in range(1,num_course):
    course_rating = float(input(f"How would you rate course {print(i)} out of 5? "))
for question in course_rating:
    print(question)
    # Check if the rating is within a valid range
    if 0 <= course_rating <= 5:
        total_rating += course_rating
        num_course += 1
    else:
        print("Invalid rating. Please enter a rating between 0 and 5.")



# Calculate the average rating
if num_course > 0:
    average_rating = total_rating / num_course
    print(f"Your average rating for {num_course} courses is: {average_rating:.2f}")
else:
    print("No valid courses rated. Unable to calculate average.")

# Give a comment based on the average
if average_rating < 1 or average_rating == 1 :
    print ("Ouch.")
elif average_rating > 3 :
    print ("Glad to hear that.")
else :
    print ("Not a bad semester.")