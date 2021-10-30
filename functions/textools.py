from functions import descriptions
from functions import universal

def find_pos(text):
    find = input('Find what?: ')
    text.find(find)
    if text.find(find) == -1:
        result = 'fail'
    else:
        result = text.find(find)
    return result, find


def replace(text):
    while True:
        original = input('Replace what?: ')
        if text.find(original) == -1:
            print(f'"{original}" not found in the text.')
        else:
            break
    new = input('With what?: ')
    result = text.replace(original, new)
    return result


def count_end():
    while True:
        choice = input('Enter your choice: ')
        if choice == '1':
            descriptions.textools_welcome()
            back = True
            break
        elif choice == '2':
            universal.quit()
        else:
            descriptions.choice_error(choice)


def upperlower(choice, text):
    if choice == '1':
        result = text.upper()
    elif choice == '2':
        result = text.lower()
    elif choice == 'R':
        result = 'back'
    else:
        result = 'fail'
    return result


def upper_end(text):
    while True:
        choice = input('Enter your choice: ')
        if choice == '1':
            result = text.lower()
        elif choice == '2':
            result = 'back'
        elif choice == '3':
            universal.quit()
        else:
            descriptions.choice_error(choice)
        return result


def lower_end(text):
    while True:
        choice = input('Enter your choice: ')
        if choice == '1':
            result = text.upper()
        elif choice == '2':
            result = 'back'
        elif choice == '3':
            universal.quit()
        else:
            descriptions.choice_error(choice)
        return result


def f_end():
    while True:
        choice = input('Enter your choice: ')
        if choice == '1':
            back = False
            break
        elif choice == '2':
            descriptions.textools_welcome()
            back = True
            break
        elif choice == '3':
            universal.quit()
        else:
            descriptions.choice_error(choice)
    return back