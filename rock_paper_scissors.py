import random
print("===== Rock Paper Scissors Game =====")
print("Instructions:")
print("Type rock, paper, or scissors to play.")
print("Type exit anytime to stop the game.\n")
user_score = 0
computer_score = 0
while True:
    print("\nChoose: rock / paper / scissors")
    user = input("Enter your choice: ").lower()
    if user == "exit":
        print("Game stopped")
        break
    if user not in ["rock", "paper", "scissors"]:
        print("Invalid input, try again")
        continue
    computer = random.choice(["rock", "paper", "scissors"])
    print("You:", user)
    print("Computer:", computer)
    if user == computer:
        print("It's a tie")
    elif user == "rock":
        if computer == "scissors":
            print("You win")
            user_score += 1
        else:
            print("Computer wins")
            computer_score += 1
    elif user == "paper":
        if computer == "rock":
            print("You win")
            user_score += 1
        else:
            print("Computer wins")
            computer_score += 1
    elif user == "scissors":
        if computer == "paper":
            print("You win")
            user_score += 1
        else:
            print("Computer wins")
            computer_score += 1
    print("Score -> You:", user_score, " Computer:", computer_score)
    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("\nFinal Score -> You:", user_score, " Computer:", computer_score)
        print("Thanks for playing")
        break
