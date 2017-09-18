import random
#config
low = 1
high = 10
limit = 4

#helper functions
def get_guess():
    while True:
        g = input("Take a guess: ")

        if g.isnumeric():
            g = int(g)
            return g
        else:
            print("You must enter a number.")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == "y" or decision == "yes":
            return True
        elif decision == "n" or decision == "no":
            return False

        print("I don't understand. Please answer 'y' or 'n'.")

again = True

while again:
    #start game
    rand = random.randint(low, high)
    print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

    guess = -1
    tries = 0

    #play the game
    while guess != rand and tries < limit:
        guess = get_guess()
        
        if guess < rand:
            print("You guessed too low.")
        elif guess > rand:
            print("You guessed too high.")
        
        tries += 1
       
    #game over
    if tries == rand:
        print("You win!")
    else:
        print("You're stupid and should just quit playing! The real number was " + str(rand) + ".")

    again = play_again()

print("Goodbye.")
