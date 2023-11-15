import random
number = random .randrange(0,100)
guess = int(input("Sisesta number 1-100: "))
while number!= guess:
    if guess < number:
        print("number liiga madal.")
        guess = int(input("Sisesta number uuesti: "))
    if guess > number:
        print("number liiga suur.")
        guess = int(input("Sisesta number uuesti: "))
    else:
     break
print("Teie nuber on õige")
        
