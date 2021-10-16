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

class course(db.Model):
    __tablename__ = 'classes'

    classID = db.Column(db.Integer, primary_key=True)
    startDate = db.Column(db.DateTime, nullable=False)
    endDate = db.Column(db.DateTime, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    startTime = db.Column(db.String(20), nullable=False)
    endTime = db.Column(db.String(20), nullable=False)
    minSlot = db.Column(db.Integer, nullable=False)
    maxSlot = db.Column(db.Integer, nullable=False)
    regStartDate = db.Column(db.DateTime, nullable=False)
    regEndDate = db.Column(db.DateTime, nullable=False)
    courseID = db.Column(db.Integer, primary_key=True)
    trainerID = db.Column(db.Integer)

    def __init__(self , classID , startDate, endDate, size, startTime, endTime, maxSlots, minSlots, regStartDate, regEndDate, courseID, trainerID):
        self.__classID = classID
        self.__startDate = startDate
        self.__endDate = endDate
        self.__size = size
        self.__startTime = startTime
        self.__endTime = endTime
        self.__maxSlots = maxSlots
        self.__minSlots = minSlots
        self.__regStartDate = regStartDate
        self.__regEndDate = regEndDate
        self.__courseID = courseID
        self.__trainerID = trainerID

    def json(self):
        return {"classID": self.classID, "startDate": self.startDate, "endDate": self.endDate, "size": self.size, "startTime": self.startTime, "endTime": self.endTime, 
        "maxSlots": self.maxSlots, "minSlots": self.minSlots, "regStartDate": self.regStartDate, "regEndDate": self.regEndDate, "courseID": self.courseID, "trainerID": self.trainerID}

@app.route("/classes")
def get_all():
    classlist = classes.query.all()
    if len(classlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "class": [classes.json() for classes in classlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no classes."
        }
    ), 404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True)