import random

def guessingGame(guessLimit, number):
    randomNumber = random.randint(1, number)

    try:
        while guessLimit > 0:
            guess = int(input("What is your guess?"))
            guessLimit -= 1

        if randomNumber == guess:
            print('Congrats, you got it right!')
            # break
        elif guess > number:
            print('Your guess is out of range')
            print(f'You have {guessLimit} guess(es) left!')
        else:
            print('Sorry, you are wrong!')
            print(f'You have {guessLimit} guess(es) left!')

        print('Game Over!')
        print(f'The random number was {randomNumber}')

    except ValueError:
        print("Only number is allowed")