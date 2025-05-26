'''
Build a simple CLI game where the user tries to guess a randomly
generated number within a limited number of attempts.
The program gives hints like “too high” or “too low.”
'''
import random

attempts = 3
n1 = 1
n2 = 10

def welcome_message():
    print('Welcome to Guessing Game!\n\n\n')

    print(f'You have to guess a number between {n1} and {n2}.\n')
    print(f'You only have {attempts} attempts to guess the number.\n\n')

    print(f'Good luck! Press ANY key to start the game...')
    input()

def guess_number():
    global attempts, n1, n2
    i = 0
    num = random.randint(n1, n2)
    while i < attempts:
        user_input = int(input("\nGuess the number: "))

        if user_input < num:
            print('Too low. Guess again...')
            attempts -= 1
        elif user_input > num:
            print('Too high. Guess again...')
            attempts -= 1
        else:
            print('\nCongratulations! You won.')
            break
    else:
        print('\n\nYou lose. Better luck next time.')
        print(f'The number is {num}\n')


if __name__=='__main__':
    welcome_message()
    guess_number()
