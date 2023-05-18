
#Q4

user_input = input('Enter a string:')

number_of_chars = {}
for item in user_input:
    if item in number_of_chars.keys():
        number_of_chars[item] += 1
    else:
        number_of_chars[item] = 1

print(number_of_chars)

