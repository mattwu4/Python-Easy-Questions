import random

while True:
    guess = input("Guess a number between 1 and 9 : ")
    guess = int(guess)
    number = random.randint(1,9)
    if guess == number:
        print("Correct!!")
    elif guess > number:
        print("Too High!!")
    else:
        print("Too Low!!")
    guess = str(guess)
    number = str(number)
    print("Your guess : " + guess)
    print("Correct value : " + number)
    exit = input("Again? Yes or No? ")
    if exit == "no":
        print("Thanks for playing!!")
        break
    else:
        pass
