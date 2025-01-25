#!/bin/env python

import sys
import random

def exit():
    sys.exit()

while True:
    try:
        user_input_level = int(input("Level: "))
        number = random.randint(1,user_input_level)
        user_guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        #print("Generated number: ", number)
        if user_guess == 0:
            continue
        elif user_guess > number:
            print("Too large!", end="")
            continue
        elif user_guess < number:
            print("Too small!", end="")
            continue
        elif user_guess == number:
            print("Just right!", end="")
            exit()
        else:
            continue