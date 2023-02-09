'''password generator'''

from random import choice
from string import ascii_letters, digits

all_symbols = ascii_letters + digits

def password_generator(len_password  : int):
    print(''.join([choice(all_symbols) for i in range(len_password)]))

print('''Hi this password generator it will make 10 password options of the size you need''')

while True:
    try:
        len_pass = int(input('Enter size password -> '))
    except:
        print('Enter number please')

    print()

    for i in range(10):
        password_generator(len_pass)

    print('\nIf you find a fake password write otherwise write no and the program will generate a new set of passwords')
    yes_no = input('Enter Yes or No ->')
    if yes_no[0] in 'Nn':
        print('Goodbye')
        break