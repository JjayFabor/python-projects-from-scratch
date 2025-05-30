'''
Create a program that generates random passwords based on
user-defined rules like length, inclusion of numbers, symbols, uppercase, and lowercase letters.
'''
import random

def generate_password():

    print('\nPassword Generator\n')
    print("Answer the following questions for a more  secured and customized password.\n")
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    password_length = int(input("Enter password length: "))
    is_number_included = input("Do you want to include numbers (Y/N): ").lower()
    is_symbol_included = input("Do you want to include symbols (Y/N): ").lower()
    is_uppercase = input("Do you want to want to include uppercase letters (Y/N): ").lower()
    is_lowercase = input("Do you want to include lowercase letters (Y/N): ").lower()

    required_chars = []
    allowed_chars_pool = ''

    if (is_number_included == 'y'):
        required_chars.append(random.choice(digits))
        allowed_chars_pool += digits
    if (is_symbol_included == 'y'):
        required_chars.append(random.choice(symbols))
        allowed_chars_pool += symbols
    if (is_lowercase == 'y'):
        required_chars.append(random.choice(lowercase))
        allowed_chars_pool += lowercase
    if (is_uppercase == 'y'):
        required_chars.append(random.choice(uppercase))
        allowed_chars_pool += uppercase

    remaining_chars = password_length - len(required_chars)
    random_chars = ''.join(random.choices(allowed_chars_pool, k=remaining_chars))
    password = ''.join(required_chars) + random_chars
    password = (list(password))
    random.shuffle(password)
    return ''.join(password)



print(generate_password())
