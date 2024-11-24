import random

def get_user_choice():
    """Get the player's choice."""
    print("Choose your weapon: Rock, Paper, or Scissors")
    user_choice = input().lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        user_choice = input().lower()
    return user_choice

def get_computer_choice():
    """Randomly get the computer's choice."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Play a game of Rock, Paper, Scissors."""
    print("Welcome to Rock, Paper, Scissors!")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"The computer chose: {computer_choice.capitalize()}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Start the game
if __name__ == "__main__":
    play_game()
