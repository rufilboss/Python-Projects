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

def easy():
    print('You are to guess a number from 1 to 10, and you 6 guesses')
    guessingGame(6, 10)

def medium():
    print('You are to guess a number from 1 to 20, and you have 4 guesses')
    guessingGame(4, 20)

def hard():
    print('You are to guess a number from 1 to 50, and you have 3 guesses')
    guessingGame(3, 50)


def tryAgain():
    again = input('Do you want to play again? YES/NO')
    if again.upper == 'YES':
        welcome()
    elif again.upper == 'NO':
        print('Thanks for playing')
    else:
        print('Wrong input!')
        tryAgain()

def welcome():
    print('Welcome to the guessing game:')
    difficulty = input('Choose your level; Easy, Medium or Hard.')
    if difficulty.upper == 'EASY':
        easy()
        tryAgain()
    elif difficulty.upper == 'MEDIUM':
        medium()
        tryAgain()
    elif difficulty.upper == 'HARD':
        hard()
        tryAgain()
    else:
        print('This is wrong input')
        welcome()