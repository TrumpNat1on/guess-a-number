#Guess A Number AI
#By: Nathan B
import random
import math

game_work = True
while game_work:
    name = input("Please enter your name: ")
    version = input(str(name) + ", would you like to play the player version where you guess the computers' number or the ai version where the computer guesses your number?")
    if str.lower(version) == "player":
        # helper functions

        def show_start_screen():
            print("*******************************")
            print("       **** Guess a Number ! ****")
            print("        ****Goodluck " + str(name) + "!****")
            print("*******************************")
        def show_credits():
            print("***************************")
            print("*This was made by Trump himself*")
            print("***************************")
            
        def get_guess():
            while True:
                guess = input("Guess a number " + str(name) + ":")

                if guess.isnumeric():
                    guess = int(guess)
                    return guess
                else:
                    print("You must enter a number " + str(name) + ".")

        def pick_number():
            print(str(name) + ", I'm thinking of a number from " + str(low) + " to " + str(high) +".")

            return random.randint(low, high)

        def check_guess(guess, rand):
            if guess < rand:
                print("")
                print("You guessed too low.")
            elif guess > rand:
                print("")
                print("You guessed too high.")

        def show_result(guess, rand):
            if guess == rand:
                print("You win!")
            else:
                print("You are sooooo stupid" + str(name) + "! The number was " + str(rand) + ".")

        def play_again():
            while True:
                decision = str.lower( input("Would you like to play again " + str(name) + "? (y/n) "))

                if str.lower(decision) == 'y' or decision == 'yes':
                    return True
                elif str.lower(decision) == 'n' or decision == 'no':
                    return False
                else:
                    print("")
                    print("I don't understand" + str(name) + ". Please enter 'y' or 'n'.")

        def play():
            guess = -1
            tries = 0

            rand = pick_number()
            
            while guess != rand and tries < limit:
                guess = get_guess()
                check_guess(guess, rand)

                tries += 1

            show_result(guess, rand)


        # Game starts running here
        show_start_screen()
        old_low = input("Please input the low that you wish the computer to use.....")
        old_high = input("Please input the high that you wish the computer to use.....")
        low = int(old_low)
        high = int(old_high)
        limit = math.ceil(math.log((high - low) + 1, 2))

        playing = True

        while playing:
            play()
            playing = play_again()

        show_credits()
        game_work = False

    elif str.lower(version) == "ai":
        #intelligence
        intelligence = 2

        
        # helper functions

        def show_start_screen():
            print("*************************")
            print("****** WELCOME TO ******")
            print("****  Guess a Number A.I!  ****")
            print("******** " + str(name) + "********")
            print("*************************")

        def show_credits():
            print("GOOODBYE!")

        def pick_number():
            """
            Ask the player to think of a number between low and high.
            Then  wait until the player presses enter.
            """
            print(str(name) + ", please think of a number between " + str(low) + " and " + str(high) + ".")
            input("Press enter to continue... ")

        def get_guess(current_low, current_high):
            """
            Return a truncated average of current low and high.
            """
            #versions
            if intelligence == 0:
                return random.randint(current_low, current_high)
            elif intelligence == 1:
                if current_high - current_low == 5 or current_high - current_low == 4 or current_high - current_low == 3 or current_high - current_low == 2 or current_high - current_low == 1:
                   return current_low + 1
                else:
                    return ((current_low + current_high) // 2)
            elif intelligence == 2:
                return ((current_low + current_high) // 2)
            
        def check_guess(guess, guess_used, current_low, current_high):
            """
            Computer will ask if guess was too high, low, or correct.

            Returns -1 if the guess was too low
                     0 if the guess was correct
                     1 if the guess was too high
            """
            print("")
            answer = input("Guess " + str(guess_used) + " of " + str(limit) + ". Is " + str(guess) + " 'Too high', 'Too low', or 'Correct' " + str(name) + "?")
            if current_high - current_low != 2:
                if str.lower(answer) == "too high" or answer == "high" or answer == "h":
                    return 1
                elif str.lower(answer) == "too low" or answer == "low" or answer == "l":
                    return -1
                elif str.lower(answer) == "correct" or answer == "c":
                    return 0
                else:
                    print("You didn't answer correctly " + str(name) + ".")
            elif current_high - current_low == 2:
                if str.lower(answer) == "correct" or answer == "c":
                    return 0
                else:
                    print("I think you did something wrong")
            else:
                print("I think something went wrong.")
        def show_result(check, guess_used):
            """
            Says the result of the game. (The computer might always win.)
            """
            
            if check == 0:
                print("Haha " + str(name) + "! Game over, I won in " + str(guess_used) + " tries!")
            pass

        def play_again():
            while True:
                decision = input("Would you like to play again " + str(name) + "? (y/n) ")

                if decision == 'y' or decision == 'yes':
                    return True
                elif decision == 'n' or decision == 'no':
                    return False
                else:
                    print("I don't understand " + str(name) + ". Please enter 'y' or 'n'.")

        def play():
            current_low = low
            current_high = high
            check = -1
            guess_used = 1
            pick_number()
            while check != 0 and guess_used <= limit:
                guess = get_guess(current_low, current_high)
                check = check_guess(guess, guess_used, current_low, current_high)
    
                if check == -1:
                    # adjust current_low
                    current_low = guess
                    guess_used = guess_used + 1
                elif check == 1:
                    # adjust current_high
                    current_high = guess
                    guess_used = guess_used + 1
            show_result(check, guess_used)
            print("")

        # Game starts running here
        show_start_screen()
        old_low = input("Please input the low that you wish the computer to use.....")
        old_high = input("Please input the high that you wish the computer to use.....")
        low = int(old_low)
        high = int(old_high)
        limit = math.ceil(math.log((high - low) + 1, 2))
        
        playing = True

        while playing:
            play()
            playing = play_again()
    
        show_credits()
        game_work = False
    else:
        print("Please enter computer or ai " + str(name) + ".")


      

