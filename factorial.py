#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Nov. 1, 2022
# This program calculates the factorial value of an integer.


def main():

    # Initializing variables
    loop_counter = 0
    factorial_ans = 1

    # Gets the user's number as a string
    str_num = input("Enter a positive integer: ")

    # Tries casting the user's number to an integer
    try:
        int_num = int(str_num)

    # Tells the user to restart if they did not enter a number
    except ValueError:
        input("You must enter an integer. Please try again.")

    # Tells the user to restart if their number is negative
    if int_num < 0:
        input("You must enter a positive number. Please restart.")

    # Loops through body code until the counter is greater than
    # the user's number.
    while True:
        loop_counter += 1
        factorial_ans *= loop_counter
        print(f"Looped through {loop_counter} times.")
        if loop_counter >= int_num:
            break

    # Prints the factorial value of the user's number.
    print(f"{int_num}! = {factorial_ans}")


if __name__ == "__main__":
    main()
