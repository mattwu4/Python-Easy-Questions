ask = input("How many Fibonacci numbers would you like me to generate? ")
ask = int(ask)
i = 1
if ask == 1:
    c = [1]
    print(c)
if ask == 2:
    d = [1, 1]
    print(d)
if ask >= 3:
    b = [1, 1]
    while i < (ask - 1) :
        b.append(b[i] + b[i-1])
        i += 1
    print(b)
