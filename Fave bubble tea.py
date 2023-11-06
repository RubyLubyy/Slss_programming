# Bubble Tea Popularity Algorithm
# Author : Ruby
# Date : 27 October 2023

# Ask 5 users what their favourite bubble tea place is 
# Print out a summary of the data
NUM_RESPONDENTS = 5

coco_likes = 0
chatime_likes = 0
suntea_likes = 0
xingfutang_likes = 0
bbqueen_likes = 0
others = 0

for _ in range(NUM_RESPONDENTS):
    # Ask the user what their favourite bbt place is 
    print ("What's your favourite bubble tea")
    fave_bbt = input().strip(",.?! ").lower()

    # Tallying / Counting Algo
    # Options : CoCo, Chattie
    # If they say CoCo
    if fave_bbt == "coco": 
        coco_likes + 1
    elif fave_bbt == "chatime":
            chatime_likes += 1
    elif fave_bbt == "suntea":
            suntea_likes += 1
    elif fave_bbt == "xingfutang":
            xingfutang_likes += 1
    elif fave_bbt == "bbqueen":
            bbqueen_likes += 1
    else:
        others += 1

# Print out a summary
coco_percentage = coco_likes / NUM_RESPONDENTS * 100
chatime_percent = chatime_likes / NUM_RESPONDENTS * 100
suntea_percent = suntea_likes / NUM_RESPONDENTS * 100
xingfutang_percent = xingfutang_likes / NUM_RESPONDENTS * 100
bbqueen_percent = bbqueen_likes / NUM_RESPONDENTS * 100
other_percent = others / NUM_RESPONDENTS * 100


print(f"CoCo Likes : {coco_percentage}")
print(f"chatime Likes : {chatime_percent}")
print(f"SunTeaLikes : {suntea_percent}")
print(f"Xingfutang Likes : {xingfutang_percent}")
print(f"bbqueen Likes : {bbqueen_percent}")
print(f"other percent : {other_percent}")
