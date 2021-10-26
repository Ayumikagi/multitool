while True:

    text = input('Enter your text: ')

    if len(text) == 0:
        print('Put in something!')

    else:
        break

confirm = input('Confirm presence of: ')

if confirm in text:
    print(f'"{confirm}" can be found in the input.')

else:
    print(f'"{confirm}" not present in the input.')