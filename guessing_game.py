#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on November 2020
# This program is a guessing game

import random


def main():
    # this function compares a user input to a random number

    print("Today we will play a guessing game.")

    # random number generation
    random_number = random.randint(0, 9)

    # input
    user_guess = int(input("Enter a number between 0-9: "))
    print("")

    # process
    if user_guess == random_number:
        # output
        print("Correct! {} was the right answer."
              .format(random_number))
    else:
        # output
        print("Incorrect, try again!")


if __name__ == "__main__":
    main()
