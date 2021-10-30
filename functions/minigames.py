import random
from functions import descriptions
from functions import cargame_status
from functions import guessgame_status
from functions import universal

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
                number = random.randint(1, 10)
                break
            elif choice == '2':
                number = random.randint(1, 20)
                break
            elif choice == '3':
                diff = 'hard'
                number = random.randint(1, 30)
                break
            elif choice == '4' and extreme == True:
                diff = 'extreme'
                number = random.randint(1, 50)
                break
            elif choice == '5' and insane == True:
                diff = 'insane'
                number = random.randint(1, 100)
                break
            elif choice == '6' and gigachad == True:
                diff = 'gigachad'
                number = random.randint(1, 250)
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
    