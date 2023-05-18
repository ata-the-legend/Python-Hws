
#Q2

user_input = input('Enter a number:')


if user_input.isnumeric():
    print(user_input[::-1])
else:
    print('It is not an integer!')

########## هر نوع ورودی از جنس عدد را تشخیص بده
flag_dot = 0
flag = 1
for item in user_input:
    if item == '-' and user_input[0] != '-' or user_input[-1] == '.' or flag_dot > 1:
        flag = 0
        break
    elif item == '.':
        flag_dot += 1
    elif not item.isnumeric() and item != '-':
        flag = 0
        break

if flag:
    print(user_input[::-1])
else:
    print('It is not a number!')

