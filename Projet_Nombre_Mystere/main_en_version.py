import random

mystery_number = random.randint(1, 101)

number_of_attempts = 5

print("\033[92mWelcome to the Mystery Number Game!\033[0m")
print("\033[94mYou have to guess the mysterious number between 1 and 100.\033[0m")

while number_of_attempts > 0:
    user_guess = input("What is the mystery number according to you? ")

    if user_guess == str(mystery_number):
        print("CONGRATULATIONS! You have found the mystery number.")
        break  # Exit the loop if the correct number is guessed

    number_of_attempts -= 1

    if user_guess > str(mystery_number):
        print(f"The mystery number is smaller than {user_guess}.")
    elif user_guess < str(mystery_number):
        print(f"The mystery number is greater than {user_guess}.")

    print(f"\033[91mYou have {number_of_attempts} chance(s) left.\033[0m")

if number_of_attempts == 0:
    print(f"Sorry, you've run out of attempts. The mystery number was {mystery_number}.")


