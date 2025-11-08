import random
import random

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")

random = random.randint(low, high)
ch = 7
gc = 0

while gc < ch:
    gc += 1
    guess = int(input("Enter your guess: "))

    if guess == random:
        print(f"Correct! The number is {guess}. You guessed it in {gc} attempts.")
        break
    elif guess >=  random and guess != random:
        print(f'Sorry! The number was {random}. Better luck next time.')
        break
    elif guess < random:
        print(f"Too low! Try a higher number.")
    elif guess > random:
        print(f"Too high! Try a lower number.")

