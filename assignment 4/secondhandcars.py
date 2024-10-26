# Requirements for Sales Manager Position
MAX_YEARS_USED = 10
MAX_PRICE = 10000

# User's provided data:
years_used = int(input("Enter the car's year used: "))
price = int(input('Enter your budget: '))

if years_used < MAX_YEARS_USED and price < MAX_PRICE:
    print('The car is eligible.')
else:
    print(f'''
    With the year used of
    {MAX_YEARS_USED} and the max price of {MAX_PRICE}
    the car is not eligible.

''')