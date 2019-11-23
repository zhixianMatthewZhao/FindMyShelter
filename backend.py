import flask

import requests
import json
import string
import hashlib
import random

import pymongo

from jsonStoreControllerUser.controller import jsonStoreController

app = flask.Flask(__name__)

userid = 0
@app.route('/',methods = ['GET'])
def rootPage():
    return flask.render_template('index.html')

@app.route('/login',methods = ['GET','POST'])
def login():
    if flask.requests.method == 'GET':
        return flask.render_template('login.html')
    if flask.requests.method == 'POST':
        userdata = {
            'usertype':flask.request.form['usertype'],
            'username':flask.request.form['username'],
            'password':hashlib.sha512(str.encode(flask.request.form['password'])).hexdigest()
        }
        control = jsonStoreController()
        ans = control.getUser()
        res = {
            'usertype':ans['usertype'],
            'loginstatus':ans['password']==userdata['password']
        }
        return flask.jsonify(res)



@app.route('/register',methods = ['GET','POST'])
def register():
    if flask.request.method == 'GET':
        return flask.render_template('register.html')
    if flask.request.method == 'POST':
        userid += 1
        controller = jsonStoreController()
        payload = {
            'usertype':flask.request.form['usertype'],
            'username':flask.request.form['username'],
            'password':hashlib.sha512(str.encode(flask.request.form['username'])).hexdigest
        }
    controller.newUser(payload,userid)

app.run(host='0.0.0.0',port=5000,debug=True)