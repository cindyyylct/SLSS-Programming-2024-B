# Answer to the Great Question
# Cindy Li
# Feb 20th, 2024

# Ask the user for their answer to the great question
g_answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

# if they answer 4, forty-two, or forty two, respond YES
if g_answer == "42" or g_answer == "forty-two" or g_answer == "forty two":
    print("Yes.")

# if they answer anything else, respond NO
else:
    print("No.")