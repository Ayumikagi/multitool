import math

while True:

    while True:

        num = input('Enter desired number: ')

        try:
            num = float(num)
            break

        except ValueError:
            print(f'"{num}" is not a valid input!')
    
    while True:

        print('''What do we do?:
        
1. Round         4. Absolute value
2. Square root   5. Floor and Ceiling
3. Exponential
        ''')

        choice = input('Enter your choice: ')

        if choice == '1':

            print(f' Rounded value is {round(float(num))}.')

        if choice == '2':

            print(f'Square root of {num} is {math.sqrt(float(num))}')

        if choice == '3':

            while True:

                exponent = input('Enter exponent: ')

                try:
                    exponent = float(exponent)
                    print(f'{num} to the power of {exponent} equals {math.pow(float(num), float(exponent))}')
                    break

                except ValueError:
                    print(f'"{exponent}" is not a valid input!')

        if choice == '4':

            print(f'Absolute value of {num} is {abs(num)}')

        if choice == '5':

            print(f'Number {num} has a {math.floor(num)} floor and a {math.ceil(num)} ceiling.')

        while True:

            redo = input('Do another calculation? (Y/N/R): ')
            
            if redo.upper() == 'Y':
                break
            
            elif redo.upper() == 'N':
                input('Bye! Press any key to continue')
                exit()

            elif redo.upper() == 'R':
                break

            else:
                print(f'"{redo}" is not a valid input! Please use (Y)es, (N)o, (R)eturn.')
        
        if redo.upper() in ('Y', 'R'):
            break
    
    if redo.upper() == 'R':
        break