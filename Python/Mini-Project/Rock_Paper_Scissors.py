import random #computer pick a random choice
while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper,  or scissors\n").lower() #player picks one of those
    if player == computer:
        print("computer: ", computer) #print out computer choice
        print("player:", player) #print out player choice
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player:", player)
            print("You win!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player:", player)
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player:", player)
            print("You lose!")
        if computer == "paper":
            print("computer: ", computer)
            print("player:", player)
            print("You lose!")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player:", player)
            print("You lose!")
        if computer == "rock":
            print("computer: ", computer)
            print("player:", player)
            print("You win!")
    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Bye!")

