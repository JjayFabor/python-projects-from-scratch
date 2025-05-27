'''
Create a command-line calculator that takes two numbers and an operator from the user and
performs basic arithmetic operations like addition, subtraction, multiplication, and division.
'''

def simple_calculator():
    print('Welcome to simple Calculator.\n\n\n')

    op = input("Enter operator [+, -, *, /]: ")
    n1 = int(input("\nEnter the first number: "))
    n2 = int(input("Enter the second number: "))

    match op:
        case '+':
            print(eval('n1 + n2'))
        case '-':
            print(eval('n1 - n2'))
        case '*':
            print(eval('n1 * n2'))
        case '/':
            print(int(eval('n1 / n2')))
        case _:
            print('Enter correct operator.')

simple_calculator()
