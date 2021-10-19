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


from LessonClass import Lesson
from courseClass import Course

class Trainer:
    def __init__(self,courseName =  Course.courseName ):
        self.__courseName= courseName

    #def getClass(self):


    def getAssignedCourse(self, courseName):
        return self.__courseName
