import random

while True:
    a = ["q","w","e","r","t","y","u","i","o","p","l","k","j","h","g","f","d","s","a","m","n","b","v","c","x","z"]
    b = ["Q","W","E","R","T","Y","U","I","O","P","l","K","J","H","G","F","D","S","A","M","N","B","V","C","X","Z"]
    c = ["1","2","3","4","5","6","7","8","9","0"]
    d =["!","@","$","%","^","&","*","_","-","=","+"]
    i = random.randint(0,25)
    j = random.randint(0,25)
    k = random.randint(0,9)
    l = random.randint(0,10)
    print(a[i]+b[j]+c[k]+d[l])
    ask = input("Happy or not? Yes / No : ")
    if ask == "no" :
        pass
    else:
        break
