print("We are glad you have chosen to sign-up for Programmer's Toolkit Monthly Subscription Box!\n")

print("At Programmer's Toolkit Monthly Subscription Box we provide several levels of membership.\n")

print("Each level will provide you with a varying amount of product to be included in your subscription box.\n")

print("Please choose from the list below and then enter the membership level you desire to get a quote on monthly costs incurred.\n")

print("Platinum\nGold\nSilver\nBronze\nFree Trial\n")

level = input('Desired Membership Level:\n')

if level == 'Platinum':
    print('Monthly Membership Cost: $60')
elif level == 'Gold':
    print('Monthly Membership Cost: $50')
elif level == 'Silver':
    print('Monthly Membership Cost: $40')
elif level == 'Bronze':
    print('Monthly Membership Cost: $30')
elif level == 'Free Trial':
    print('Monthly Membership Cost: $0')
else:
    print('Enter a Valid Membership Level Next Time!')
