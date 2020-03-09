#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

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


app.run()
