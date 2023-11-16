# Semester Evaluator Bot
# Auhtor : Ruby
# Date : 6th Nov, 2023

# Greet and ask for the number of courses
num_courses = int(input("How many courses are you taking this semester? "))
# Initialize total rating and course count
total_rating = 0
course_count = 0
# Ask for the rating for each course
for i in range(1, num_courses + 1):
    course_rating = (input(f"How would you rate course {i} out of 5? "))
for question in course_rating:
    print(question)


# Calculate the average rating
if num_courses > 0:
    course_rating = float(input().strip(",.?! "))
    average_rating = course_rating / num_courses
    print(f"Your average rating for {num_courses} courses is: {average_rating:.2f}")
else:
    print("No valid courses rated. Unable to calculate average.")

# Give a comment based on the average
if average_rating < 1 or average_rating == 1 :
    print ("Ouch.")
elif average_rating > 3 :
    print ("Glad to hear that.")
else :
    print ("Not a bad semester.")