"""
Create and save the users and their additional info.

Classes:

    User:
        A class for create users. 
        This class uses hash algoritem SHA256 to save passwords.

Raises:
    PasswordError: For invalid passwords
    UsernameError: For repeating username
    EmptyError: For empty given username
    ValueError: For invalid phone number
    ValidationError: For Wrong password

"""

import uuid
import hashlib
import json

class UsernameError(ValueError):
    pass

class PasswordError(ValueError):
    pass

class EmptyError(ValueError):
    pass

class ValidationError(ValueError):
    pass


class User:
    """
    A class to represent a user.

    ...

    Attributes
    ----------
    username : str
        username of the user
    password : str
        password of the user
    phone_number : str
        phone number of the user
    id: str
        A unique ID for each user

    Methods
    -------
    sign_up(cls, username: str, password: str, phone_number: str) -> None:
        Creates a new user
    validation(username: str, password: str) -> bool:
        Validates the password for a user
    profile(cls, username: str) -> 'User':
        Returns username, phone number and id of a user
    edit_profile(cls, old_username: str, new_username: str, new_phone_number: str) -> None:
        Changes a users username and phone number
    edit_password(username: str, old_password: str, new_password: str) -> None:
        Changes a users password
    """
    __users = {}
    def __init__(self, username: str, password: str, id: str, phone_number: str | None = None) -> None:
        """
        Initializes all the necessary attributes for the person object.

        Args:
            username (str): username of the user
            password (str): password of the user
            id (str): A unique ID for each user
            phone_number (str | None, optional): phone number of the user. Defaults to None.
        """
        self.username = username
        # if len(password) < 4:
        #     raise PasswordError('Password should be more than 4 chars') 
        self.__password = password 
        # self.__password = hashlib.sha256(password.encode()).hexdigest()
        # self.id = uuid.uuid4()
        self.id = id
        self.phone_number = phone_number
        type(self).__users[self.username] = self

    @property
    def username(self) -> str:
        """
        Getter for username attribute
        """
        return self._username

    @username.setter
    def username(self, username: str) -> None:
        """
        Setter for username attribute
        """
        if username in User.__users.keys():
            raise UsernameError('This username was taken.')
        elif username == '' or username.isspace():
            raise EmptyError('Userame cant be empty!')
        self._username = username

    def __str__(self) -> str:
        return f'Username: {self.username}\nPhone Number: {self.phone_number}\nID: {self.id}'

    def __repr__(self) -> str:
        return f'({self.username}, {self.__password}, {self.phone_number}, {self.id})'

    def users() -> dict:
        """
        Shows all users

        Returns:
            dict: All signed up users
        """
        return User.__users
    
    @classmethod
    def sign_up(cls, username: str, password: str, phone_number: str) -> None:
        """
        Creates an object of user

        Args:
            username (str): username of the user
            password (str): password of the user
            phone_number (str | None, optional): phone number of the user. Defaults to None.
        """
        if len(password) < 4:
            raise PasswordError('Password should be more than 4 chars') 
        password = hashlib.sha256(password.encode()).hexdigest()
        id = str(uuid.uuid4())
        if not phone_number:
            cls(username, password, id)
        elif not phone_number.isnumeric() or len(phone_number) != 11:
            raise ValueError('Invalid phone number!')
        else:
            cls(username, password, id, phone_number)

    @staticmethod
    def validation(username: str, password: str) -> bool:
        """
        Validates a users password

        Args:
            username (str): username of the user
            password (str): password of the user

        Returns:
            bool: True for right password
        """
        return User.__users[username].__password == hashlib.sha256(password.encode()).hexdigest()

    @classmethod
    def profile(cls, username: str) -> 'User':
        """
        Checks users profile

        Args:
            username (str): username of the user

        Returns:
            User: Asked user object
        """
        return cls.__users[username]
    
    @classmethod
    def edit_profile(cls, old_username: str, new_username: str, new_phone_number: str) -> None:
        """
        Changes a users username and phone number

        Args:
            old_username (str): Current username of the user
            new_username (str): New username of the user
            new_phone_number (str): New phone number of the user
        """
        user = cls.__users[old_username] 
        if not new_phone_number or new_phone_number.isspace():
            # pass                     # if we dont want to delete the number from database
            user.phone_number = None
        elif not new_phone_number.isnumeric() or len(new_phone_number) != 11:
            raise ValueError('Invalid phone number!')
        else:                          
            user.phone_number = new_phone_number
        if new_username == old_username:
            pass
        else:
            user.username = new_username
            cls.__users[new_username] = cls.__users[old_username] 
            del cls.__users[old_username] 

    @staticmethod
    def edit_password(username: str, old_password: str, new_password: str) -> None:
        """
        Changes a password of a user
  
        Args:
            username (str): username of the user
            old_password (str): Current password of the user
            new_password (str): New password of the user
        """
        if not User.validation(username, old_password):
            raise ValidationError('Wrong password')
        elif len(new_password) < 4:
            raise PasswordError('Password should be more than 4 chars') 
        user = User.__users[username]
        user.__password = hashlib.sha256(new_password.encode()).hexdigest()

    @classmethod
    def from_json(cls) -> None:
        """
        Loads old users from a JSON file.
        """
        with open("users.json", 'r', encoding= 'utf-8') as f:
            json_data = json.loads(f.read())
            for u in json_data:
                cls(u['_username'], u['_User__password'], u['id'], u['phone_number'])
            # print(type(json_data))
            # print(json_data)

    @classmethod
    def to_json(cls) -> None:
        """
        Saves all users in a JSON file.
        """
        with open("users.json", 'w', encoding= 'utf-8') as f:
            # json_data ={}
            # for u in cls.__users.items():
            #     json_data[u[0]] = vars(u[1])
            json_data =[]
            for u in cls.__users.values():
                json_data.append(vars(u))
            json.dump(json_data, f, indent=4)

