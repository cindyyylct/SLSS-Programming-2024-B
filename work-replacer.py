# Emoji Replacer
# Cindy Li
# Feb 26, 2024

def translate(user_input):
    # Your block of code goes in here
    # Delete the pass and put in your own code
   
    # if user_input == "noodle"
    # return "🍜"
      # if user_input == "100":
    #     return "💯"
    return user_input.replace("noodle", "🍜").replace("100", "💯")

def main():
    # Ask the user to type something
    user_response = input("Enter something here:")  # "I like to eat noodles."

    # Use the translate function to replace words with emoji
    # Print the result
    print(translate(user_response))

# Test cases
# print(translate("Get to 100!"))
# print(translate("I like noodles."))
# print(translate("I love 100 noodles."))
# print(translate("noodle"))
# print(translate("100"))
main()