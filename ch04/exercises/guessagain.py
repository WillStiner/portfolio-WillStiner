import random
num = random.randint(1, 100)
num_guesses = 0
guess = -1

while guess != num:
    guess = int(input("enter a guess: "))
    if guess == num:
        pass
    elif guess > num:
        print("too high")
    elif guess < num:
        print("too low")
    num_guesses += 1
print("correct! it took", num_guesses, "to get it")