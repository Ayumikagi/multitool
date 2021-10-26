while True:

    text = input('Enter your text: ')

    if len(text) == 0:
        print('Put in something!')

    else:
        break

form = input('(U)PPERCASE or (l)owercase?:').upper()

if form in ('UPPER, UPPERCASE, U, UP'):
    print(text.upper())

elif form in ('LOWER, LOWERCASE, L, LOW'):
    print(text.lower())
