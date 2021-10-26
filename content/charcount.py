while True:

    text = input('Enter your text: ')

    if len(text) == 0:
        print('Put in something!')

    else:
        break

print(f' Length of your input is {(len(text))} character(s).')
