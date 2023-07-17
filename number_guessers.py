'''
Number guessing games, human, linear search, and binary search
Each function has 3 arguments; tries, start, and stop. a random number between
start and stop will be picked that must be guessed within tries.
by patjcolon
Last updated 7/16/2023
'''

import random


def guess_random_num(tries: int=5, start: int=0, stop: int=10):
    '''
    human powered number guessing game. random number between start and stop
    is picked and must be guessed with tries
    '''
    winning_number = str(random.randint(start, stop))

    print(f"Pick a number between {start} and {stop}.")
    while tries > 0:
        print(f"You have {tries} tries left.")
        guess = input()
        print("Guessing", guess)
        tries -= 1
        if guess == winning_number:
            print(f"You got it right! The answer was {winning_number}.")
            return True
        elif guess > winning_number:
            print("Your guess was too high.")
        else:
            print("Your guess was too low.")
        print()
    print("You ran out of tries!")
    print(f"The answer was {winning_number}.")
    return False


def guess_random_num_linear(tries: int=5, start: int=0, stop: int=10):
    '''
    linear search algorithm powered number guessing game. random number
    between start and stop is picked and must be guessed within tries.
    this algorithm starts at start and guessing up by 1 each try
    '''
    winning_number = random.randint(start, stop)
    guess = start

    while tries > 0:
        print(tries, "tries remaining.")
        tries -= 1
        print("Guessing", guess)
        if guess == winning_number:
            print("Guessed correctly. Answer was", winning_number)
            return True
        print("Guess was too low.")
        guess += 1
        print()
    print("No tries remain!")
    print(f"The answer was {winning_number}.")
    return False


def guess_random_num_binary(tries: int=5, start: int=0, stop: int=31):
    '''
    binary search algorithm powered number guessing game. random number
    between start and stop is picked and must be guessed within tries.
    if the length of range start-stop is equal to or less than 2**tries, the
    binary search algorithm has a 100% chance of guessing correctly.
    '''
    winning_number = random.randint(start, stop)
    guess_options = [i for i in range(start, stop+1)]
    
    lower_bound = 0
    upper_bound = len(guess_options) - 1

    while tries > 0:
        print(f"You have {tries} tries remaining.")
        tries -= 1

        pivot = (lower_bound + upper_bound) // 2
        guess = guess_options[pivot]
        print("Guessing", guess)

        if guess == winning_number:
            print("You guessed correctly! The answer was", winning_number)
            return True
        elif guess > winning_number:
            print("Your guess is too high!")
            upper_bound = pivot - 1
        else:
            print("Your guess it too low!")
            lower_bound = pivot + 1

    print("You ran out of guesses.")
    print(f"The correct answer was {winning_number}.")
    
    return False
        

# if you know binary search alg you can win this 100% of the time
# guess halfway, add or subtract 1/4 -> +/- 1/8 -> +/- 1/16 . . .
# my wife's method has less than 100% accuracy but has been able to
#   guess in much fewer tries, even if i pick a leaf / guaranteed last try
#   for the the binary search method
guess_random_num(10, 0, 1023)

guess_random_num_linear(10, 0, 1023)
guess_random_num_binary(10, 0, 1023)
