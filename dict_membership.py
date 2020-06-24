def in_dict():
    d = {'Shampoo':10, 'Conditioner':15, 'Hair Gel':12}

    b = input('Enter a hair product to see if we have it: ')

    if b in d:
        print('True')
    else:
        print('False')

in_dict()
