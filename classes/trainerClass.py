from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

from courseClass import Course
from employeeClass import Employee

class Trainer:
    def __init__(self,courseName =  Course.courseName , trainerID = Employee.empID):
        self.__courseName= courseName
        self.__trainerID = trainerID

    #def getClass(self):
    def getEmpID(self):
        return self.__trainerID


    def getAssignedCourse(self, courseName):
        return self.__courseName
