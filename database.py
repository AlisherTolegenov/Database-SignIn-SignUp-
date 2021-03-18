import shelve

class HelloUser:
    db = shelve.open('database')
    def __init__(self):
        self.starting()

    @staticmethod
    def starting():
        print('1.Sign In')
        print('2.Sign Up')
        while True:
            answer = input('Select function: ')
            if answer == '1':
                SignIn()
                break
            if answer == '2':
                SignUp()
                break
            else:
                print('Incorrectly entered function number')
                continue

class SignUp:
    def __init__(self):
        self.registration_login()

    @staticmethod
    def registration_login():
        while True:
            flag = False
            login = input('Enter your desired username: ')
            for key in HelloUser.db:
                if login == HelloUser.db[key].login:
                    print('A user with the given name already exists, please choose a different username')
                    flag = True
            if flag:
                continue
            else:
                print('You have successfully created a login')
                SignUp.registration_password(login)
            break

    @staticmethod
    def registration_password(login):
        while True:
            password = input('Enter the desired password: ')
            if len(password) < 8:
                print('Password must contain at least 8 letters')
                continue
            else:
                print('You have successfully registered!')
                user = Person(login, password)
                length = len(HelloUser.db)+1
                key = 'd' + str(length)
                HelloUser.db[key] = user
                HelloUser()
                break

class Person:
    def __init__(self, login, password):
        self.login = login
        self.password = password


class SignIn:
    def __init__(self):
        self.sign_in_login()

    @staticmethod
    def sign_in_login():
        while True:
            flag = True
            login = input('Enter username: ')
            for key in HelloUser.db:
                if HelloUser.db[key].login == login:
                    flag = False
                    SignIn.sign_in_password(login)
                    break
            if flag:
                print('User with this login does not exist')
                continue
            break

    @staticmethod
    def sign_in_password(login):
        while True:
            flag = True
            password = input('Enter password:')
            for key in HelloUser.db:
                if HelloUser.db[key].login == login and HelloUser.db[key].password == password:
                    print('You have successfully signed in to your account')
                    HelloUser.db.close()
                    flag = False
                    break
            if flag:
                print('Your password is not correct, please try again')
                SignIn.sign_in_password(login)
            break

if __name__ == '__main__':
    HelloUser()
