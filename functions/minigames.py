from functions import descriptions
from functions import cargame_status
from functions import guessgame_status
from functions import universal
from functions import questions
from pathlib import Path
from random import randint
from textwrap import dedent


def guessgame(state):
    diff = ''
    extreme = ''
    insane = ''
    gigachad = ''

    if state == '0':
        extreme, insane, gigachad == guessgame_status.state_0()
        descriptions.guessgame_welcome_0()
    elif state == '1':
        extreme, insane, gigachad == guessgame_status.state_1()
        descriptions.guessgame_welcome_1()
    elif state == '2':
        extreme, insane, gigachad == guessgame_status.state_2()
        descriptions.guessgame_welcome_2()
    elif state == '3':
        extreme, insane, gigachad == guessgame_status.state_3()
        descriptions.guessgame_welcome_3()
    
    while True:
        while True:
            choice = input('Enter your choice: ').upper()
            if choice == '1':
                number = randint(1, 10)
                break
            elif choice == '2':
                number = randint(1, 20)
                break
            elif choice == '3':
                diff = 'hard'
                number = randint(1, 30)
                break
            elif choice == '4' and extreme == True:
                diff = 'extreme'
                number = randint(1, 50)
                break
            elif choice == '5' and insane == True:
                diff = 'insane'
                number = randint(1, 100)
                break
            elif choice == '6' and gigachad == True:
                diff = 'gigachad'
                number = randint(1, 250)
                break
            elif choice == 'R':
                number = 'back'
                break
            else:
                descriptions.choice_error(choice)
        if number == 'back' and extreme == True:
            state = '1'
            descriptions.minigames_welcome()
            return state
        elif number == 'back' and insane == True:
            state = '2'
            descriptions.minigames_welcome()
            return state
        elif number == 'back' and gigachad == True:
            state = '3'
            descriptions.minigames_welcome()
            return state
        elif number == 'back' and not extreme == True:
            state = '0'
            descriptions.minigames_welcome()
            return state
        else:
            lives = 3
            while lives > 0:
                while True:
                    guess = input('Guess the number: ')
                    try:
                        guess = int(guess)
                        break
                    except ValueError:
                        descriptions.choice_error(guess)
                if guess > number:
                    lives -= 1
                    print(f'Too high! Remaining lives: {lives}')
                elif guess < number:
                    lives -= 1
                    print(f'Too low! Remaining lives: {lives}')
                elif guess == number:
                    break
            if lives > 0:
                print(f'Good job! The right number was {number}')
                if diff == 'hard':
                    extreme = True
                    descriptions.guessgame_welcome_1()
                elif diff == 'extreme':
                    insane = True
                    descriptions.guessgame_welcome_2()
                elif diff == 'insane':
                    gigachad = True
                    descriptions.guessgame_welcome_3()
                elif diff == 'gigachad':
                    print('You did it! You are a true Guess the Number enjoyer!')
                    input('Press any key to continue.')
                    descriptions.guessgame_welcome_3()
                else:
                    descriptions.guessgame_welcome_0()
            elif lives == 0:
                print(f'Out of lives! The right number was {number}')
                if extreme == True and not insane == True:
                    descriptions.guessgame_welcome_1()
                elif insane == True and not gigachad == True:
                    descriptions.guessgame_welcome_2()
                elif gigachad == True:
                    descriptions.guessgame_welcome_3()
                else:
                    descriptions.guessgame_welcome_0()


def cargame():
    car_state = 'stop'
    descriptions.cargame_welcome() 
    while True:
        user_input = input('>').upper()
        if user_input == 'ACCEL':
            if car_state == 'stop':
                car_state = cargame_status.accel_0()
            elif car_state == 'slow':
                car_state = cargame_status.accel_1()
            elif car_state == 'average':
                car_state = cargame_status.accel_2()
            elif car_state == 'fast':
                car_state = cargame_status.accel_3()
            elif car_state == 'max':
                cargame_status.accel_4()
        elif user_input == 'STOP':
            if car_state == 'slow':
                car_state = cargame_status.stop_0()
            elif car_state == 'average':
                car_state = cargame_status.stop_1()
            elif car_state == 'fast':
                car_state = cargame_status.stop_2()
            elif car_state == 'max':
                car_state = cargame_status.stop_3()
            elif car_state == 'stop':
                cargame_status.stop_4()
            print('You are standing still.')
        elif user_input == 'R':
            descriptions.minigames_welcome()
            break
        elif user_input == 'QUIT':
            universal.quit()
        else:
            descriptions.choice_error(user_input)


