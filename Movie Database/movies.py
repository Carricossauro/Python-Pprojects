import sqlite3
import random
import sys
import os
from imdbAPI import getInfo

insert = 'INSERT INTO Movies (Name, Runtime, Released) VALUES '
select = 'SELECT * FROM Movies'
remove = 'DELETE FROM Movies WHERE Name="'


def main():
    try:
        connection = createConnection()
        cursor = connection.cursor()
        while 1:
            operation = input("Operation: ").lower()
            if operation == 'add':
                movie = input("Movie name: ")
                addMovie(cursor, movie)
            elif operation == 'check':
                os.system('clear')
                checkMovies(cursor)
            elif operation == 'remove':
                removeMovie(cursor)
            elif operation == 'random':
                randomMovie(cursor)
            elif operation == 'exit':
                break
            else:
                print("Please give a working command")
        connection.commit()
        connection.close()
        sys.exit()
    except KeyboardInterrupt:
        print()
        sys.exit()
    except sqlite3.Error as error:
        print("Program failed : " + str(error))


def addMovie(cursor, movie):
    try:
        cursor.execute(insert + getInfo(movie))
    except sqlite3.Error as error:
        print("Attempt to add movie has failed: " + str(error))
    except Exception as error:
        print("Attempt to add movie has failed: " + str(error))
    else:
        print("Movie successfully added")


def addMovieManual(cursor):
    movie = input("Movie Information (Name, Runtime, Release Date): ")
    try:
        cursor.execute(insert + movie)
    except sqlite3.Error as error:
        print("Attempt to add movie has failed: " + str(error))
    except Exception as error:
        print("Attempt to add movie has failed: " + str(error))
    else:
        print("Movie successfully added")


def createConnection():
    con = None
    try:
        con = sqlite3.connect('movies')
    except sqlite3.Error as error:
        print("Connection failed: " + str(error))
    return con


def checkMovies(cursor):
    try:
        cursor.execute(select)
        rows = cursor.fetchall()
    except sqlite3.Error as error:
        print("Attempt to select failed: " + str(error))
    else:
        for row in rows:
            getRow(row)


def getRow(row):
    print("-----------------------------")
    print("Name: " + str(row[0]))
    print("Runtime: " + str(row[1]) + " minutes")
    print("Released on: " + str(row[2]))
    print("-----------------------------")


def removeMovie(cursor):
    name = input("Movie name: ").lower().title()
    try:
        cursor.execute(remove + name + '"')
    except sqlite3.Error as error:
        print("Error deleting movie from table: " + str(error))
    else:
        print("Movie successfully removed")


def randomMovie(cursor):
    cursor.execute(select)
    movies = cursor.fetchall()
    mov = random.choice(movies)
    getRow(mov)


if __name__ == '__main__':
    main()
