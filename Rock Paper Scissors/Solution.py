while True:
    Player1 = input("Rock? Paper? Scissors? ")
    Player2 = input("Rock? Paper? Scissors? ")
    if Player1 == Player2:
        print("It's a Draw!!")
    elif Player1 == "rock":
        if Player2 == "paper":
            print("Player2 wins!!")
        else:
            print("Player1 wins!!")
    elif Player1 == "paper":
        if Player2 == "rock":
            print("Player1 wins!!")
        else:
            print("Player2 wins!!")
    elif Player1 == "scissors":
        if Player2 == "rock":
            print("Player2 wins!!")
        else:
            print("Player1 wins!!")
    stop = input("Again? Yes or No? ")
    if stop == "no":
        print("Thanks for playing!!")
        break
