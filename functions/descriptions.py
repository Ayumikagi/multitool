import textwrap


def welcome(user_name):
        print(f'''
Hey {user_name}, welcome to multitool v3.0.0!
Enter the assigned function number to proceed.
Press R to return to previous menu.

What would you like to do?:

[1. Calculator]  [2. Text Tools]
[3. Converter]   [4. Minigames]
''')


def re_welcome():
        print('''
What would you like to do?:

[1. Calculator]  [2. Text Tools]
[3. Converter]   [4. Minigames]
''')


def calc_welcome():
        print('''
What would you like to do? [Calculator mode]:

[1. Add] [2. Subtract] [3. Multiply] [4. Divide] [5. Round]
[6. Square root] [7. Exponentation] [8. Absolute] [9. Floor/Ceiling]
[10. Factorial]
''')


def textools_welcome():
        print('''
What would you like to do? [Text Tools mode]: 

[1. Find] [2. Replace] [3. Count] [4. ALL UPPERCASE/lowercase]
''')


def textools_find_redo():
        print('''
Search again?:

[1. Yes] [2. No] [3. Quit]
''')


def textools_replace_redo():
        print('''
Replace again?:

[1. Yes] [2. No] [3. Quit]        
''')


def textools_count_end():
        print('''
What would you like to do next?

[1. Return to Text Tools menu] [2. Quit]
''')


def upperlower():
        print('''
Make all of your text:

[1. UPPERCASE] [2. Lowercase]
''')


def upper_end():
        print('''
Would you like to...:

[1. Make it lowercase] [2. Return to Text Tools menu] [3. Quit]
''')


def lower_end():
        print('''
Would you like to...:

[1. Make it UPPERCASE] [2. Return to Text Tools menu] [3. Quit]
''')


def f_end():
        print('''
What would you like to do next?

[1. Return to Calculator menu] [2. Quit]
''')


def choice_error(choice):
        print(f'"{choice}" is not a valid input.')


def converter_welcome():
        print('''
What would you like to do? [Converter mode]:

[1. Convert Weight] [2. Convert Length] [3. Convert Temperature]
''')


def weight_units():
        print('''
What units?:

[1. Kilograms] [2. Pounds]
''')


def length_units():
        print('''
What units?:

[1. Milimeters] [2. Centimeters] [3. Decimeters]
[4. Meters] [5. Kilometers]
''')


def temp_units():
        print('''
What units?:

[1. Celsius] [2. Fahrenheit] [3. Kelvin]
''')


def conv_end():
        print('''
Would you like to:

[1. Return to Converter menu] [2. Return to Tools menu] [3. Quit]
''')


def minigames_welcome():
        print('''
What would you like to play? [Minigames mode]:

[1. Guess the Number] [2. Car Game] [3. Trivia Game]
''')

def guessgame_welcome_0():
        print('''
Choose your difficulty:
[1. Easy (1-10)] [2. Normal (1-20)] [3. Hard (1-30)]
''')


def guessgame_welcome_1():
        print('''
Choose your difficulty:
[1. Easy (1-10)] [2. Normal (1-20)] [3. Hard (1-30)]
[4. Extreme (1-50)]
''')


def guessgame_welcome_2():
        print('''
Choose your difficulty:
[1. Easy (1-10)] [2. Normal (1-20)] [3. Hard (1-30)]
[4. Extreme (1-50)] [5. Insane (1-100)]
''')


def guessgame_welcome_3():
        print('''
Choose your difficulty:
[1. Easy (1-10)] [2. Normal (1-20)] [3. Hard (1-30)]
[4. Extreme (1-50)] [5. Insane (1-100)] [6. Gigachad (1-250)]
''')


def cargame_welcome():
        print('''
Welcome to Car Game! Available commands:
[accel] [stop] [quit]       
''')
