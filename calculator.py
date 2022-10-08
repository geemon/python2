#calculator script in python

from unittest import result


print('Welcome to the Matrix calculator\n')
try:
    f_number =int( input('Input your first number\n'))

    s_number = int(input('Input your second number\n' ))
except ValueError:
    print('please provid only digits')

else:
     result = f_number + s_number
     print(f' the sum of {f_number} + {s_number} == {result}')


