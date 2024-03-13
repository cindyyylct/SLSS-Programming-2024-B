# Unit 1 Activity – Song rater bot
# Cindy Li
# Mar 4, 2024


def main():
    # Asks the user for their favourite song,
    initial_response = input("What's your favourite song?")
    # Asks how they rate the melody & harmony on a scale of 1-5 and lyrics on a scale of 1-5
    melody_harmony = m_and_h (input("On a scale of 1-5, how would you rate the melody and harmony?"))
    # and lyrics on a scale of 1-5
    lyrics = l_ (input("How would you rate the lyrics? "))
   # Finally, multiply the inputs to get a final value and evaluates the overall mark of the song
    overall_score = melody_harmony * lyrics

    # Note: This is one way to round a number to two decimal places
    print(f"'{initial_response}' is {overall(overall_score)}")

# turn input numbers into integers
def m_and_h(mh):
    return float (mh)

# turn input numbers into integers
def l_(l):
    return float (l)

def overall(o):
    if o == 0:
        return "probably not your fav :("
    if 0 < o <= 10:
        return "a okay song"
    if 10 < o <= 20:
        return "a good song"
    if 20 < 0 < 25:
        return "a great song"
    if o == 25:
        return "your it song of the year!"
    else:
        return "..."
    
main()