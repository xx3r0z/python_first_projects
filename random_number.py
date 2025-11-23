import random

lower_number = int(input("Enter the lower bound: "))
upper_number = int(input("Enter the upper bound: "))

random_number = random.randint(lower_number, upper_number)
print(random_number)