import random
number = random.randint(1, 10)

guess = int(input("what is your guess?"))
for _ in range (2):
    if guess == number:
        print("you did it")
    elif not guess == number:
        print("that's incorrect")
        guess = int(input("what is your guess?"))
        

