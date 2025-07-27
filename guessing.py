"""
import random 

import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

x = random.randint(1,100)


import argparse as ap


def check (guess , target):

    if guess > target :
        print(f"Incorrect! The number is greater than {guess}")

    elif guess < target :
        print(f"Incorrect! The number is less than {guess}")

    else :
        print("Congratulations! You guessed the correct number")
        return True

p = ap.ArgumentParser("Number guessing game")
print("welcome")
p.add_argument("chance"  , type=int , choices=[1 ,2, 3] )

args= p.parse_args()

if args.chance == 2 :
    clear_terminal()
    print("you choose meduim ")
    i = 4
    while ( i != 0 ) :
        print(x)
        p1 = ap.ArgumentParser("meduim")
        p1.add_argument("guess" , type=int)
        z = p1.parse_args()
        t = check(z.guess , x)
        if t == True :
            print(f"you do it in {5-i}")
            break
        i = i-1
    

"""
import random
import argparse

def get_max_attempts(difficulty):
    return {
        'easy': 10,
        'medium': 5,
        'hard': 3
    }.get(difficulty, 5)  # Default to medium if input is invalid

def play_game(max_attempts):
    target = random.randint(1, 100)
    attempts = 0

    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} chances to guess the correct number.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess == target:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            return
        elif guess < target:
            print(f"Incorrect! The number is greater than your {guess}.")
        else:
            print(f"Incorrect! The number is less than your {guess}.")

    print(f"\nYou've run out of chances. The correct number was {target}.")

def main():
    p = argparse.ArgumentParser(description="CLI Number Guessing Game")
    p.add_argument("--show" , type=str , default="menu")
    p.add_argument('-d' , '--difficulty' , choices=['easy', 'medium', 'hard'], help="Choose difficulty level")
    
    args = p.parse_args()

    if args.show == "menu" :
        print("\nPlease select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        print("hint coding --> -d easy, medium, hard")
    if args.difficulty != None :
        print(f"\nGreat! You have selected the {args.difficulty.capitalize()} difficulty level.")
        print("Let's start the game!")

        max_attempts = get_max_attempts(args.difficulty)
        play_game(max_attempts)

if __name__ == '__main__':
    main()