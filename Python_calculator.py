
def start_calc():
    print('-------------------------------------------------------------------------------------')
    print('Hello there')
    print('What is your name?')
    name = input('name: ')
    print('-------------------------------------------------------------------------------------')
    #asks for the users name
    print(f'Okay {name}, what do you want to do?')
    choice()

def buffer():
    choice()
    
def choice():
    print('Addition: +\nSubtraction: -\nMultiplication: *\nDivision: /')
    print('-------------------------------------------------------------------------------------')
    choice = input('Your choice: ')
    print('-------------------------------------------------------------------------------------')
    if choice == '+':
        start_add()
        
    elif choice == '-':
        start_sub()

    elif choice == '*':
        start_mul()
       
    elif choice == '/':
        start_div()
       
    else:
        print('Invalid choice')
        buffer()


def start_add():
    print('Type two numbers to add together')
    num1 = int(input('Number1: '))
    num2 = int(input('Number2: '))
    result = num1 + num2
    print(f'Your result is: {result}')
    print('-------------------------------------------------------------------------------------')
    choice()

def start_sub():
    print('Type two numbers to subtract together')
    num1 = int(input('Number1: '))
    num2 = int(input('Number2: '))
    result = num1 - num2
    print(f'Your result is: {result}')
    print('-------------------------------------------------------------------------------------')
    choice()

def start_mul():
    print('Type two numbers to multiply together')
    num1 = int(input('Number1: '))
    num2 = int(input('Number2: '))
    result = num1 * num2
    print(f'Your result is: {result}')
    print('-------------------------------------------------------------------------------------')
    choice()

def start_div():
    print('Type two numbers to divide together')
    num1 = int(input('Number1: '))
    num2 = int(input('Number2: '))
    result = num1 / num2
    print(f'Your result is: {result}')
    print('-------------------------------------------------------------------------------------')
    choice()

start_calc()
