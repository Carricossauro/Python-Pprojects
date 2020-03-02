import login
import operations
import os
import time
import sys


def main():
    try:
        logging = True
        while logging:
            logging = login.login()

        os.system('clear')
        operations.instruction()
        time.sleep(0.6)
        os.system('clear')

        print("--------------- This was fun! Come back anytime! ----------------------")
        time.sleep(0.4)

    except KeyboardInterrupt:
        print("\n", end='')
        sys.exit()


if __name__ == "__main__":
    main()