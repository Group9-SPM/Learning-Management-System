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
    __tablename__ = 'course'

    courseID = db.Column(db.Integer, primary_key=True)
    courseName = db.Column(db.String(100), nullable=False)
    courseDesc = db.Column(db.String(500), nullable=False)
    courseDuration = db.Column(db.String(50), nullable=False)

    def __init__(self, courseID, courseName, courseDesc, courseDuration):
        self.courseID = courseID
        self.courseName = courseName
        self.courseDesc = courseDesc
        self.courseDuration = courseDuration


    def json(self):
        return {"courseID": self.courseID, "courseName": self.courseName, "courseDesc": self.courseDesc, "courseDuration": self.courseDuration}

@app.route("/courses")
def get_all():
    courselist = course.query.all()
    if len(courselist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course": [course.json() for course in courselist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no course."
        }
    ), 404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True)