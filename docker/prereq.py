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
#app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

class Prerequisite(db.Model):
    __tablename__ = 'prerequisite'

    courseID = db.Column(db.Integer, primary_key=True)
    prerequisiteID = db.Column(db.Integer, primary_key=True)

    def __init__(self, courseID, prerequisiteID):
        self.courseID = courseID
        self.prerequisiteID = prerequisiteID



    def json(self):
        return {"courseID": self.courseID, "prerequisiteID": self.prerequisiteID}


@app.route("/prerequisite")
def getAllPrerequisite():
    prerequisitelist = Prerequisite.query.all()
    if len(prerequisitelist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "prerequisite course": [prerequisite.json() for prerequisite in prerequisitelist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no prerequisite course."
        }
    ), 404