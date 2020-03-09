import sys
import mysql.connector


def main(user):
    myDB = mysql.connector.connect(
        host="localhost",
        user="carricossauro",
        passwd="teste",
        db="db"
    )
    query = myDB.cursor()
    query.execute('SELECT * FROM UserData')
    data = query.fetchall()

    for i in data:
        for item in i:
            if user == item:
                print(user)


if __name__ == '__main__':
    try:
        main("carricossauro")
    except KeyboardInterrupt:
        print("Goodbye")
        sys.exit()
    except mysql.connector.Error as error:
        print("Failed accessing database:\n" + str(error))
        sys.exit()
