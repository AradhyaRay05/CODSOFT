import random

print("---- Welcome to the Rock - Paper - Scissors Game ----\n")
print("--- Get ready to test your luck and skill! ---\n")

options = ("rock", "paper", "scissors")
user_score = 0
computer_score = 0

while True:
    user_choice = input("Enter a choice (rock or  paper or scissors): ").lower()
    if user_choice not in options:
        print("Invalid choice. Please enter a valid choice.\n")
    else:
        computer_choice = random.choice(options)
        print(f"Your choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors'):
            print("You win!")
            user_score += 1
        elif (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            user_score += 1
        elif (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1
        print("User Score :",user_score) 
        print("Computer Score :",computer_score)
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
            
print("\nFinal scores are:")
print("User Score :",user_score) 
print("Computer Score :",computer_score)

print("Thanks for playing!")