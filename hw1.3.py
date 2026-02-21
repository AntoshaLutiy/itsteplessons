import random
a = random.randint(1, 10)
b=0
c = 3
while c!=0:
    b = int(input("Вибери число"))
    if b==a:
        print("Молодець")
        break
    if b<a:
        print("Більше")
    if b>a:
        print("Менше")
    c = c-1
