import textwrap

print('Welcome to scuffed text racer 9000, type "help" for a list of commands.')
car_state = 'stop'
user_input = ""

while True:
    user_input = input('>').upper()
    if user_input == 'HELP':
        print(textwrap.dedent('''
        "Start" to start the car
        "Stop" to stop the car
        "Quit" to exit the "game:
              '''))
    elif user_input == 'START':
        if car_state == 'stop':
            car_state = 'slow'
            print('Starting the car...')
            print('Going slowly!')
        elif car_state == 'slow':
            car_state = 'average'
            print('Speed ramping up!')
        elif car_state == 'average':
            car_state = 'fast'
            print('Full steam ahead!')
        elif car_state == 'fast':
            car_state = 'max'
            print('What the hell are you doing?!')
        elif car_state == 'max':
            print("Can't start, you are already pushing it to the limit!")
    elif user_input == 'STOP':
        if car_state == 'slow':
            car_state = 'stop'
            print('Stopping the car...')
        elif car_state == 'average':
            car_state = 'stop'
            print('Smooth braking!')
        elif car_state == 'fast':
            car_state = 'stop'
            print('Wild stop! Your tires are on fire!')
        elif car_state == 'max':
            car_state = 'stop'
            print('Your brakes can be heard on mars...')
        elif car_state == 'stop':
            print("Can't stop, you are not moving!")
        print('You are standing still.')
    elif user_input == 'QUIT':
        break
    else:
        print(f'"{user_input}" is not a valid input!')
input('Bye! Press any key to continue.')