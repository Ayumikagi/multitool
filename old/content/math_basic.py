import math

while True:

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

    while True:

        print('''What do we do?: 
        
        1. Add        3. Multiply
        2. Subtract   4. Divide
        ''')

        choice = input('Enter your choice: ').upper()

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

                pick = input('Enter your choice: ').upper()

                if pick in ('1', '2'):

                    if pick == '1':
                        print(f'{num1} / {num2} = {num1/num2}')
                        break

                    elif pick == '2':
                        rounded = num1 // num2
                        print(f'Rounded result: {num1} / {num2} = {rounded}')
                        modulo = num1 % num2
                        print(f'Leftover: {modulo}')
                        break

                    elif pick == 'R':
                        break

                else:
                    print(f'"{pick}" is not a valid input!')

        elif choice == 'R':
            break

        while True:

            redo = input('Do another calculation? (Y/N/R): ').upper()
            
            if redo == 'Y':
                break
            
            elif redo == 'N':
                input('Bye! Press any key to continue')
                exit()

            elif redo == 'R':
                break

            else:
                print(f'"{redo}" is not a valid input! Please use (Y)es, (N)o, (R)eturn.')
        
        if redo in ('Y', 'R'):
            break
    
    if redo == 'R':
        break