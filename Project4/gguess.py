import random

def guessingGame(guessLimit, number):
    randomNumber = random.randint(1, number)

    try:
        while guessLimit > 0:
            guess = int(input("Enter your input..."))
            

    except ValueError:
        print("Only number is allowed")