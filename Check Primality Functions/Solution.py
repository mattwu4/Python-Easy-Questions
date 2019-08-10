while True:
    number = input("Choose any number you want! ")
    number = int(number)
    if number == 2:
        print("PRIME!")
    elif number == 3:
        print("PRIME!")
    elif number == 5:
        print("PRIME!")
    elif number == 7:
        print("PRIME!")
    elif number == 11:
        print("PRIME!")
    elif (number % 2) == 0:
        print("NOT PRIME!!")
    elif (number % 3) == 0:
        print("NOT PRIME!!")
    elif (number % 5) == 0:
        print("NOT PRIME!!")
    elif (number % 7) == 0:
        print("NOT PRIME!!")
    elif (number % 11) == 0:
        print("NOT PRIME!!")
    else:
        print("PRIME!!")
