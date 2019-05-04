# 1. Asks the user to enter his/her last name.
# 2. Asks the user to enter his/her first name.
# 3. Prints out the user’s first and last names in that order. 

def hello_world():
    print('What is your first name?')
    first_name = input()
    print('What is your last name?')
    last_name = input()
    print('Nice to meet you, ' + first_name + ' ' + last_name)

hello_world()
