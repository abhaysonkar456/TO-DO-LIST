# Number guessing game
import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
       guess = int(input(f"Attempt {attempts + 1}: Guess the number (1–100): "))



       if guess == secret_number:
        print("correct number guess by the user")
       elif guess > secret_number:
        print("too high")
       else:
        print("too low")

       attempts += 1

if attempts == max_attempts and guess != secret_number:
    print("max attempts had been reached, try again ")