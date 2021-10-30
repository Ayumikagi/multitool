import math

while True:

    num4 = input('Enter value: ')

    try:
        num4 = float(num4)
        break

    except ValueError:
        print(f'"{num4}" is not a valid input!')

while True:

    temp = input('What scale? (Celsius/Fahrenheit/Kelvin): ').upper()

    if temp in ('CELSIUS', 'C'):
        print(f'{num4}°C equals to {(num4*1.8)+32}F or {num4+273.15}K')
        break

    elif temp in ('FAHRENHEIT', 'F'):
        print(f'{num4}F equals to {(num4-32)*1.8}°C or {(num4-32)*1.8+273.15}K')
        break

    elif temp in ('KELVIN', 'K'):
        print(f'{num4}K equals to {num4-273.15}°C or {(num4-273.15)*1.8+32}F')
        break

    elif temp == 'R':
        break

    else:
        print(f'"{temp}" is not a valid input!')