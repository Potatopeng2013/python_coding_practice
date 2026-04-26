#This is the number guessing game where you have to guess the computer generated number based on the difficulty.

import random

difficulty = input("Choose a difficulty 1 to 4. 4 is the hardest: ")

if difficulty == "1":
    guess = int(input("Enter a number between 1 and 10: "))
    number = random.randint(1, 10)
elif difficulty == "2":
    guess = int(input("Enter a number between 1 and 50: "))
    number = random.randint(1, 50)
elif difficulty == "3":
    guess = int(input("Enter a number between 1 and 100: "))
    number = random.randint(1, 100)
elif difficulty == "4":
    guess = int(input("Enter a number between 1 and 1000: "))
    number = random.randint(1, 1000)
else:
    print("Not a difficulty number.")   

while guess != number:
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")

    guess = int(input("Try again: "))

print("You got it")