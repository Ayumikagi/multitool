import math

while True:

    print('''What do you want to do?: 
    
1. Calculator
2. Text tools
          ''')

    tool = input('Pick a tool!: ')

    if tool in ('1', '2'):

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

                                if pick == '2':
                                    rounded = num1 // num2
                                    print(f'Rounded result: {num1} / {num2} = {rounded}')
                                    modulo = num1 % num2
                                    print(f'Leftover: {modulo}')
                                    break
                            else:
                                print(f'"{pick}" is not a valid input!')

                    while True:

                        next_calculation = input('Do another calculation? (Y/N): ')
                        
                        if next_calculation == 'Y':
                            break
                        
                        elif next_calculation == 'N':
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
                        
                        if next_calculation == 'Y':
                            break
                        
                        elif next_calculation == 'N':
                            print('Bye!')
                            input('Press any key to continue')
                            exit()

                        else:
                            print(f'"{next_calculation}" is not a valid input! Please use (Y)es or (N)o.')
                
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

                print('''What are we looking for?: 

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

                    if choice == '2':

                            confirm = input('Confirm presence of: ')

                            if confirm in text:
                                print(f'"{confirm}" can be found in the input.')

                            else:
                                print(f'"{confirm}" not present in the input.')

                    if choice == '3':

                        while True:

                            replace = input('Choose a letter or string to replace: ')
                        
                            (text.find(replace))

                            if (text.find(replace)) == -1:
                                print(f'Cannot find "{replace}"')

                            else:
                                replacement = input(f'Replace "{replace}" with: ')
                                print(text.replace(replace, replacement))
                                break

                    if choice == '4':

                        print(f' Length of your input is {(len(text))} character(s).')

                    if choice == '5':

                        print(text.upper())

                    if choice == '6':

                        print(text.lower())

                    while True:
                        redo = input('Choose another action? (Y/N): ')

                        if redo == 'Y':
                            break

                        elif redo == 'N':
                            print('Bye!')
                            input('Press any key to end.')
                            exit()

                        else:
                            print(f'"{redo}" is not a valid input! Please use (Y)es or (N)o.')

                else:
                    print(f'"{choice}" is not a valid input!')
        
    else:
        print(f'"{tool}" is not a valid input!')