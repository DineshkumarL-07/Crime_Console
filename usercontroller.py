import re
from model.usermodel import UserModel
class User:
    def signup(self):
        EMAIL_RE = r'^[a-z0-9\.\_]{1,}@\w+.\w+'
        password = "crimeDATA"
        passcode = input("Enter your passcode to sign Up:")
        if passcode == password:
            name = input("Enter an user name:")
            email = input("Enter an Email Id:")
            if re.search(EMAIL_RE, email):
                pwd = input("Enter an password:")
                renter = input("Re-enter the password to confirm:")
                while (pwd != renter):
                    print("Password and Confirm Password doesn't match. Enter correct one")
                    renter = input("Re-enter the password to confirm:")
                if pwd == renter:
                    temp = UserModel.signup(name, pwd, email)
                    if temp:
                        print(f"Sign Up successfully completed,{name}")
                    else:
                        print("Invalid Sign Up")
            else:
                print("Use an Valid Email Id")
        else:
            print("Invalid Passcode for Sign up!")
    def login(self):
        username = input("Enter an Email Id or Username: ")
        pwd = input("Enter an Password: ")
        user = UserModel()
        ans = user.login(username)
        if ans[0][0] == pwd:
            print(f"Login successfully completed,{ans[0][1]}")
            print("\t\t\t Welcome Sir! \t\t\t")
            return True
        elif ans[0][0] != pwd:
            print("Invalid Password")
            return False
        else:
            print("Invalid Email ID. Please try again or Sign Up")
            return False
