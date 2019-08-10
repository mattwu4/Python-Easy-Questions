number = input('Choose any number : ')
number = int(number)
x = range(1, number)
for element in x:
    if (number % element) == 0:
        print(element)
