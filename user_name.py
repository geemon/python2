from name_function import full_name

print('press q to exit the program')
while True:
    first = input('Please input your first name\n')
    if first == 'q':
        break
    last = input('please provide your surname\n')
    if last == 'q':
        break

    username = full_name(first,last)
    print(f'your full name is {username}')
    