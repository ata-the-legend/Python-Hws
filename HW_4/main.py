
from users import User
from getpass import getpass
import users

def sign_up() -> bool:
    """
    Signs up a new user.
    """
    print(50*'-'+'\nSign up:')
    username = input('Username: ')#.lower()
    password = getpass()
    phone_number = input('phone number:(optional) ')
    try:
        User.sign_up(username, password, phone_number)
    except users.UsernameError:
        print('This username was taken. Try again:')
        return False
    except users.PasswordError:
        print('Password should be more than 4 chars. Try again:')
        return False
    except users.EmptyError:
        print('Userame or Password cant be empty! Try again:')
        return False
    except ValueError:
        print('Invalid phone number! Try again:')
        return False
    else:
        print('Congratulations! Sign up completed.')
        return True

def sign_in() -> tuple[bool, str]:
    """
    Validates the user for signing in.

    Returns:
        tuple[bool, str]: (True for Valid users, Its username for next uses)
    """
    print(50*'-'+'\nSign in:')
    username = input("Username: ")
    password = getpass()
    try:
        return (User.validation(username, password) , username)
    except KeyError:
        print('username not found!')
        return (False, username)

def edit_prof(username: str) -> tuple[bool, str]:
    """
    Edits username and phone number of user.

    Args:
        username (str): old username

    Returns:
        tuple[bool, str]: (True for successful change, Its new username for next uses)
    """
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

def edit_pass(username: str) -> bool:
    """
    Edits password of a user.

    Args:
        username (str): Username of the user wants to change his password 

    Returns:
        bool: True for successful change
    """
    old_password = getpass('Current Password: ')
    new_password = getpass('New Password: ')
    new_password_repeat = getpass('Confirm New Password: ')
    if new_password != new_password_repeat:
        print("Repeated password must be equal to new password!")
        print('Unsuccessful Operation!')
        return False
    try:
        User.edit_password(username, old_password, new_password)
    except users.ValidationError:
        print('Wrong Password!')
    except users.PasswordError:
        print('Password should be more than 4 chars')         
    else:
        print('Password changed successfully!') 
        return True
    print('Unsuccessful Operation!')
    return False


def main():
    """
    Main func for menu
    """
    while True:
        print('\n'+50*'-'+'\nLog In')
        user_command = input(50*'-'+"\n(1 --> sign up, 2 --> sign in, 0 --> Exit): ")
        print()
        match user_command:
            case '0':
                break
            case '1':
                sign_in_flag = sign_up()
                while not sign_in_flag:
                    if input("Try again?(y/n): ").lower() == 'n':
                        break 
                    sign_in_flag = sign_up()
            case '2':
                (flag, username) = sign_in()
                while not flag:
                    print('Wrong username, password')
                    if input("Try again?(y/n): ").lower() == 'n':
                        break 
                    (flag, username) = sign_in()
                else:
                    while True:
                        print('\n'+50*'-'+'\nMain Menu')
                        signed_command = input(50*'-'+'\n(1 --> Watch-Profile, 2 --> Edit-Profile, 3 --> Change-Password, 4 --> Back-to-Log-In): ')
                        print()
                        match signed_command:
                            case '1':
                                print(f'Your Profile:\n{User.profile(username)}')
                            case '2':
                                change_profile = edit_prof(username) # if True --> profile changed 
                                while not change_profile[0]:
                                    if input("Try again?(y/n): ").lower() == 'n':
                                        break 
                                    print('Try again:')
                                    change_profile = edit_prof(username)
                                username = change_profile[1] # either this or next line
                                # if change_profile:
                                #     break
                            case '3':
                                change_pass = edit_pass(username) # if True --> pass changed 
                                while not change_pass:
                                    if input("Try again?(y/n): ").lower() == 'n':
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


if __name__ == '__main__':
    main()

