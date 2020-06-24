def test_in_dict_true():
    d = {'Shampoo':10, 'Conditioner':15, 'Hair Gel':12}
    if 'Shampoo' in d:
        print('True')
    else:
        print('False')
    if 'Mousse' in d:
        print('True')
    else:
        print('False')

test_in_dict_true()
