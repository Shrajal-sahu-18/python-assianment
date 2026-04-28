import random
number = random.randint(1,100)
guess = None

while guess != number:
    guess = int(input("guess the number:"))
    if guess > number:
        print("to high ")
    elif guess < number:
        print("to low")
    else:
        print("you guess correct number")
    