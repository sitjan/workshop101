import random


def get_user_choice():
    """Get user's choice of 'scissor', 'paper', or 'rock'."""
    while True:
        user_choice = input(
            "Enter your choice (scissor/paper/rock): ").strip().lower()
        if user_choice in ['scissor', 'paper', 'rock']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'scissor', 'paper', or 'rock'.")


def get_computer_choice():
    """Generate computer's random choice of 'scissor', 'paper', or 'rock'."""
    return random.choice(['scissor', 'paper', 'rock'])


def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'scissor' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'rock' and computer_choice == 'scissor'):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    """Play a single round of the game."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}. Computer chose {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))

# Main function to run the game


def main():
    play_game()


if __name__ == "__main__":
    main()
