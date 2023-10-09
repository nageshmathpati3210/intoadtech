import random

class NumberGuessingGame:
    def __init__(self):
        self.min_value = 1
        self.max_value = 100
        self.target_number = None
        self.attempts = 0
        self.max_attempts = 10
        self.player_name = ""

    def welcome_message(self):
        print("*************************************")
        print("*************************************")
        print("Welcome to the Number Guessing Game!")
        print("*************************************")
        print("*************************************")
        self.player_name = input("Enter your name: ")
        print(f"Hello, {self.player_name}! You have {self.max_attempts} attempts to guess the number between {self.min_value} and {self.max_value}.")

    def generate_random_number(self):
        self.target_number = random.randint(self.min_value, self.max_value)

    def get_player_guess(self):
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")
            return self.get_player_guess()

    def play_game(self):
        self.welcome_message()
        self.generate_random_number()

        while self.attempts < self.max_attempts:
            self.attempts += 1
            player_guess = self.get_player_guess()

            if player_guess < self.target_number:
                print("Too low! Try again.")
            elif player_guess > self.target_number:
                print("Too high! Try again.")
            else:
                self.display_result()
                break

        if self.attempts == self.max_attempts and player_guess != self.target_number:
            print(f"Sorry, {self.player_name}! You've run out of attempts. The number was {self.target_number}.")

        self.play_again()

    def display_result(self):
        print(f"Congratulations, {self.player_name}! You guessed the number {self.target_number} in {self.attempts} attempts.")

    def play_again(self):
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            self.reset_game()
            self.play_game()
        else:
            print("Thanks for playing!")

    def reset_game(self):
        self.attempts = 0
        self.target_number = None

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.play_game()
