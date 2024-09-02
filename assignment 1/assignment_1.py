def String_Quoting():
    print('hello world')
    print("'amy' is a name")
    print('''this is the first line.
        this is the second line.
this is the third line.
        ''')
    return

def String_Escaping():
    string = 'this is amy\'s car'
    print(string)
    return 

def TypeConversion_Casting():
    num_string = '129'
    num_int = 0
    num_int = int(num_string)
    print('num string: ',num_string)
    print('num int: ',num_int)
    return

def Input_Concatenation():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    full_name = first_name + last_name
    print(full_name)
    return

def Using_fstrings():
    name = 'Daniel'
    age = 23
    print(f"Hello, My name is {name} and I'm {age} years old.")
    return

def Math():
    temp = []

    for i in range(3):
        temp_int = input(f"Enter your {i+1} integer: ")
        temp.append(int(temp_int))
    res = (temp[0]*temp[1])**2 - temp[2]
    print(res)
    return

def Currency_Formatting():
    temp = []

    for i in range(3):
        temp_int = input(f"Enter your {i+1} float: ")
        temp.append(float(temp_int))
    currency = (temp[0]*temp[1])**2 - temp[2]
    print(currency)
    return

def Demo_the_end_parameter():
    print('Some text and',end = ' ')
    print('some other text.')
    return

def Demo_the_sep_parameter():
    print('01','29','2024', sep = '-')
    return

if __name__ =="__main__":
    #String_Quoting()
    
    #String_Escaping()

    #TypeConversion_Casting()

    #Input_Concatenation()

    #Using_fstrings()

    #Math()

    #Currency_Formatting()

    Demo_the_end_parameter()

    Demo_the_sep_parameter()