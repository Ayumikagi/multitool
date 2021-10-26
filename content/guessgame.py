import random

while True:

    target = random.randint(1, 10)
    lives = 3
    while lives > 0:

        while True:
            guess = input('Guess the numba: ')

            try:
                guess = float(guess)
                break
            except ValueError:
                print(f'Cannot read "{guess}", please enter a number!')
        
        if guess > target:
            lives -= 1
            print(f'Too high! Remaining lives: {lives}')
        elif guess < target:
            lives -= 1
            print(f'Too low! Remaining lives: {lives}')
        elif guess == target:
            break
        elif guess.upper() == 'R':
            break
    
    if lives > 0:
        print(f'Good job! The right number was {target}.')
        break

    elif lives == 0:
        print(f'Out of lives! The right number was {target}')
        break

while True:
    redo = input('Try again? (Y/N): ')

    if redo.upper() == 'Y':
        target = random.randint(1, 10)
        lives = 3
        break

    elif redo.upper() == 'N':
        input('Bye! Press any key to continue.')
        exit()

    else:
        print(f'"{redo}" is not a valid input! Please use (Y)es or (N)o.')