import random
low = int(input("pick a random number:"))
high = int(input("pick a larger number:"))
num_numbers = int(input("how many random numbers do you want?:"))

for num in range (num_numbers):
    random_number = random.randint(low, high)
    print(random_number)