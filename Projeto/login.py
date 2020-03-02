import time
from getpass import getpass


def login():
    user = input("Username: ")
    password = getpass("Password: ")
    if user == "carricossauro" and password == "qwerty":
        time.sleep(0.4)
        print("--------------- Authentication Successful -----------------------------")
        time.sleep(0.4)
        return False
    else:
        time.sleep(0.4)
        print("--------------- Authentication Failed. Please Try Again ---------------")
        time.sleep(0.4)
        return True


if __name__ == "__main__":
    login()
