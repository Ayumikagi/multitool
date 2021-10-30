while True:

    text = input('Enter your text: ')

    if len(text) == 0:
        print('Put in something!')

    else:
        break

while True:

    replace = input('Choose a letter or string to replace: ')

    (text.find(replace))

    if (text.find(replace)) == -1:
        print(f'Cannot find "{replace}"')

    else:
        replacement = input(f'Replace "{replace}" with: ')
        print(text.replace(replace, replacement))
        break