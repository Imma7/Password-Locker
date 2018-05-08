import sys
import random
import string

from user import User
from credential import Credential

def passlen(l):
    _all = string.ascii_letters+ string.punctuation+string.digits
    return "".join(random.sample(_all,l))

def sign_in():
    username = input("Select preferred user: ")
    password1 = input("Enter Password: ")
    password2 = input("Enter your password again: ")

    if password1 == password2:
        User(username, password1)
        return True
    else:
        print("Password does not match")
        sign_in()

def start():
    print("Start Here")
    options = True
    while options:
        inp = int(input("1. Sign In \n2. Leave"))
        if inp == 1:
            return sign_in()
            options = False
        elif inp == 2:
            print("You are Signing Out")
            sys.exit(5)
        else:
            print("Select 1 or 2")


def main():
    print("Welcome to Password Locker")
    registered = start()
    if registered:
        registering = True
        while registering:
            selections = int(input("1. New Account\n2. View Accounts\n3. Delete Account\n4. Log Out"))
            
            #Create Account
            if selections == 1:
                    account = input("Enter account name: ")
                    name = input("Enter your username: ")
                    lenpass = int(input("Enter your password length: "))
                    password = passlen(lenpass)
                    Credential(account, name, password)
            #View Account
            elif selections == 2:
                Credential.view()

#             #Delete Account
            elif selections == 3:
                Credential.delete(input("which account do you wish to delete ?"))

#             elif selections == 4:
#                 print("You are exiting")
#                 registering = False



# if __name__ == '__main__':
#     main()