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

class Quiz():
     
    def __init__(self, quizID, passingCriteria, quizType):
        self.__quizID = quizID
        self.__passingCriteria = passingCriteria
        self.__quizType = quizType

    def getQuizID(self):
        return self.__quizID
    def getQuizDuration(self):
        return self.__quizDuration
    def getPassingCriteria(self):
        return self.__passingCriteria
    def getQuizType(self):
        return self.__quizType
