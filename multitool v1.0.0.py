import math

while True:

    print('''What do you want to do?: 
    
    1. Calculator
    2. Text tools
          ''')

    while True:
        tool = input('Pick a tool!: ')
        print('\n')

        if tool in ('1', '2'):

            if tool == '1':

                def add(x, y):
                    return x + y

                def subtract(x, y):
                    return x - y

                def multiply(x, y):
                    return x * y

                def divide(x, y):
                    return x / y

                print('''Select operation: 

    1. Add          6. Square root
    2. Subtract     7. Exponentation
    3. Multiply
    4. Divide 
    5. Round
                      ''')

                while True:
                    choice = input('Enter your choice: ')

                    if choice in ('1' , '2', '3', '4'):
                        
                        while True:

                            num1 = None
                            num2 = None

                            try:
                                num1 = float(input('Enter first number: '))
                            except ValueError:
                                print('Ay yo, stop, resetting your value 1...\n')
                                pass
                                    
                            if num1 != None:
                                break

                        while True:
                            try:
                                num2 = float(input('Enter second number: '))
                            except ValueError:
                                print('Ay yo, stop, resetting your value 2...\n')
                                pass

                            if num2 != None:
                                break

                            if num1 != None and num2 != None:
                                break

                        if choice == '1':
                            print(num1, '+', num2, '=', add(num1, num2))
                            print('\n')

                        elif choice == '2':
                            print(num1, '-', num2, '=', subtract(num1, num2))
                            print('\n')

                        elif choice == '3':
                            print(num1, '*', num2, '=', multiply(num1, num2))
                            print('\n')

                        elif choice == '4':
                            
                            print('''Would you like to see:

    1. Full result
    2. Rounded result with modulo
                                  ''')

                            while True:

                                pick = input('Enter your choice: ')
                                print('\n')

                                if pick in ('1', '2'):

                                    if pick == '1':
                                        print(num1, '/', num2, '=', divide(num1, num2))
                                        print('\n')
                                        break

                                    if pick == '2':
                                        rounded = num1 // num2
                                        print(f'Rounded result: {num1} / {num2} = {rounded}')
                                        modulo = num1 % num2
                                        print(f'Leftover: {modulo}\n')
                                        break
                                else:
                                    print('Wrong input!\n')

                        while True:
                            next_calculation = input('Do another calculation? (Y/N): ')
                            print('\n')
                            
                            if next_calculation == 'Y':
                                del num1
                                del num2
                                break
                            
                            elif next_calculation == 'N':
                                print('Bye!')
                                print('Press any key to continue')
                                exit()

                            else:
                                print(f'"{next_calculation}" is not an option! Please use (Y)es or (N)o.\n')

                    elif choice in ('5', '6', '7'):

                        if choice == '5':
                        
                            while True:
                                
                                round_val = (input('Enter your value: '))
                                print('\n')

                                if round_val.isnumeric() == True:
                                    float(round_val)
                                    print(f' Rounded value is {(round(round_val))}.\n')
                                    break

                                elif round_val.isnumeric() == False and round_val.find(',') == True:
                                    print(f'"{round_val}" is not a valid format!')
                                    print('Please use dot instead of comma for proper formatting.\n')

                                else:
                                    print(f'"{round_val}" is not a number!\n')

                        if choice == '6':

                            while True:

                                sqrt_val = input('Enter your value: ')
                                print('\n')

                                if sqrt_val.isnumeric():
                                    print(f'Square root of {sqrt_val} is {math.sqrt(float(sqrt_val))}\n')
                                    break

                                else:
                                    print(f'"{sqrt_val}" is not a valid input!\n')

                        if choice == '7':

                            while True:

                                exp_val = input('Enter your value: ')
                                print('\n')
                                
                                if exp_val.isnumeric():
                                    break

                                else:
                                    print(f'"{exp_val}" is not a valid input!\n')

                            while True:

                                exponent = input('Enter exponent: ')
                                print('\n')
    
                                if exponent.isnumeric():
                                    print(f'{exp_val} to the power of {exponent} equals {math.pow(float(exp_val), float(exponent))}\n')
                                    break

                                else:
                                    print(f'"{exponent}" is not a valid input!\n')

                        while True:
                            next_calculation = input('Do another calculation? (Y/N): ')
                            print('\n')
                            
                            if next_calculation == 'Y':
                                del num1
                                del num2
                                break
                            
                            elif next_calculation == 'N':
                                print('Bye!')
                                input('Press any key to continue')
                                exit()

                            else:
                                print(f'"{next_calculation}" is not an option! Please use (Y)es or (N)o.\n')
                    
                    else:
                        print('Invalid input!\n')

            if tool == '2':

                while True:

                    text = input('Enter your text: ')
                    print('\n')

                    if len(text) == 0:
                        print('Put in something!\n')

                    else:
                        break

                print('''What are we looking for?: 

    1. Find (Position)
    2. Find (Confirm)
    3. Replace
    4. Count
    5. ALL UPPERCASE
    6. all lowercase
                      ''')

                while True:
                    choice = input('Enter your choice: ')
                    print('\n')

                    if choice in ('1', '2', '3', '4', '5', '6'):

                        if choice == '1':

                            search = input('Enter key value: ')

                            (text.find(search))

                            if (text.find(search)) == -1:
                                print(f'Cannot find "{search}"')

                            else:
                                print(f'"{search}" found at position {(text.find(search))}.')

                        if choice == '2':
                            confirm = input('Confirm presence of: ')

                            if confirm in text:
                                print(f'"{confirm}" can be found in the input.')

                            else:
                                print(f'"{confirm}" not present in the input.')

                        if choice == '3':

                            replace = input('Choose a letter or string to replace: ')
                            
                            (text.find(replace))

                            if (text.find(replace)) == -1:
                                print(f'Cannot find "{replace}"')

                            else:
                                replacement = input(f'Replace "{replace}" with: ')
                                print(text.replace(replace, replacement))

                        if choice == '4':

                            print(f' Length of your input is {(len(text))} character(s).')

                        if choice == '5':

                            print(text.upper())

                        if choice == '6':

                            print(text.lower())

                        while True:
                            redo = input('Choose another action? (Y/N): ')
                            print('\n')

                            if redo == 'Y':
                                break

                            elif redo == 'N':
                                print('Bye!')
                                input('Press any key to end.')
                                exit()

                            else:
                                print(f'"{redo}" is not an option! Please use (Y)es or (N)o.\n')

                    else:
                        print(f'"{choice}" is not an option!\n')
            
        else:
            print(f'"{tool}" is not an option!\n')
