import sqlite3
import os

selectAll = 'SELECT * FROM Contactos'
selectCol1 = 'SELECT '
selectCol2 = ' FROM '
where = ' WHERE '
ins = ' INSERT INTO '
insParam = ' (Nome, Numero) VALUES '


def normalize(row):
    print("------------------------------")
    for i in row:
        if isinstance(i, int):
            print("Numero: " + str(i))
        else:
            print("Nome: " + str(i))
    print("------------------------------")


def createConnection(name):
    if os.path.isfile(name):
        print("Accessing database")
    else:
        print("Creating database")
    conn = None
    cur = None
    try:
        conn = sqlite3.connect(name)
        cur = conn.cursor()
    except sqlite3.Error as error:
        print("Attempt to access database failed: " + str(error))
    else:
        print("--------------- Database accessed -------------------------------------")
    return cur, conn


def closeConnection(connection):
    try:
        connection.commit()
        connection.close()
    except sqlite3.Error as error:
        print("Error closing database: " + str(error))
    else:
        print("--------------- Database closed ---------------------------------------\n")
    return None


def select(conn, argument, wheres='', table='Contactos'):
    if wheres == '':
        selectCols = selectCol1 + argument + selectCol2 + table.title()
    else:
        selectCols = selectCol1 + argument + selectCol2 + table.title() + where + wheres

    try:
        conn.execute(selectCols)
    except sqlite3.Error as error:
        print("Attempt to access " + argument + " has failed: [" + str(error) + "]")
    else:
        rows = conn.fetchall()
        for row in rows:
            normalize(row)
    return None


def insert(conn, name, number, table='Contactos'):
    insertCommand = ins + table.title() + insParam + '(' + name + ', ' + number + ')'
    try:
        conn.execute(insertCommand)
    except sqlite3.Error as error:
        print("Unable to insert values " + name + " in table " + table.title() + ': ' + str(error))
    else:
        print("Values " + name + ' and ' + str(number) + " successfully inserted in table " + table.title())