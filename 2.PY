import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to Guess the Number!")

    while True:
        try:
            user_guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("Please enter a valid guess between 1 and 100.")

            elif user_guess < secret_number:
                print("Too low! Try again.")

            elif user_guess > secret_number:
                print("Too high! Try again.")

            else:
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    guess_the_number()
