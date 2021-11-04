import math
from functions import descriptions
from functions import universal

def add(num1, num2):
    result = num1 + num2
    return result


def subtract(num1, num2):
    result = num1 - num2
    return result


def multiply(num1, num2):
    result = num1 * num2
    return result


def divide(num1, num2):
    result = num1 / num2
    rounded = num1 // num2
    modulo = num1 % num2
    return result, rounded, modulo


def round(num):
    result = round(num)
    return result


def sqrt(num):
    result = num ** 0.5
    return result


def exponent(num):
    while True:
        try:
            exp = float(input('Enter exponent: '))
            break
        except ValueError:
            print(f'"{exp}" is not a valid value.')
    result = num ** exp
    return result, exp


def abs(num):
    if num < 0:
        result = num * -1
    else:
        result = num
    return result


def floor_ceil(num):
    result1 = math.floor(num)
    result2 = math.ceil(num)
    return result1, result2


def math_f_end():
    while True:
        choice = input ('Enter your choice: ')
        if choice == '1':
            descriptions.calc_welcome()
            back = True
            break
        elif choice == '2':
            universal.quit()
        else:
            descriptions.choice_error(choice)
    return back


def factorial(num):
    result = 1
    while num > 0:
        if num == 0:
            break
        else:
            result *= num
            num -= 1
    return result
