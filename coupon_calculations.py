def calculate_price():
    price = input('Enter Price of Order Before Discount, Shipping, and Tax: ')

    condition1 = input('\nDo you have a cash-off coupon? Enter Y or N.\n')

    if condition1 == 'Y':
        cash_coupon = input('\nEnter Cash Coupon Value: ')
        if cash_coupon == 5 or 10:
            pass
        else:
            print('\nInvalid Entry, Please Enter a Valid Promotion')
            quit()
    elif condition1 == 'N':
        cash_coupon = 0
    else:
        print('\nInvalid Entry, Please enter Y or N next time...')
        quit()

    price1 = round((float(price) - float(cash_coupon)), 2)

    condition2 = input('\nDo you have a percent discount? Enter Y or N.\n')

    if condition2 == 'Y':
        percent_coupon = input('\nEnter Percent Off: ')
        if percent_coupon == 10 or 15 or 20:
            price2 = round(float(price1) - (float(price1) * (float(percent_coupon) / 100)), 2)
        else:
            print('\nInvalid Entry, Please Enter a Valid Promotion')
            quit()
    elif condition2 == 'N':
        price2 = price1
    else:
        print('\nInvalid Entry, Please enter Y or N next time...')
        quit()

    if price2 < 10:
        shipping = 5.95
    elif 10 <= price2 < 30:
        shipping = 7.95
    elif 30 <= price2 < 50:
        shipping = 11.95
    else:
        shipping = 0

    tax = round((price2 * .06), 2)

    price3 = round((price2 + tax) + shipping, 2)

    print('\nPrice Before Discount: $', price)

    print('Price After Discount: $', price2)

    print('Tax: $', tax)

    print('Shipping: $', shipping)

    print('\nTotal Cost of Order: $', price3)

if __name__ == '__main__':
    calculate_price()
