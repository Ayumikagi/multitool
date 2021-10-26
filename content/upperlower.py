while True:

    text = input('Enter your text: ')

    if len(text) == 0:
        print('Put in something!')

    else:
        break

form = input('(U)PPERCASE or (l)owercase?:')

if form.upper() in ('UPPER, UPPERCASE, U, UP'):
    print(text.upper())

elif form.upper() in ('LOWER, LOWERCASE, L, LOW'):
    print(text.lower())