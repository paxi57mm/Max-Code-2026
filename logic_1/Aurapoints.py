
import random

def guess_the_number():
   
    secret_number = random.randint(1, 10)
    print("I'm thinking of a number between 1 and 10.")

    #
    while True:
        guess = int(input("Take a guess: "))

        if guess == secret_number:
            print("Great job! You guessed it right.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Call the function
guess_the_number()
