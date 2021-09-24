#! python3

import random

username = input('Hello, what is your name?   ')
print('Well, ' + username + ', I am thinking of a number between 1 and 24. Can you guess it?')
secretNumber = random.randint(1,24)


i=0
while i < 6:
    try:
        guess = int(input('Take a guess    '))

        if guess == secretNumber:
            print('Congratulations! That\'s what I was thinking!')
            print('This only took ' + str(i) + ' tries!')
            break
        elif guess != secretNumber:
            print('Sorry, that\'s incorrect :(')
            if guess > secretNumber:
                print('You guessed too high')
            else:
                 print('You guessed too low')
            i += 1

    except ValueError:
        print('Please enter your guess with a numerical character')

if i < 6:
    print('The game is done, do something else with your life.')
else:
    print('You did not guess my number quickly enough. You are a dodo bird')
