menu_option = ''
while menu_option != 'q':
    print('MENU:','a: boil noodles', 'b: stir fry beef', 'c: present the dish', 'q: quit')
    menu_option = input("Enter your choice: ")
    if menu_option == 'a':
        print('Noodle boiled!')
    elif menu_option == 'b':
        print('Beef cooked!')
    elif menu_option == 'c':
        print('Dish presented!')
