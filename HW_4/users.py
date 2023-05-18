import uuid

class UsernameError(ValueError):
    pass

class PasswordError(ValueError):
    pass

class EmptyError(ValueError):
    pass

class User:

    __users = {}
    def __init__(self, username, password, phone_number = None) -> None:
        if len(password) < 4:
            raise PasswordError('Password should be more than 4 chars') 
        self.username = username
        self.id = uuid.uuid4()
        self.__password = password 
        self.phone_number = phone_number
        type(self).__users[self.username] = self

    # @username.setter
    # def username(self, username: str):
    #     for user in User.__users.keys():
    #         if username == user:
    #             raise UsernameError('This username was taken.')
    #     self._usename


    def __str__(self) -> str:
        return f'Username: {self.username}\nPhone Number: {self.phone_number}\nID: {self.id}'

    def __repr__(self) -> str:
        return f'({self.username}, {self.__password}, {self.phone_number}, {self.id})'

    def users():
        return User.__users
    
    @classmethod
    def sign_up(cls, username, password, phone_number):
        if username == '' or password == '':
            raise EmptyError('Userame or Password cant be empty!')
        if not phone_number:
            phone_number = None
        elif not phone_number.isnumeric() or len(phone_number) != 11:
            raise ValueError('Invalid phone number!')
        cls(username, password, phone_number)

    @staticmethod
    def validation(username, password):
        return User.__users[username].__password == password

    @classmethod
    def profile(cls, username):
        return cls.__users[username]
    
    @classmethod
    def edit_profile(cls, old_username, new_username, new_phone_number):
        user = cls.__users[old_username] 
        for userr in User.__users.keys():
            if new_username == userr:
                raise UsernameError('This username was taken.')
        if new_username == '':
            raise EmptyError('Userame cant be empty!')
        # if not new_phone_number:
        #     pass
        if not new_phone_number.isnumeric() or len(new_phone_number) != 11:
            raise ValueError('Invalid phone number!')
        
        user.username = new_username
        user.phone_number = new_phone_number
        cls.__users[new_username] = cls.__users[old_username] 
        del cls.__users[old_username] 

    @staticmethod
    def edit_password(username: str, new_password: str):
        user = User.__users[username]
        if len(new_password) < 4:
            raise PasswordError('Password should be more than 4 chars') 
        user.__password = new_password


        

# getter setter
# docstr









# import random

# self.id = f"{random.randint(0, 9):04}" ## bayad yekta bashe                     ### baze random ###
#         flag= 1
#         while flag:
#             repeat = 0
#             flag = 0
#             for user in User.__users:
#                 # print(self.id , self.username)
#                 # s=0
#                 while self.id == user.id: #and repeat < 10: # age az birun karbar avordim - jayi save kardim $##### random bashe ehtemalan tu 1000 tamum nemishe
#                     self.id = f"{random.randint(0, 9):04}" #mitune be tatibam bashe
#                     # print(self.id, user.id)
#                     # print(s)
#                     # s+=1
#                     flag = 1
#                 repeat += 1 #in doros nist chon shyad ye id yekrari ke gablan chek shode bud bede va user tekrari ro emtehankone
#                 if repeat == 10: 
#                     raise MemoryError('Capacitance is full') 
