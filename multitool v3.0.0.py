from functions import descriptions
from functions import calculator
from functions import textools
from functions import universal
from functions import converter
from functions import minigames

state = ''
user_name = input('Enter your name: ')
descriptions.welcome(user_name)

while True:
    choice = input('Enter your choice: ').upper()
    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            descriptions.calc_welcome()
            while True:
                choice = input('Enter your choice: ').upper()
                if choice in ('1', '2', '3', '4'):
                    while True:
                        num1 = input('Enter first value: ')
                        try:
                            num1 = float(num1)
                            break
                        except ValueError:
                            descriptions.choice_error(num1)
                    while True:
                        num2 = input('Enter second value: ')
                        try:
                            num2 = float(num2)
                            break
                        except ValueError:
                            descriptions.choice_error(num2)
                    if choice == '1':
                        result = calculator.add(num1, num2)
                        print(f'The result is of {num1} + {num2} is {result}')
                    elif choice == '2':
                        result = calculator.subtract(num1, num2)
                        print(f'The result is of {num1} - {num2} is {result}')
                    elif choice == '3':
                        result = calculator.multiply(num1, num2)
                        print(f'The result is of {num1} * {num2} is {result}')
                    elif choice == '4':
                        result, rounded, modulo = calculator.divide(num1, num2)
                        print(f'The result is of {num1} / {num2} is {result}')
                        print(f'Rounded result equals {rounded} and modulo is {modulo}')
                    descriptions.f_end()
                    back = calculator.math_f_end()
                    if back == True:
                        pass
                        
                elif choice in ('5', '6', '7', '8', '9'):
                    while True:
                        num = input('Enter desired value: ')
                        try:
                            num = float(num)
                            break
                        except ValueError:
                            descriptions.choice_error(num)
                    if choice == '5':
                        result = calculator.round(num)
                        print(f'Number {num} rounded equals {result}')
                    elif choice == '6':
                        result = calculator.sqrt(num)
                        print(f'Square root of {num} equals {result}')
                    elif choice == '7':
                        result, exp = calculator.exponent(num)
                        print(f'{num} to the power of {exp} equals {result}')
                    elif choice == '8':
                        result = calculator.abs(num)
                        print(f'Absolute value of {num} is {result}')
                    elif choice == '9':
                        result1, result2 = calculator.floor_ceil(num)
                        print(f'Number {num} has a floor of {result1} and a ceiling of {result2}')
                    descriptions.f_end()
                    back = calculator.math_f_end()
                    if back == True:
                        pass
                elif choice == 'R':
                    descriptions.re_welcome()
                    break
                else:
                    descriptions.choice_error(choice)
        elif choice == '2':
            while True:
                text = input('Enter text to work with: ')
                if len(text) == 0:
                    print('Cannot process empty input!')
                else:
                    break
            descriptions.textools_welcome()
            while True:
                choice = input('Enter your choice: ').upper()      
                if choice == '1':
                    while True:
                        result, find = textools.find_pos(text)
                        if result == 'fail':
                            print(f'"{find}" not found in the text.')
                        else:
                            print(f'"{find}" found at position [{result}]')
                        descriptions.textools_find_redo()
                        back = textools.f_end()
                        if back == True:
                            break
                        elif back == False:
                            pass
                elif choice == '2':
                    while True:
                        result = textools.replace(text)
                        print(result)
                        descriptions.textools_replace_redo()
                        back = textools.f_end()
                        if back == True:
                            break
                        elif back == False:
                            pass
                elif choice == '3':
                    result = len(text)
                    print(f'Your text has a total of {result} characters.')
                    descriptions.textools_count_end()
                    back = textools.count_end()
                    if back == True:
                        pass
                elif choice == '4':
                    descriptions.upperlower()
                    while True:
                        choice = input('Enter your choice: ').upper()
                        result = textools.upperlower(choice, text)
                        if result in (text.upper(), text.lower()):
                            text = result
                            print(text)
                            break
                        elif result == 'fail':
                            descriptions.choice_error(choice)
                        elif result == 'back':
                            descriptions.textools_welcome()
                            break
                    if result == text.upper():
                        descriptions.upper_end()
                        result = textools.upper_end(text)
                        if result == text.lower():
                            print(result)
                            descriptions.textools_welcome()
                        elif result == 'back':
                            descriptions.textools_welcome()
                            pass
                    elif result == text.lower():
                        descriptions.lower_end()
                        result = textools.lower_end(text)
                        if result == text.upper():
                            print(result)
                            descriptions.textools_welcome()
                        elif result == 'back':
                            descriptions.textools_welcome()
                            pass
                elif choice == 'R':
                    descriptions.re_welcome()
                    break
                else:
                    descriptions.choice_error(choice)
        elif choice == '3':
            descriptions.converter_welcome()
            while True:
                choice = input('Enter your choice: ').upper()
                if choice == '1':
                    while True:
                        value = input('How much?: ')
                        try:
                            value = int(value)
                            break                        
                        except ValueError:
                            descriptions.choice_error(value)
                    result, units = converter.weight_conv(value)
                    if units == 'kg':
                        print(f'Your weight in pounds is {int(result)}lbs.')
                    elif units == 'lbs':
                        print(f'Your weight in kilograms is {int(result)}kg.')
                    elif result == 'back':
                        descriptions.re_welcome()
                        break
                    descriptions.conv_end()
                    result = converter.conv_end()
                    if result == 'redo':
                        descriptions.converter_welcome()
                        pass
                    elif result == 'back':
                        descriptions.re_welcome()
                        break
                elif choice == '2':
                    while True:
                        value = input('Enter length: ')
                        try:
                            value = float(value)
                            break
                        except ValueError:
                            descriptions.choice_error(value)
                    result = converter.length_units(value)
                    if result  == 'back':
                        descriptions.re_welcome()
                        break
                    descriptions.conv_end()
                    result = converter.conv_end()
                    if result == 'redo':
                        descriptions.converter_welcome()
                        pass
                    elif result == 'back':
                        descriptions.re_welcome()
                        break
                elif choice == '3':
                    while True:
                        value = input('Enter temperature: ')
                        try:
                            value = float(value)
                            break
                        except ValueError:
                            descriptions.choice_error(value)
                    celsius, fahrenheit, kelvin, result = converter.temp_conv(value)
                    if celsius == True:
                        print(f'{value}°C equals to {fahrenheit}F or {kelvin}K')
                    elif fahrenheit == True:
                        print(f'{value}F equals to {celsius}°C or {kelvin}K')
                    elif kelvin == True:
                        print(f'{value}K equals to {celsius}°C or {fahrenheit}F')
                    elif result == 'back':
                        descriptions.re_welcome()
                        break
                    descriptions.conv_end()
                    result = converter.conv_end()
                    if result == 'redo':
                        descriptions.converter_welcome()
                        pass
                    elif result == 'back':
                        descriptions.re_welcome()
                        break
                elif choice == 'R':
                    descriptions.re_welcome()
                    break
                else:
                    descriptions.choice_error(choice)
        elif choice == '4':
            descriptions.minigames_welcome()
            while True:
                choice = input('Enter your choice: ').upper()
                if choice == '1':
                    if state == '':
                        state = '0'
                        state = minigames.guessgame(state)
                    elif state in ('0', '1', '2', '3'):
                        guess_savedatastate = minigames.guessgame(state)
                elif choice == '2':
                    minigames.cargame()
                elif choice == 'R':
                    descriptions.re_welcome()
                    break
                else:
                    descriptions.choice_error(choice)
    elif choice == 'R':
        print('Cannot return any further!')

    elif choice == 'Q':
        universal.quit()

    else:
        descriptions.choice_error(choice)