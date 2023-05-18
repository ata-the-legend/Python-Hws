
from users import User
import users

# user1 = User('Ata', '123')
user2 = User('Ata', '1234')
user3 = User('Ali', '123532')
user4 = User('javad', '1235151')
# user5 = User('Ata', '123654')

print(user2)
print(user3)
print(user3.phone_number)
# print(user3.__password)
print(user3.id)
print(user3.id)
print(user4.id)
user4.phone_number = "123356"
print(user4.phone_number)
print(user4.id)

print(User.users())


user2 = User('Ata1', '1234')
user2 = User('Ata2', '1234')
user2 = User('Ata3', '1234')
user2 = User('Ata4', '1234')
user2 = User('Ata5', '1234')
user2 = User('Ata6', '1234')
user2 = User('Ata7', '1234')
# user2 = User('Ata8', '1234')


print(user2)
print(User.users())
print('\n')
########################################################

def sign_up():
    print('Sign up:')
    username = input('Username: ')#.lower()
    password = input('Password: ')
    phone_number = input('phone number:(optional) ')
    try:
        User.sign_up(username, password, phone_number)
    except users.UsernameError:
        print('This username was taken. Try again:')
        sign_up()
    except users.PasswordError:
        print('Password should be more than 4 chars. Try again:')
        sign_up()
    except users.EmptyError:
        print('Userame or Password cant be empty! Try again:')
        sign_up()
    except ValueError:
        print('Invalid phone number! Try again:')
        sign_up()
    else:
        print('Congratulations! Sign up completed.')

def sign_in():
    print('Sign in:')
    username = input("Username: ")
    password = input("Password: ")
    try:
        return (User.validation(username, password) , username)
    except KeyError:
        print('username not found!')
        return (False, username)
    # return True
    # return False
    # 'username not found'
    # 'wrong password'

def edit_prof(username):
    new_username = input('New username: ')
    new_phone_number = input('New phone number: ')
    try:
        User.edit_profile(username, new_username, new_phone_number)
    except users.UsernameError:
        print('This username was taken.')
    except users.EmptyError:
        print('Userame cant be empty!')
    except ValueError:
        print('Invalid phone number!')
    else:
        print('Username changed successfully!') 
        return (True, new_username)
    print('Unsuccessful Operation!')
    return (False, username)

def edit_pass(username: str):
    old_password = input('Current Password: ')
    new_password = input('New Password: ')
    new_password_repeat = input('Repeat New Password: ')
    if new_password != new_password_repeat:
        print("Repeated password must be equal to new password!")
        print('Unsuccessful Operation!')
        return False
    if User.validation(username, old_password):
        try:
            User.edit_password(username, new_password)
        except users.PasswordError:
            print('Password should be more than 4 chars')         
        else:
            print('Password changed successfully!') 
            return True
    else:
        print('Wrong Password!')
    print('Unsuccessful Operation!')
    return False


# def main():
command = 1
while command:
    print('\n'+50*'-'+'\nMain Menu')
    user_command = input(50*'-'+"\n(1 --> sign up, 2 --> sign in, 0 --> Exit): ")
    print()
    match user_command:
        case '0':
            command = 0
            continue
        case '1':
            sign_up()
        case '2':
            (flag, username) = sign_in()
            while not flag:
                print('Wrong username, password')
                if input("Go back?(y/n): ").lower() == 'y':
                    break 
                (flag, username) = sign_in()
            else:
                while True:
                    print('\n'+50*'-'+'\nSigned in!')
                    signed_command = input(50*'-'+'\n(1 --> Watch-Profile, 2 --> Edit-Profile, 3 --> Change-Password, 4 --> Back-to-Main-Menu): ')
                    print()
                    match signed_command:
                        case '1':
                            print(f'Your Profile:\n{User.profile(username)}')
                        case '2':
                            change_profile = edit_prof(username) # if True --> profile changed 
                            while not change_profile[0]:
                                if input("Go back?(y/n): ").lower() == 'y':
                                    break 
                                print('Try again:')
                                change_profile = edit_prof(username)
                            username = change_profile[1] # either this or next line
                            # if change_profile:
                            #     break
                        case '3':
                            change_pass = edit_pass(username) # if True --> pass changed 
                            while not change_pass:
                                if input("Go back?(y/n): ").lower() == 'y':
                                    break 
                                print('Try again:')
                                change_pass = edit_pass(username)
                            if change_pass:
                                break
                        case '4':
                            break
                        case _:
                            print('Invalid Command!')
        case _:
            print("Invalid command!")





    # try:
    #     command = int(user_command)
    #     if command == 0:
    #         continue
    #     elif command not in [1,2]:
    #         command = 1
    #         print("Invalid command!")
    #         continue
    # except ValueError:
    #     command = 1
    #     print("Invalid command!")
    #     continue

    # if command == 1:
    #     sign_up()
    # elif command == 2: #mishe nazasht elifo (bala check shode) --> bayad ye continue bara if bala bzarim
    #     while not sign_in():
    #         print('Wrong username, password')
    #         if input("Go back?(y/n): ").lower() == 'y':
    #             break 
    #     else:
    #         print('Signed in!')
    #         signed_command = input('(1-->Watch-Profile, 2-->Edit-Profile, 3-->Change-Password, 4-->Back-to-Main-Menu): ')
    #         match signed_command:
    #             case '1':
    #                 pass
    #             case '2':
    #                 pass
    #             case '3':
    #                 pass
    #             case '4':
    #                 pass
    #             case _:
    #                 print('Invalid Command!')



