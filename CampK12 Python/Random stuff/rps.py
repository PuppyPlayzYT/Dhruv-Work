import random 
li = ["rock", "paper", "scissor"]
user_input = input("Welcome to Rock Paper and Scissor! Please type 'Rock', 'Paper' or 'Scissor' down below!\n")
user_input = user_input.lower()

computer_choice = random.choice(li)

if user_input == computer_choice:
    print("You selected", user_input,"And the computer chose", computer_choice,", Hence it was a tie!")
elif user_input == "rock" and computer_choice == "paper":
    print("You selected", user_input,"And the computer chose", computer_choice,", Hence the computer won!")
elif user_input == "rock" and computer_choice == "scissor":
    print("You selected", user_input,"And the computer chose", computer_choice,", Hence you win!")
elif user_input == "paper" and computer_choice == "scissor":
    print("You selected", user_input,"And the computer chose", computer_choice, ", Hence the computer won!")
elif user_input == "paper" and computer_choice == "rock":
    print("You selected", user_input,"And the computer chose", computer_choice,", Hence you win!")
elif user_input == "scissor" and computer_choice == "rock":
    print("You selected", user_input,"And the computer chose", computer_choice,", Hence the computer won!")
elif user_input == "scissor" and computer_choice == "paper":
    print("You selected", user_input,"And the computer chose", computer_choice,", Hence you win!")
else:
    print("You typed the wrong characters, please try again")