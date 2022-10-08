guest = True
while guest:
    name = input('please provide your name to the receptionist\n')
    print(f'welcome,{name}')
    with open('guest_book.txt', 'a') as file:
        file.write(f'{name}\n')
    ans= input('Is there any other guest yet:"y"/"n"')
    if ans == 'n':
        break
    else:
         continue

