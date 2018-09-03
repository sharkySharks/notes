
import random
from random import randrange

computerNumber = random.randrange(1,101)
attempts = 0

while True:
    guess = int(raw_input('Enter your guess: ' ))
    attempts += 1

    if guess == 'q' or guess == 'Q':
        break
    elif guess == computerNumber:
        print '{} <=== You got it in {} guesses!'.format(guess, attempts)
        break
    elif guess > computerNumber:
        print '{} IS TOO HIGH!'.format(guess)
    elif guess < computerNumber:
        print '{} is too loooow'.format(guess)
