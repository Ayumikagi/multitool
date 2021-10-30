import textwrap
from functions import descriptions
from functions import universal

def weight_conv(value):
    descriptions.weight_units()
    while True:
        choice = input('Enter your choice: ').upper()
        if choice == '1':
            units = 'kg'
            result = value / 0.45
            break
        elif choice == '2':
            units = 'lbs'
            result = value * 0.45
            break
        elif choice == 'R':
            result = 'back'
            break
        else:
            descriptions.choice_error(unit)
    return result, units


def conv_end():
    while True:
        choice = input('Enter your choice: ')
        if choice == '1':
            result = 'redo'
            break
        elif choice == '2':
            result = 'back'
            break
        elif choice == '3':
            universal.quit()
        else:
            descriptions.choice_error(choice)
    return result


def length_units(value):
    descriptions.length_units()
    while True:
        choice = input('Enter your choice: ').upper()
        if choice == '1':
            result = 'mm'
            print(textwrap.dedent(f'''
            {value}mm is equal to:
                                
            Metric: {value/10}cm / {value/100}dm / {value/1000}m / {value/1000000}km
            Imperial: {value/25.4}in / {value/304.8}ft / {value/914.4}yd / {value/1609343.97}mi
            '''))
            break
        elif choice == '2':
            result = 'cm'
            print(textwrap.deden(f'''
            {value}cm is equal to:
                                
            Metric: {value/0.1}mm / {value/10}dm / {value/100}m / {value/100000}km
            Imperial: {value/2.54}in / {value/30.48}ft / {value/91.44}yd / {value/160934.39}mi
            '''))
            break
        elif choice == '3':
            result = 'dm'
            print(textwrap.dedent(f'''
            {value}dm is equal to:
                                
            Metric: {value/0.01}mm / {value/0.1}cm / {value/10}m / {value/10000}km
            Imperial: {value/0.254}in / {value/3.048}ft / {value/9.144}yd / {value/16093.43}mi
            '''))
            break
        elif choice == '4':
            result = 'm'
            print(textwrap.dedent(f'''
            {value}m is equal to:
                                
            Metric: {value/0.001}mm / {value/0.01}cm / {value/0.1}dm / {value/1000}km
            Imperial: {value/0.0254}in / {value/0.3048}ft / {value/0.9144}yd / {value/1609.34}mi
            '''))
            break
        elif choice == '5':
            result = 'km'
            print(textwrap.dedent(f'''
            {value}km is equal to:
                                
            Metric: {value/0.000001}mm / {value/0.00001}cm / {value/0.0001}dm / {value/1000}m
            Imperial: {value/0.0000254}in / {value/0.0003048}ft / {value/0.0009144}yd / {value/1.6}mi
            '''))
            break
        elif choice == 'R':
            result = 'back'
            break
        else:
            descriptions.choice_error(choice)
    return result


def temp_conv(value):
    result = ''
    descriptions.temp_units()
    while True:
        choice = input('Enter your choice: ').upper()
        if choice == '1':
            celsius = True
            fahrenheit = (value * 1.8) + 32
            kelvin = value + 273.15
            break
        elif choice == '2':
            celsius = (value - 32) * 1.8
            fahrenheit = True
            kelvin = (value - 32) * 1.8 + 273.15
            break
        elif choice == '3':
            celsius = num4 - 273.15
            fahrenheit = (num4 - 273.15) * 1.8 + 32
            kelvin = True
            break
        elif choice == 'R':
            result = ''
            break
        else:
            descriptions.choice_error(choice)
    return celsius, fahrenheit, kelvin, result