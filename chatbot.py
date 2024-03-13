# Chatbot
# Cindy Li
# March 8, 2024

import random 
import time

# 1. Greets the user
print("Hello there!")
time.sleep(1.5)

# 2. Asks them: how are you? or something like that
print("How are you doing?")
user_feeling = input().strip(",.?!"). lower()

# 3. respond with a general statement
    # that is randomly chosen
    # create a list
if user_feeling == "good" or user_feeling == "great":
    good_possible_resp = ["I'm really happy for you!", "That's good news!", "That's awesome!"]
    chosen_response = random.choice(good_possible_resp)
    print(chosen_response)


    # randomly choose a response
    # print the response

elif user_feeling == "bad" or user_feeling == "not too good":
    bad_possible_resp = ["I'm sorry to hear that", "Hope that you'll feel better", "That's sad :("]
    chosen_response2 = random.choice(bad_possible_resp)
    print(chosen_response2)

else:
    else_possible_resp = ["Cool!", "Good!", ":)"]
    chosen_responseelse = random.choice(else_possible_resp)
    print(chosen_responseelse)

# 4. says goodbye
print("Well, thanks for your time :)")