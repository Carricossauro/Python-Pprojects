#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from datetime import date

db = create_engine('mysql://carricossauro:admin@localhost/PythonAPI')
app = Flask(__name__)
api = Api(app)
con = db.connect()
app.config["DEBUG"] = True


@app.route('/userids', methods=['GET'])
def getIDs():
    query = con.execute("SELECT id FROM PythonTable")
    list = []
    for i in query.cursor.fetchall():
        list.append(i[0])
    return jsonify(list)


@app.route('/users', methods=['GET'])
def getUsers():
    query = con.execute("SELECT username, email, id FROM PythonTable")
    return jsonify([dict(zip(tuple(query.keys()), i)) for i in query.cursor])


@app.route('/users/find', methods=['GET'])
def findUser():
    if 'username' in request.args:
        username = request.args['username']
    else:
        return "Error: No username field provided. Please specify a username."
    query = con.execute('SELECT username FROM PythonTable WHERE username="' + username + '"')
    return jsonify([dict(zip(tuple(query.keys()), i)) for i in query.cursor])


@app.route('/users/add', methods=['GET', 'POST'])
def addUser():
    resp = 400
    if 'username' in request.args and 'password' in request.args and 'email' in request.args:
        try:
            user = request.args['username']
            passwd = request.args['password']
            email = request.args['email']
            todaysDate = date.today().strftime("%Y-%m-%d")
            con.execute("INSERT INTO PythonTable "
                        "(Username, password, email, CreationDay) VALUES "
                        "('{}', '{}', '{}','{}')".format(user, passwd, email, todaysDate))
            resp = 201
        except Exception as error:
            print(error)
            resp = 409

    return jsonify(resp)


app.run()
