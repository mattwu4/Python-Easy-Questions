import random

a = random.randint(0,9)
b = random.randint(0,9)
c = random.randint(0,9)
d = random.randint(0,9)
while True:
    first = input("Choose your first number : ")
    second = input("Choose your second number : ")
    third = input("Choose your third number : ")
    fourth = input("Choose your fourth number : ")
    first = int(first)
    second = int(second)
    third = int(third)
    fourth = int(fourth)
    cow = 0
    bull = 0
    if first == a :
        cow = cow + 1
    elif first == b :
        bull = bull + 1
    elif first == c :
        bull = bull + 1
    elif first == d :
        bull = bull + 1
    else :
        cow = cow
        bull = bull
    if second == b :
        cow = cow + 1
    elif second == a :
        bull = bull + 1
    elif second == c :
        bull = bull + 1
    elif second == d :
        bull = bull + 1
    else :
        cow = cow
        bull = bull
    if third == c :
        cow = cow + 1
    elif third == b :
        bull = bull + 1
    elif third == a :
            bull = bull + 1
    elif third == d :
        bull = bull + 1
    else :
        cow = cow
        bull = bull
    if fourth == d :
        cow = cow + 1
    elif fourth == b :
        bull = bull + 1
    elif fourth == a :
        bull = bull + 1
    elif fourth == c :
        bull = bull + 1
    else :
        cow = cow
        bull = bull
    cow = str(cow)
    bull = str(bull)
    print(cow + " Cows", bull + " Bulls")
    if cow == "4" :
        print("Well Done!")
        break
