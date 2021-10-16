from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

import requests

import os, sys
from os import environ

#from invokes import invoke_http
import json

import urllib.request
import mysql.connector
from datetime import date, datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

class signuplist(db.Model):
    __tablename__ = 'signuplist'

    learnerID = db.Column(db.Integer, primary_key=True)
    classID = db.Column(db.Integer, primary_key=True)
    courseStatus = db.Column(db.String(300), nullable=False)


    def __init__(self, learnerID, classID,courseStatus):
        self.learnerID = learnerID
        self.classID = classID
        self.courseStatus = courseStatus

@app.route("/signuplist")
def getAll():
    signuplists = signuplist.query.all()
    if len(signuplists):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "signuplist": [signup.json() for signup in signuplists]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no signup."
        }
    ), 404