def trivia_game():
    class Player:
        def __init__(self, name, rank, exp, nexp):
            self.name = name
            self.rank = rank
            self.exp = exp
            self.nexp = nexp
        
        def welcome(self):
            print(f'Welcome {self.rank} {self.name}!')
            
    try:
        data = Path('triviadata.txt').read_text()
        user = data.split(', ')
        name, rank, exp, nexp = user
        exp = int(exp)
    except FileNotFoundError:
        name = input('Enter your name: ')
        rank = 'Rookie'
        exp = 0
        nexp = '5'
        Path('triviadata.txt').write_text(f"{name}, {rank}, {exp}, {nexp}")
    player = Player(name, rank, exp, nexp)
    player.welcome()

    print('Trivia Master 1.0.0 Loaded.')
    while True:
        print('[1. New game] [2. Profile] [3. Quit]')
        choice = input("What's it gonna be?: ")
        if choice == '1':
            pool, right_answer, exclude = 5, 0, []
            print('Starting a new game...')
            while pool > 0:
                while True:
                    question = randint(1, 5)
                    if question in exclude:
                        pass
                    else:
                        break
                A, B, C = questions.q(question)
                while True:
                    choice = input('Enter your choice: ').upper()
                    if choice == 'A':
                        answer = A
                        break
                    elif choice == 'B':
                        answer = B
                        break
                    elif choice == 'C':
                        answer = C
                        break
                    else:
                        print(f'"{choice}" is not a valid input.')
                if answer == True:
                    print('Correct!')
                    right_answer += 1
                    pool -= 1
                elif answer == False:
                    print('Wrong')
                    pool -= 1
                    if A == True:
                        print('The right answer was A.')
                    elif B == True:
                        print('The right answer was B.')
                    elif C == True:
                        print('The right answer was C.')
                exclude.append(question)
                A = B = C = None
            print(dedent(f'''
            Good job {player.name}!
            You have answered correctly to {right_answer} question(s).
            '''))
            exp += right_answer
            if 10 > exp > 4 and rank == 'Rookie':
                print(f'Promoted from {rank} to Apprentice!')
                rank = 'Apprentice'
                nexp = '10' 
            elif 20 > exp > 9 and rank == 'Apprentice':
                print(f'Promoted from {rank} to Expert!')
                rank = 'Expert'
                nexp = '20'
            elif 35 > exp > 19 and rank == 'Expert':
                print(f'Promoted from {rank} to Master!')
                rank = 'Master'
                nexp = '35'
            elif 50 > exp > 34 and rank == 'Master':
                print(f'Promoted from {rank} to Legend!')
                rank = 'Legend'
                nexp = '50'
            elif exp > 49 and rank == 'Legend':
                print(f'Promoted from {rank} to Gigachad!')
                rank = 'Gigachad'
                nexp = 'MAX'
            elif right_answer < 5:
                print('Rank remains unchanged.')
            print(f'Next rank progress: {exp}/{nexp}')
            input('Press any key to continue.')
            Path('triviadata.txt').write_text(f"{name}, {rank}, {exp}, {nexp}")
        elif choice == '2':
            print(f'Name: {name} | Rank: {rank} | XP: {exp}/{nexp}')
            while True:
                choice = input('Would you like to change your name? [Y/N]: ').upper()
                if choice == 'Y':
                    name = input('Enter your new name: ')
                    player.name = name
                    print(f'"{name}" set as your name.')
                    Path('triviadata.txt').write_text(f"{name}, {rank}, {exp}, {nexp}")
                    break
                elif choice == 'N':
                    break
                else:
                    print(f'"{choice}" is not a valid input.')
        elif choice == '3':
            Path('triviadata.txt').write_text(f"{name}, {rank}, {exp}, {nexp}")
            descriptions.minigames_welcome()
            break
        else:
            print(f'"{choice} is an invalid input."')
    
