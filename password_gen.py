#CoolPasswordGenerator
import random


keys = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def weak():
    result = ''
    for i in range(0,6):
        result += random.choice(keys)
    return result

def medium():
    result = ''
    for i in range(8,12):
        result += random.choice(keys)
    return result


def strong():
    result = ''
    for i in range(10,18):
        result += random.choice(keys)
    return result
    
def main():
    print('\n1.Weak')
    print('2.Medium')
    print('3.Strong\n')

    user = input('Select an option > ')

    if user == '1':
        password = weak()
    elif user == '2':
        password = medium()
    elif user == '3':
        password = strong()
    else:
        exit()

    print(password)


while True:
    main()

