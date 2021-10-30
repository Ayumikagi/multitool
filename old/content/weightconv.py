import math

while True:

    num4 = input('Enter value: ')

    try:
        num4 = float(num4)
        break

    except ValueError:
        print(f'"{num4}" is not a valid input!')

while True:

    weight = input('(L)bs or (K)g?: ').upper()

    if weight == 'L':
        print(f'You are {num4}Lbs, that equals {num4*0.45}Kg.')
        break

    elif weight == 'K':
        print(f'You are {num4}Kg, that equals {num4/0.45}Lbs.')
        break

    elif weight == 'R':
        break

    else:
        print(f'"{weight}" is not a valid input!')