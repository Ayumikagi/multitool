import math
import importlib

while True:
    print('Welcome to multitool v1.2.0, press assigned number to execute a function or (R) to return to the previous menu')
    print('''What do you want to do?: 
    
1. Calculator
2. Text tools
3. Converter
4. Minigames
          ''')

    tool = input('Pick a tool!: ').upper()

    if tool in ('1', '2', '3', '4'):

        if tool == '1':

            while True:

                print('''Select operation: 

1. Add/Subtract/Multiply/Divide
2. Round/Square Root/Exponentation/Absolute/Floor Ceiling
                      ''')

                choice = input('Enter your choice: ').upper()

                if choice == '1':
                        
                    try:
                        importlib.reload(math_basic)
                    except:
                        from content import math_basic

                elif choice == '2':

                    try:
                        importlib.reload(math_adv)
                    except:
                        from content import math_adv
                
                elif choice == 'R':
                    break
                
                else:
                    print(f'"{choice}" is not a valid input!')

        if tool == '2':

            while True:

                print('''What are we looking for? (Return not available during executioned commands): 

1. Find (Position)
2. Find (Confirm)
3. Replace
4. Count
5. ALL UPPERCASE/lowercase
                    ''')

                choice = input('Enter your choice: ').upper()

                if choice in ('1', '2', '3', '4', '5'):

                    if choice == '1':
                        
                        try:
                            importlib.lib(findpos)
                        except:
                            from content import findpos

                    elif choice == '2':

                        try:
                            importlib.reload(findconf)
                        except:
                            from content import findconf

                    elif choice == '3':

                        try:
                            importlib.reload(replace)
                        except:
                            from content import replace

                    elif choice == '4':

                        try:
                            importlib.reload(charcount)
                        except:
                            from content import charcount

                    elif choice == '5':

                        try:
                            importlib.reload(upperlower)
                        except:
                            from content import upperlower

                    while True:
                        redo = input('Return to text tools menu? (Y/N): ').upper()

                        if redo == 'Y':
                            break

                        elif redo == 'N':
                            input('Bye! Press any key to end.')
                            exit()

                        else:
                            print(f'"{redo}" is not a valid input! Please use (Y)es or (N)o.')

                elif choice == 'R':
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

                choice = input('Enter your choice: ').upper()

                if choice in ('1', '2', '3'):

                    if choice == '1':
                        
                        try:
                            importlib.reload(weightconv)
                        except: 
                            from content import weightconv

                    if choice == '2':
                        
                        try:
                            importlib.reload(lengthconv)
                        except:
                            from content import lengthconv

                    if choice == '3':

                        try:
                            importlib.reload(tempconv)
                        except:
                            from content import tempconv

                    while True:

                        redo = input('Return to conversion menu? (Y/N): ').upper()
                        
                        if redo == 'Y':
                            break
                        
                        elif redo == 'N':
                            input('Bye! Press any key to end')
                            exit()
                                    
                        else:
                            print(f'"{redo}" is not a valid input! Please use (Y)es or (N)o.')

                elif choice == 'R':
                    break

                else:
                    print(f'"{choice}" is not a valid input!')
        
        if tool == '4':

            while True:

                print('''What would you like to play?:
            
1. Guess the number
2. Car game
                      ''')

                choice = input('Enter your choice: ').upper()

                if choice in ('1', '2'):

                    if choice == '1':
                        try:
                            importlib.reload(guessgame)
                        except:
                            from content import guessgame

                    if choice == '2':
                        try:
                            importlib.reload(car_game)
                        except:
                            from content import car_game

                elif choice == 'R':
                    break

        else:
            print(f'"{choice}" is not a valid input!')

    elif tool == 'R':
        print('Cannot return any further!')

    else:
        print(f'"{tool}" is not a valid input!')
