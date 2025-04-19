import random
item_list = ["Rock","Paper","Scissors"] #variable-list
user_choice = input("Enter your choice : Rock, Paper, Scissors = ")
computer_choice = random.choice(item_list)
print(f"user choice = {user_choice}, computer choice = {computer_choice}")

if user_choice == computer_choice:
    print("Both chooses same: = Match Tie")

elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("paper covers Rock = Computer wins")
    else:
        print("Rock smashes Scissors = you win")
elif user_choice == "Paper":
    if computer_choice == "Scissors":
      print("Scissors cuts paper,computer wins")
    else:
        print("Paper covers rock, you win")
elif user_choice == "Scissor":
    if computer_choice == "Paper":
        print("Scissors cuts paper,you win")
    else:
        print("rock will smash scissor, computer wins")
