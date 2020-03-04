import sys
import json
import sqlite3
import movies
import re


def main():
    conn = movies.createConnection()
    cur = conn.cursor()
    file = open("movs.json")
    jfile = json.load(file)
    for key, item in jfile.items():
        print("Getting information on: " + item)
        movies.addMovie(cur, item)
    try:
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Failure closing database: " + str(error))
    else:
        print("Database closed. Movies saved.")
    file.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()