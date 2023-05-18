
#Q3

vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

user_input = input("Enter a string:")
output = []

for item in user_input:
    if item == " ":
        continue
    elif item in vowels:
        output.append('.')
    elif item.isupper():
        output.append(item.lower())
    elif item.islower():
        output.append(item.upper())
    else:
        output.append(item)


print(''.join(output))


