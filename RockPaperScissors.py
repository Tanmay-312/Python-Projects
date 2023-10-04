import random
user_choice = input("Enter your choice (rock, paper, scissors): ")
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
print("You chose:", user_choice, "and Computer chose:", computer_choice)
if user_choice == computer_choice:
    print("You both chose the same. So it is a TIE")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock destroys the scissors! You WIN")
    else:
        print("Paper coves the rock, You LOSE")
elif user_choice == "paper":
    if computer_choice == "scissors":
        print("Scissors Cuts the Paper in pieces, You LOSE")
    else:
        print("Paper covers the rock, You WIN")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper, You WIN")
    else:
        print("Rock destroys the scissors!, You LOSE")
else:
    print("watch your typing!!")
