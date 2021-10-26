while True:

    text = input('Enter your text: ')

    if len(text) == 0:
        print('Put in something!')

    else:
        break

while True:

    search = input('Enter key value: ')

    (text.find(search))

    if (text.find(search)) == -1:
        print(f'Cannot find "{search}"')

    else:
        print(f'"{search}" found at position {(text.find(search))}.')
        break