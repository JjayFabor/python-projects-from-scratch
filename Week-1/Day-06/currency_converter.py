'''
Build a currency converter that converts a fixed amount from
one currency to another using static exchange rates stored in a dictionary.
'''

def convert(rate, symbol):
    user_money = float(input("Enter any amount: "))
    user_money = round((user_money * rate), 2)
    return f'\nConverted user money => {user_money} {symbol}\n\n'

def currency_converter():
    rate_conversion = {
        'PHP_TO_USD': 0.0175,
        'USD_TO_PHP': 57.14,
    }

    while True:
        print("1. Philippine Peso (PHP) to United States of America (USD) ")
        print("2. United States of America (USD)  to Philippine Peso (PHP)")
        print("3. Quit")

        user_input = int(input("\nChoose a currency converter: "))

        match (user_input):
            case 1:
                print(convert(rate_conversion['PHP_TO_USD'], 'USD'))

            case 2:
                print(convert(rate_conversion['USD_TO_PHP'], 'PHP'))
            case 3:
                print('\nThank you for using the currency converter.\n')
                break
            case _:
                print('\nCHOOSE A CORRECT CONVERSION.\n')


if __name__ == '__main__':
    print("Welcome to a simple currency converter!\n")
    currency_converter()
