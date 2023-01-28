from time import sleep
import random
import math


print("\nHello, Dear user this is a number guessing game.")
sleep(2)


amount_of_guesses = 0
random_digit = random.randint(1, 1000)
random_guess_help = 2


number_guess = int(input("\nGuess my number between 1 and 1000 (intergers only)\
 with the fewest possible guesses.\nPlease enter your first guess: "))

amount_of_guesses += 1


while True:

    if random_digit > number_guess:
        print("\nToo Low. Try again.")
        Too_low = random_digit - number_guess
        print(f"\nYou are too low by {math.ceil(Too_low/random_guess_help)} or more.")
        sleep(1)
        number_guess = int(input("\nEnter you next guess: "))
        amount_of_guesses += 1

    if random_digit < number_guess:
        print("\nToo High. Try again.")
        Too_high = number_guess - random_digit
        print(f"\nYou are too high by {math.ceil(Too_high/random_guess_help)} or more.")
        sleep(1)
        number_guess = int(input("\nEnter you next guess: "))
        amount_of_guesses += 1

    if random_digit == number_guess:
        print("\nCongratulations. You guessed the number!")
        print(f"\nAnd this only took you {amount_of_guesses} tries!")
        sleep(2)
        play_again = input("\nDo you desire to play again? (yes/no)")
        if play_again == "no":
            break
        if play_again == "yes":
            random_digit = random.randint(1, 1000)
            amount_of_guesses = 0
            number_guess = int(input("\nThank you for deciding to play again.\nPlease enter your new first guess: "))
            amount_of_guesses += 1