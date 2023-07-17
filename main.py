import random

print("Welcome to the Number Guessing Game !")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
number_of_attempts = 0
if difficulty == "easy":
    number_of_attempts = 10


elif difficulty == "hard":
    number_of_attempts = 5

number = random.randint(1, 100)
while number_of_attempts >= 1:
    print(f"You have {number_of_attempts} attempts remaining to guess the number .")
    number_of_attempts -= 1
    guess = int(input("Make a guess : "))
    if number == guess:
        print("you win : your guess is correct ")
        break
    elif number < guess:
        print("Too high. ")
        print("Guess again. ")
    elif number > guess:
        print("Too Low. ")
        print("Guess again. ")
