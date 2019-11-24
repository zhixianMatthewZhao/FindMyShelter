import flask

import requests
import json
import string
import hashlib
import random

from jsonStoreControllerUser.controller import jsonStoreController
from mysqlcontrollerCompanyUser.companyController import companyController

app = flask.Flask(__name__)


userid = 0

@app.route('/',methods = ['GET'])
def rootPage():
    return flask.render_template('landing.html')

@app.route('/login', methods = ['POST'])
def login():
    userdata = {
        "usertype": flask.request.form['usertype'],
        "username": flask.request.form['username'],
        "password": hashlib.sha512(str.encode(flask.request.form['password'])).hexdigest()
    }
    control = jsonStoreController()
    ans = control.getPassword(userdata['username'])
   
    res = {
        'usertype':ans[1],
        'loginstatus':str(ans[0]==userdata["password"]),
        'username':userdata['username']
    }
    return flask.jsonify(res)

@app.route('/register',methods = ['POST'])
def register():
    global userid
    if flask.request.method == 'POST':
        userid += 1
        controller = jsonStoreController()
        payload = {
            'usertype':flask.request.form['usertype'],
            'username':flask.request.form['username'],
            'password':hashlib.sha512(str.encode(flask.request.form['password'])).hexdigest(),
            'details':'{ }'
        }
        if payload['usertype'] == 'user':
            controller = jsonStoreController()
            payload['shelter']=' '
            controller.newUser(payload)
        else:
            controller = companyController()
            controller.newCompanyUser(payload)
        return ' '

@app.route('/dashboard',methods=['GET'])
def companyDashboard():
    return flask.render_template('organization.html', **{
        'username' : 'urgaymom',
        'phone': 'your gay dad',
        'address': 'your gay brother',
        'data':json.dumps({
            'urparents':'huge pussies'
        })
    })

app.run(host='0.0.0.0',port=5000,debug=True)