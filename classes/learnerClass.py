from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from QuizClass import Quiz
from LessonClass import Lesson
from courseClass import Course
from employeeClass import Employee

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

class Learner: 

    __tablename__ = 'learner'

    #empID = db.Column(db.Integer, primary_key=True)
    badges = db.Column(db.String(300), nullable=False)
    learnerID = db.Column(db.Integer, db.ForeignKey('employee.empID'))
    
    def __init__(self , badges, empID = Employee.empID, quizGrade = Quiz.quizGrade, courseName = Course.CourseName):
        self.__empID = empID
        self.__badges = badges
        self.__quizGrade = quizGrade
        self.__courseName = courseName

    def getEmpID(self):
            return self.__empID
    
    def getQuizGrade(self):

            return self.__quizGrade

    def getEnrolledCourse(self):
            return self.__courseName
    
    #def getAppliedClass(self):
