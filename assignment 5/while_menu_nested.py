menu_option = ''
while menu_option != 'q':
    print(f'''
Shop information FAQS:
a: boil noodles
b: stir fry beef
c: present the dish
q: quit
''')
    
    menu_option = input("Enter your choice: ")
    if menu_option == 'a':
        print('Noodle boiled!')
    elif menu_option == 'b':
        print('Beef cooked!')
    elif menu_option == 'c':
        print('Dish presented!')
        driver = input('Are you comfortable driving? AKA to become a deliverer? enter (y or n): ')
        if driver == 'y':
            print("Awesome! You will be paid extra to be a deliverer!")
        else:
            print("We won't ask you to deliver!")
