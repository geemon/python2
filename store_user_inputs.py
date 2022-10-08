store_user = 'user_info.txt'
with open(store_user , 'a') as file:
    username = input( 'please enter name\n')
    userage = input('please provide your age below\n')
    user_info = f"{username} {userage}"
    file.write(f'\n{user_info}')
    #file.write(userage)