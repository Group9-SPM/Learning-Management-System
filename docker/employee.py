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

class Employee(db.Model):
    __tablename__ = 'employee'

    empID = db.Column(db.Integer, primary_key=True)
    empName = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    roleType = db.Column(db.String(1), nullable=False)

    def __init__(self, empID, empName, department, username, roleType):
        self.empID = empID
        self.empName = empName
        self.department = department
        self.username = username
        self.roleType = roleType

    def json(self):
        return {"empID": self.empID, "empName": self.empName, "department": self.department, "username": self.username,"roleType": self.roleType}

@app.route("/employee")
def get_all():
    employeelist = Employee.query.all()
    if len(employeelist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "employee": [employee.json() for employee in employeelist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no employee."
        }
    ), 404


@app.route("/employee/<string:roleType>")
def getAllEmployeeByRole(roleType):
    employeelist = Employee.query.filter_by(roleType = roleType).all()
    if len(employeelist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "employee": [employee.json() for employee in employeelist]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "employee not found."
        }
    ), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True)