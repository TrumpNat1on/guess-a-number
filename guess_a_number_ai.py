import random
import math

# config
low = 1
high = 100


# helper functions
def show_start_screen():
    print("*************************")
    print("****  Guess a Number A.I!  ****")
    print("*************************")

def show_credits():
    print("GOOODBYE!")
def get_guess(current_low, current_high):
    """
    Return a truncated average of current low and high.
    """
    average = ((current_low + current_high) // 2)
    return average

def pick_number():
    """
    Ask the player to think of a number between low and high.
    Then  wait until the player presses enter.
    """
    print("Think of a number between " + str(low) + " and " + str(high) + ".")
    input("Press Enter to continue...")
    
def check_guess(guess):
    """
    Computer will ask if guess was too high, low, or correct.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """
    print("")
    answer = input("Is " + str(guess) + " 'Too high', 'Too low', or 'Correct'?")
    if str.lower(answer) == "too high" or answer == "high":
        return 1
    elif str.lower(answer) == "too low" or answer == "low":
        return -1
    elif str.lower(answer) == "correct":
        return 0
    else:
        print("You didn't answer correctly")
def show_result(check):
    """
    Says the result of the game. (The computer might always win.)
    """
    if check == 0:
        print("Game over, I won!")
    pass

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
    check = -1
    
    pick_number()

    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            # adjust current_low
            current_low = guess
            pass
        elif check == 1:
            # adjust current_high
            current_high = guess

    show_result(guess)

# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()


