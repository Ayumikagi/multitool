import math
import random

while True:
    print('Welcome to multitool v1.2.0, press assigned number to execute a function or (R) to return to the previous menu')
    print('''What do you want to do?: 
    
1. Calculator
2. Text tools
3. Converter
4. Minigames
          ''')

    tool = input('Pick a tool!: ')

    if tool in ('1', '2', '3', '4'):

        if tool == '1':

            while True:

                print('''Select operation: 

1. Add          6. Square root
2. Subtract     7. Exponentation
3. Multiply     8. Absolute
4. Divide       9. Floor/Ceiling
5. Round
                      ''')

                choice = input('Enter your choice: ')

                if choice in ('1' , '2', '3', '4'):
                        
                    while True:

                        num1 = input('Enter first number: ')

                        try:
                            num1 = float(num1)
                            break
                            
                        except ValueError:
                            print('Ay yo, stop, resetting your value 1...')

                    while True:

                        num2 = input('Enter second number: ')

                        try:
                            num2 = float(num2)
                            break

                        except ValueError:
                            print('Ay yo, stop, resetting your value 2...')

                    if choice == '1':
                        add = num1 + num2
                        print(f'{num1} + {num2} = {add}')

                    elif choice == '2':
                        sub = num1 - num2
                        print(f'{num1} - {num2} = {sub}')

                    elif choice == '3':
                        multi = num1 * num2
                        print(f'{num1} * {num2} = {multi}')

                    elif choice == '4':

                        while True:

                            print('''Would you like to see:

1. Full result
2. Rounded result with modulo
                                ''')

                            pick = input('Enter your choice: ')

                            if pick in ('1', '2'):

                                if pick == '1':
                                    print(f'{num1} / {num2} = {divide(num1, num2)}')
                                    break

                                elif pick == '2':
                                    rounded = num1 // num2
                                    print(f'Rounded result: {num1} / {num2} = {rounded}')
                                    modulo = num1 % num2
                                    print(f'Leftover: {modulo}')
                                    break

                                elif pick.upper() == 'R':
                                    break

                            else:
                                print(f'"{pick}" is not a valid input!')

                    while True:

                        next_calculation = input('Do another calculation? (Y/N): ')
                        
                        if next_calculation.upper() == 'Y':
                            break
                        
                        elif next_calculation.upper() == 'N':
                            print('Bye!')
                            input('Press any key to continue')
                            exit()

                        else:
                            print(f'"{next_calculation}" is not a valid input! Please use (Y)es or (N)o.')

                elif choice in ('5', '6', '7', '8', '9'):

                    while True:

                        num3 = input('Enter desired number: ')

                        try:
                            num3 = float(num3)
                            break

                        except ValueError:
                            print(f'"{num3}" is not a valid input!')

                    if choice == '5':

                        print(f' Rounded value is {round(float(num3))}.')

                    if choice == '6':

                        print(f'Square root of {num3} is {math.sqrt(float(num3))}')

                    if choice == '7':

                        while True:

                            exponent = input('Enter exponent: ')

                            try:
                                exponent = float(exponent)
                                print(f'{num3} to the power of {exponent} equals {math.pow(float(num3), float(exponent))}')
                                break

                            except ValueError:
                                print(f'"{exponent}" is not a valid input!')

                    if choice == '8':

                        print(f'Absolute value of {num3} is {abs(num3)}')

                    if choice == '9':

                        print(f'Number {num3} has a {math.floor(num3)} floor and a {math.ceil(num3)} ceiling.')

                    while True:

                        next_calculation = input('Do another calculation? (Y/N): ')
                        
                        if next_calculation.upper() == 'Y':
                            break
                        
                        elif next_calculation.upper() == 'N':
                            print('Bye!')
                            input('Press any key to end')
                            exit()

                        else:
                            print(f'"{next_calculation}" is not a valid input! Please use (Y)es or (N)o.')
                
                elif choice.upper() == 'R':
                    break
                
                else:
                    print(f'"{choice}" is not a valid input!')

        if tool == '2':

            while True:

                text = input('Enter your text: ')

                if len(text) == 0:
                    print('Put in something!')

                else:
                    break

            while True:

                print('''What are we looking for? (Return not available during executioned commands): 

1. Find (Position)
2. Find (Confirm)
3. Replace
4. Count
5. ALL UPPERCASE
6. all lowercase
                    ''')

                choice = input('Enter your choice: ')

                if choice in ('1', '2', '3', '4', '5', '6'):

                    if choice == '1':
                        
                        while True:

                            search = input('Enter key value: ')

                            (text.find(search))

                            if (text.find(search)) == -1:
                                print(f'Cannot find "{search}"')

                            else:
                                print(f'"{search}" found at position {(text.find(search))}.')
                                break

                    elif choice == '2':

                            confirm = input('Confirm presence of: ')

                            if confirm in text:
                                print(f'"{confirm}" can be found in the input.')

                            else:
                                print(f'"{confirm}" not present in the input.')

                    elif choice == '3':

                        while True:

                            replace = input('Choose a letter or string to replace: ')
                        
                            (text.find(replace))

                            if (text.find(replace)) == -1:
                                print(f'Cannot find "{replace}"')

                            else:
                                replacement = input(f'Replace "{replace}" with: ')
                                print(text.replace(replace, replacement))
                                break

                    elif choice == '4':

                        print(f' Length of your input is {(len(text))} character(s).')

                    elif choice == '5':

                        print(text.upper())

                    elif choice == '6':

                        print(text.lower())

                    while True:
                        redo = input('Return to text tools menu? (Y/N): ')

                        if redo.upper() == 'Y':
                            break

                        elif redo.upper() == 'N':
                            print('Bye!')
                            input('Press any key to end.')
                            exit()

                        else:
                            print(f'"{redo}" is not a valid input! Please use (Y)es or (N)o.')

                elif choice.upper() == 'R':
                    break

                else:
                    print(f'"{choice}" is not a valid input!')
        
        if tool == '3':

            while True:

                print('''What do you want to convert: 
                
1. Weight
2. Length
3. Temperature
                ''')

                choice = input('Enter your choice: ')

                if choice in ('1', '2', '3'):

                    while True:

                        num4 = input('Enter value: ')

                        try:
                            num4 = float(num4)
                            break

                        except ValueError:
                            print(f'"{num4}" is not a valid input!')

                    if choice == '1':

                        while True:

                            weight = input('(L)bs or (K)g?: ')

                            if weight.upper() == 'L':
                                print(f'You are {num4}Lbs, that equals {num4*0.45}Kg.')
                                break

                            elif weight.upper() == 'K':
                                print(f'You are {num4}Kg, that equals {num4/0.45}Lbs.')
                                break

                            elif weight.upper() == 'R':
                                break

                            else:
                                print(f'"{weight}" is not a valid input!')

                    if choice == '2':

                        while True:

                            length = input('What unit is that? (Choose from metric, fuck imperial): ')

                            if length.upper() == 'MM':
                                print(f'''{num4}mm is equal to:
                                
Metric: {num4/10}cm / {num4/100}dm / {num4/1000}m / {num4/1000000}km
Imperial: {num4/25.4}in / {num4/304.8}ft / {num4/914.4}yd / {num4/1609343.97}mi
                                ''')
                                break

                            elif length.upper() == 'CM':
                                print(f'''{num4}cm is equal to:
                                
Metric: {num4/0.1}mm / {num4/10}dm / {num4/100}m / {num4/100000}km
Imperial: {num4/2.54}in / {num4/30.48}ft / {num4/91.44}yd / {num4/160934.39}mi
                                ''')
                                break

                            elif length.upper() == 'DM':
                                print(f'''{num4}dm is equal to:
                                
Metric: {num4/0.01}mm / {num4/0.1}cm / {num4/10}m / {num4/10000}km
Imperial: {num4/0.254}in / {num4/3.048}ft / {num4/9.144}yd / {num4/16093.43}mi
                                ''')
                                break

                            elif length.upper() == 'M':
                                print(f'''{num4}m is equal to:
                                
Metric: {num4/0.001}mm / {num4/0.01}cm / {num4/0.1}dm / {num4/1000}km
Imperial: {num4/0.0254}in / {num4/0.3048}ft / {num4/0.9144}yd / {num4/1609.34}mi
                                ''')
                                break

                            elif length.upper() == 'KM':
                                print(f'''{num4}km is equal to:
                                
Metric: {num4/0.000001}mm / {num4/0.00001}cm / {num4/0.0001}dm / {num4/1000}m
Imperial: {num4/0.0000254}in / {num4/0.0003048}ft / {num4/0.0009144}yd / {num4/1.6}mi
                                ''')
                                break

                            elif length.upper() == 'R':
                                break

                            else:
                                print(f'"{length}" is not a valid input!')

                    if choice == '3':

                        while True:

                            temp = input('What scale? (Celsius/Fahrenheit/Kelvin): ')

                            if temp.upper() in ('CELSIUS', 'C'):
                                print(f'{num4}°C equals to {(num4*1.8)+32}F or {num4+273.15}K')
                                break

                            elif temp.upper() in ('FAHRENHEIT', 'F'):
                                print(f'{num4}F equals to {(num4-32)*1.8}°C or {(num4-32)*1.8+273.15}K')
                                break

                            elif temp.upper() in ('KELVIN', 'K'):
                                print(f'{num4}K equals to {num4-273.15}°C or {(num4-273.15)*1.8+32}F')
                                break

                            elif temp.upper() == 'R':
                                break

                            else:
                                print(f'"{temp}" is not a valid input!')

                    while True:

                        redo = input('Return to conversion menu? (Y/N): ')
                        
                        if redo.upper() == 'Y':
                            break
                        
                        elif redo.upper() == 'N':
                            print('Bye!')
                            input('Press any key to end')
                            exit()
         
                elif choice == 'R':
                    break
                
                else:
                    print(f'"{choice}" is not a valid input!')
        
        if tool == '4':
            
            while True:
                print('''What would you like to play?:
            
1. Guess the number
                  ''')

                pick = input('Enter your choice: ')
            
                if pick == '1':

                    target = random.randint(1, 10)
                    lives = 3
                    while True:

                        while lives > 0:

                            while True:
                                guess = input('Guess the numba: ')

                                try:
                                    guess = float(guess)
                                    break
                                except ValueError:
                                    print(f'Cannot read "{guess}", please enter a number!')
                            
                            if guess > target:
                                print('Too high!')
                                lives -= 1
                            elif guess < target:
                                print('Too low!')
                                lives -= 1
                            elif guess == target:
                                break
                            elif guess.upper() == 'R':
                                break
                        
                        if lives > 0:
                            print(f'Good job! The right number was {target}.')
                            
                            while True:
                        
                                choice = input('Try again? (Y/N): ')
                                if choice.upper() == 'Y':
                                    target = random.randint(1, 10)
                                    lives = 3
                                    break
                                elif choice.upper() == 'N':
                                    input('Bye! Press any key to continue.')
                                    exit()
                                elif choice.upper() == 'R':
                                    break
                                else:
                                    print(f'"{choice}" is not a valid input!')

                        if lives == 0:
                            print(f'Out of lives! The right number was {target}')

                            while True:
                                
                                choice = input('Try again? (Y/N): ')
                                if choice.upper() == 'Y':
                                    target = random.randint(1, 10)
                                    lives = 3
                                    break
                                elif choice.upper() == 'N':
                                    input('Bye! Press any key to continue.')
                                    exit()
                                elif choice.upper() == 'R':
                                    break
                                else:
                                    print(f'"{choice}" is not a valid input!')
                            if choice.upper() == 'R':
                                break
                
                elif pick.upper() == 'R':
                    break
                
                else:
                    print(f'"{pick}" is not a valid input!')

    elif tool.upper() == 'R':
        print('Cannot return any further!')

    else:
        print(f'"{tool}" is not a valid input!')