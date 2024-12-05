import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: Rock, Paper, or Scissors (or type 'quit' to exit).")

    choices = ["rock", "paper", "scissors"]

    while True:
        player_choice = input("\nYour choice: ").lower()

        if player_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break

        if player_choice not in choices:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice.capitalize()}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            print("🎉 You win!")
        else:
            print("💻 Computer wins!")

if __name__ == "__main__":
    rock_paper_scissors()

