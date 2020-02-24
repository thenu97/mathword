#!/usr/bin/env python3.8

secret_number = float(input("Give me a number: "))
guess_count = 0
guess_limit = 4

while guess_count < guess_limit:
    guess = float(input("Guess the number: "))
    guess_count = guess_count + 1

    if guess == secret_number:
        print("That's right!!!")
        break
else:
    print("You reached your limit!")
    
    
