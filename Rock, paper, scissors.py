#!/usr/bin/env python3.8

import random

while True:
    print("Make your guess:!", end="")
    guess = str(input())
    guess = guess.lower()
    choices = ['rock', 'paper', 'scissors']
    computer_guess = random.choice(choices)
    print("you guessed", guess)
    print("computer guessed", computer_guess)
    if guess in choices:
        if guess == computer_guess:
            print("it is a tie")
        elif guess == 'rock':
            if computer_guess == 'scissors':
                print("You win!")
            elif computer_guess == 'paper':
                print("Sorry, you lose!")
        elif guess == 'paper':
            if computer_guess == 'rock':
                print('You win!')
            elif computer_guess == 'scissors':
                print('Sorry, you lose!')
        elif guess == 'scissors':
            if computer_guess == 'paper':
                print("You win!")
            elif computer_guess == 'rock':
                print("Sorry you lose")
    break
