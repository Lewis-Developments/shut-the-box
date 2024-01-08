import os
import time
import colorama
from colorama import Fore, Back, Style

import random
from itertools import combinations as comb
from itertools import permutations as permu

colorama.init(autoreset=True)

os.system("cls")

def roll_dice():
    return random.randint(1, 6)

values_up = [1, 2, 3, 4, 5, 6, 7, 8, 9]
values_down = []


def display_down(numbers): 
    to_return = ""

    for i in range(1, 10):
        if i in numbers:
            to_return += f"{str(i)} "
        else:
            to_return += "  "

    
    return to_return


def values():
    temp_ustr = ""
    temp_dstr = ""
    for i in range(1, 10):
        if i in values_up:
            temp_ustr += " "
            temp_ustr += str(i)
        else:
            temp_dstr += " "
            temp_dstr += str(i)

    if len(temp_ustr) == 0:
        temp_ustr = ""

    if len(temp_dstr) == 0:
        temp_dstr = ""

    print(f"{Fore.GREEN}Up:    {display_down(values_up)}{Fore.RESET}")
    print(f"{Fore.RED}Down:  {display_down(values_down)}{Fore.RESET}")


def main(values_up, values_down):
    print("Welcome to the game of Shut the Box!\n")
    time.sleep(1)
    print("The goal of the game is to shut all the numbers.\n")
    time.sleep(1)
    print("You can shut numbers by rolling the dice and adding the numbers together.\n")
    time.sleep(1.25)
    print("You can shut numbers by themselves, or in pairs.\n")
    time.sleep(1)
    print("If you cannot shut any numbers, you lose.\n")
    time.sleep(1)
    print("You will be given two dice to roll.\n")
    time.sleep(2)
    print(f"{Fore.BLUE}Good luck!\n")
    input(f"Press enter to continue. {Fore.RESET}")
    os.system("cls")

    # Tutorial
    print("Let's start with a tutorial.")
    go_tut = input("Type x to skip tutorial, or press enter to continue.")
    if str(go_tut).lower() == "x":
        print("Skipping tutorial...")
    else:
        print(f"{Fore.BLUE}Tutorial text will be written in this color.{Fore.RESET}")
        #print(f"{Fore.BLUE}You can highlight the following text to see what this totals: {Back.BLACK}{Fore.BLACK}{dice1 + dice2}{Fore.RESET}{Back.RESET}")
        #run_tutorial()

    # Main game loop
    dice1 = 0
    dice2 = 0
    running_game = True
    while running_game:
        running = True
        correct_input = True
        while running: # Round loop
            # Display Values (at start of game)
            if correct_input:
                dice1 = roll_dice()
                dice2 = roll_dice()
            checking_failed = check_comb(values_up, dice1, dice2)
            if checking_failed:
                values()
                print(f"Your dice rolled a {dice1} and a {dice2}.")
                user_input = input("Type the numbers you want to shut, separated by a space. ")
                user_input = user_input.split(" ")
                for value in user_input:
                    try:
                        value = int(value)
                    except ValueError:
                        print("Invalid input. Enter a number.")
                        correct_input = False
                if correct_input:
                    #Rest of code
                    user_input = [int(i) for i in user_input]
                    correct_input = True
                    for value in user_input:
                        if value not in values_up:
                            print("Invalid input. Enter a number that is up.")
                            correct_input = False
                    if correct_input:
                        final_addition = 0
                        for value in user_input:
                            final_addition += value
                        if dice1 + dice2 == final_addition:
                            for value in user_input:
                                if value in values_up:
                                    values_up.remove(value)
                                    values_down.append(value)
                                    values_down.sort()
                
                # Check if game is over
                if len(values_up) == 0:
                    print("Congratulations! You shut the box!")
                    time.sleep(5)
                    values_up = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    values_down = []
                    correct_input = True
                    play_again()
            else:
                print("You cannot shut any numbers. You lose.")
                time.sleep(5)
                values_up = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                values_down = []
                correct_input = True
                play_again()
                
    # End game
    print("Thank you for playing Shut the Box!")
    print("We hope you enjoyed it!")
    time.sleep(5)
    quit()

def play_again():
    play_again = input("Would you like to play again? (y/n) ")
    if play_again.lower() == "y":
        main()
    else:
        print("Thank you for playing Shut the Box!")
        print("We hope you enjoyed it!")
        time.sleep(5)
        quit()
def check_comb(values_up, dice1, dice2):
    dice_to_get = dice1 + dice2
    die_total = dice1 + dice2
    for x in range(1, 10):
        todo = permu(values_up, x)
        for i in todo:
            if sum(i) == dice_to_get:
                return True
    return False

if __name__ == "__main__":
    main(values_up, values_down)