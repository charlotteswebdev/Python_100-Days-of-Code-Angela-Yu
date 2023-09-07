from Day_12_art import logo
print(logo)
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

number_answer = random.randint(1,100)

def play():
    difficulty_level = input("Choose a difficulty - 'easy' or 'hard': ").lower()
    if difficulty_level == 'easy':
        num_of_attempts = 10
    elif difficulty_level == "hard":
        num_of_attempts = 5
    while num_of_attempts != 0:
        print(f"You have {num_of_attempts} attempts remaining \n")
        guess = int(input("Make a guess: "))
        if guess > number_answer:
            print("Too high")
            num_of_attempts -= 1
        elif guess < number_answer:
            print("Too low")
            num_of_attempts -= 1
        else:
            print(f"Correct! The answer was {guess}.")
            return

        if num_of_attempts > 1:
            print("Guess again")

    print(f"You've run out of guesses, you lose!\nThe number was {number_answer}")

play()