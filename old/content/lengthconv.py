import math

while True:

    num4 = input('Enter value: ')

    try:
        num4 = float(num4)
        break

    except ValueError:
        print(f'"{num4}" is not a valid input!')

while True:

    length = input('What unit is that? (Choose from metric, fuck imperial): ').upper()

    if length == 'MM':
        print(f'''{num4}mm is equal to:
                                
Metric: {num4/10}cm / {num4/100}dm / {num4/1000}m / {num4/1000000}km
Imperial: {num4/25.4}in / {num4/304.8}ft / {num4/914.4}yd / {num4/1609343.97}mi
                                ''')
        break

    elif length == 'CM':
        print(f'''{num4}cm is equal to:
                                
Metric: {num4/0.1}mm / {num4/10}dm / {num4/100}m / {num4/100000}km
Imperial: {num4/2.54}in / {num4/30.48}ft / {num4/91.44}yd / {num4/160934.39}mi
                                ''')
        break

    elif length == 'DM':
        print(f'''{num4}dm is equal to:
                                
Metric: {num4/0.01}mm / {num4/0.1}cm / {num4/10}m / {num4/10000}km
Imperial: {num4/0.254}in / {num4/3.048}ft / {num4/9.144}yd / {num4/16093.43}mi
                                ''')
        break

    elif length == 'M':
        print(f'''{num4}m is equal to:
                                
Metric: {num4/0.001}mm / {num4/0.01}cm / {num4/0.1}dm / {num4/1000}km
Imperial: {num4/0.0254}in / {num4/0.3048}ft / {num4/0.9144}yd / {num4/1609.34}mi
                                ''')
        break

    elif length == 'KM':
        print(f'''{num4}km is equal to:
                                
Metric: {num4/0.000001}mm / {num4/0.00001}cm / {num4/0.0001}dm / {num4/1000}m
Imperial: {num4/0.0000254}in / {num4/0.0003048}ft / {num4/0.0009144}yd / {num4/1.6}mi
                                ''')
        break

    elif length == 'R':
        break

    else:
        print(f'"{length}" is not a valid input!')