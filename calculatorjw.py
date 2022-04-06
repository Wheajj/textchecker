print('Type two numbers that when added are less than 100')

num1 = int(input('Type a number :'))
num2 = int(input('Type another number :'))

add = (num1+num2)

if add >= 100:
    print('Error: sum is over 100')
if add < 100:
    print(add)
