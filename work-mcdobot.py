# McDonald's bot
# Cindy Li
# Feb 21, 2024

# Ask the user if they want fried in their meal or not
fries = input("Would you like fries in your meal? Please answer Yes or No. ")
fries = fries.strip().lower().strip("!")

# If they answer yes, reply "here's your meal and fries"
if fries == "yes":
    print("Here's your meal with fries, enjoy!")

# If they answer no, reply "here's your meal with no fries"
elif fries == "no":
    print("Here's your meal with no fries, enjoy!")

# for any other answers, reply "I didn't understand what you said"
else:
    print(f"Sorry I don't understand what is {fries}.")