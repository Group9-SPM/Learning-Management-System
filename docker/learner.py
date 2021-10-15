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

class Learner(db.Model):
    __tablename__ = 'learner'

    empID = db.Column(db.Integer, primary_key=True)
    badges = db.Column(db.String(300), nullable=False)


    def __init__(self, empID, badges):
        self.empID = empID
        self.badges = badges


@app.route("/learner")
def get_all():
    learnerlist = Learner.query.all()
    if len(learnerlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "learner": [learner.json() for learner in learnerlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no learner."
        }
    ), 404