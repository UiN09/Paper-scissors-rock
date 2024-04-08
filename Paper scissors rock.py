# Import random, set up variables for score, choice and for repeating

import random
repeat = True
ask_repeat = True
player_score = 0
fitzgerald_score = 0
play_again = "yes"


# define a thank you message
def thank_you():
    print("Thank you, kind person, for playing me in this battle.")
    if fitzgerald_score > player_score:
        print("Better luck next time old chap. I hope I see you again")
    elif fitzgerald_score == player_score:
        print("A draw, on my honour you are good.")
    else:
        print("Ahh, you are too good for me I fear, adventurer. You are more than a worthy adversary.")


# Define the function that will ask the player how many rounds they would like to play
def ask_rounds(question):
    while True:
        try:
            round_number = int(input(question))
            if round_number > 0:
                return round_number
                print(f"You are playing {round_number} rounds.")
            else:
                print("Please enter the number of rounds you would like to play (more than 1) or '999' if you want to play unlimited")
        except ValueError:
           print("Please enter the number of rounds you would like to play (more than 1) or '999' if you want to play unlimited")


# Define the function that will ask the player what choice they wnat to make
def ask_play_choice(question):
    while True:
        try:
            player_choice = input(question)
            if player_choice in ["parchment", "knife", "stone"]:
                return player_choice
            else:
                print("That will not work, Please enter 'parchment' 'knife' or 'stone")
        except ValueError:
            print("Please enter 'parchment' 'knife' or 'stone")


# Define the code that will ask the player if they would like the instructions
def want_instructions():
    while True:
        try:
            ask_instructions = input("Would you like to be presented with the rules for the competition?").lower()
            if ask_instructions in ["yes", "y"]:
                return ask_instructions
            elif want_instructions in ["no", "n"]:
                return ask_instructions
            else:
                print("Um, apoligies adventurer, I do not understand you.")
        except ValueError:
            print("Um, apoligies adventurer, I do not understand you.")


# display entry message
print("======================WELCOME========================\nNEW ADVENTURER TO YEE OLDE PARCHMENT, KNIFE, STONE 2.0")
print("My name is Fitzgerald and I will be your competitor in the coming battle of wits")

# Ask the player if they want to see the instructions, and if so print them.
instructions = want_instructions()
print(instructions)
if instructions == "yes" or "y":
    print('''
    -I will ask you how many rounds you would like to play.
    -Then I will ask you to pick an option (parchment, knife or stone)
    -Then I will make its own choice
    -I will then compare the two choices to find the winner ( "I'll be fair, I promise.")
    (Paper beats rock,
    rock beats scissors
    scissors beats paper
    if I and you pick the same thing it will be a draw.)
    -The scores depending on who won.
    -I will then ask you if you want to play again . 
    ''')
else:
    print("Ah, you have played this agme before then, I will not go easy on you then.")

# Spacers
print()
print()


# main program goes below
rounds = ask_rounds("By how many rounds will the victor be chosen?\n")  # Ask the user how many rounds they want to play.

# Repeat line code
while rounds > 0:

    # Ask user to make a choice.
    player_chose = ask_play_choice("What will be your mighty weapon traveller in the coming competition; 'parchment', 'knife' or 'stone'?")

    # spacers
    print()
    print()

    # Get the computer to make a choice.
    possible_action = ["parchment", "knife", "stone"]
    fitzgerald_choice = random.choice(possible_action)

    # Compare the choices and find the winner
    ask_repeat = True

    if fitzgerald_choice == player_chose:
        print("It's a draw")
        print("Fitzgerald Chose: ", fitzgerald_choice, "\nYou chose: ", player_chose, )

    elif player_chose == "parchment":
        if fitzgerald_choice == "knife":
            print("Fitzgerald Chose: ", fitzgerald_choice, "\nYou chose: ", player_chose, "\nYou Lose")
            fitzgerald_score = fitzgerald_score + 1
        else:
            print("Fitzgerald Chose: ", fitzgerald_choice, "\nYou chose: ", player_chose, " \nYou Win")
            player_score = player_score + 1

    elif player_chose == "knife":
        if fitzgerald_choice == "knife":
            print("Fitzgerald Chose: ", fitzgerald_choice, "\nYou chose: ", player_chose, "\nYou Win")
            player_score = player_score + 1
        else:
            print("Fitzgerald Chose: ", fitzgerald_choice, "\nYou chose: ", player_chose, " \nYou Lose")
            fitzgerald_score = fitzgerald_score + 1

    elif player_chose == "stone":
        if fitzgerald_choice == "parchment":
            print("Fitzgerald Chose: ", fitzgerald_choice, "\nYou chose: ", player_chose, " \nYou Lose")
            fitzgerald_score = fitzgerald_score + 1
        else:
            print("Fitzgerald Chose: ", fitzgerald_choice, "\nYou chose: ", player_chose, " \nYou win")
            player_score = player_score + 1
    else:
        print("My Apologies adventurer, but that will not do. Please check the spelling of your choice.")

    # spacers and print the score of each (player and computer)
    print()
    print(f"Fitzgerald score: {fitzgerald_score} \n Player Score: {player_score}")
    print()

    # Update the number of rounds they have played
    if rounds == 999:
        rounds = rounds
    else:
        rounds = rounds - 1

    # Ask the player if they would like to play again
    if ask_repeat == True:
        user_repeat = input("Care to play again adventurer?").upper()
        if user_repeat == "Y":
            repeat = True
            ask_repeat = False
            print("We have: ", rounds, "left to play")
        elif user_repeat == "N":
            repeat = False
            ask_repeat = False
        else:
            print("That will not work adventurer. Please enter only 'y' or 'n'")

    # if the player is out of rounds, ask them if they still want to play.
    if repeat == True:
        if rounds == 0:
            play_again = input("Oh no, you have no rounds left, would you still like to play?").lower()

        if play_again in ["yes", "y"] and rounds == 0:
            rounds = ask_rounds("Good choice adventurer, how many more rounds would you like to lose in?")
        elif play_again in ["yes", "y"] and rounds > 0:
            rounds = rounds
        else:
            rounds = rounds + 1
# If the player inputs "n" when the computer asks them if they would like to play again, print a thank-you
thank_you()

