import database
import os


def instruction():
    connectionAtributes = None
    op = input("What operation do you wish to perform? ")
    args = op.split(' ')

    db = False
    if args[0] == 'exit':
        return None

    if len(args) >= 2:
        name = args[1]
        if args[0].lower() == "access":
            connectionAtributes = database.createConnection(name)
            accessDB(connectionAtributes[0])
            db = True
        elif args[0].lower() == 'remove' or args[0].lower() == 'delete':
            if os.path.exists(args[1]):
                os.remove(args[1])
                print("File successfully deleted")
            else:
                print("The File " + args[1] + " does not exist.")

    if db:
        database.closeConnection(connectionAtributes[1])
    return None


def accessDB(conn):
    while True:
        op = input("Operation: ")

        if op == "exit":
            break

        else:
            args = op.split(' ')
            if args[0].lower() == "view":

                if len(args) >= 4:
                    database.select(conn, args[1], args[2], args[3])
                elif len(args) == 3:
                    database.select(conn, args[1], args[2])
                else:
                    try:
                        database.select(conn, args[1])
                    except IndexError:
                        print("'View' command requires more arguments")

            elif args[0].lower() == 'insert':

                if len(args) == 4:
                    database.insert(conn, args[1], args[2], args[3])
                else:
                    try:
                        database.insert(conn, args[1], args[2])
                    except IndexError:
                        print("'Insert' command requires more arguments")


if __name__ == "__main__":
    instruction()
