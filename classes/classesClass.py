from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from courseClass import Course
from trainerClass import Trainer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

class Classes: 
    
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
    courseID = db.Column(db.Integer, db.ForeignKey('course.courseID'))
    trainerID = db.Column(db.Integer, db.ForeignKey('employee.empID'))
    

    def __init__(self , ClassID , StartDate, EndDate, ClassSize, StartTime, EndTime, maxSlots, minSlots, regStartDate, regEndDate, trainerID = Trainer.trainerID, courseID = Course.CourseID):
        self.__ClassID = ClassID
        self.__StartDate = StartDate
        self.__EndDate = EndDate
        self.__ClassSize = ClassSize
        self.__StartTime = StartTime
        self.__EndTime = EndTime
        self.__maxSlots = maxSlots
        self.__minSlots = minSlots
        self.__regStartDate = regStartDate
        self.__regEndDate = regEndDate
        self.__courseID = courseID
        self.__trainerID = trainerID

    def getClassID(self):
        return self.__ClassID
    
    def getStartDate(self):
        return self.__StartDate

    def getEndDate(self):
        return self.__EndDate

    def getClassSize(self):
        return self.__ClassSize
        
    def getStartTime(self):
        return self.__StartTime

    def getEndTime(self):
        return self.__EndTime
    
    def getmaxSlots(self):
        return self.__maxSlots

    def getminSlots(self):
        return self.__minSlots

    def getregStartDate(self):
        return self.__regStartDate
        
    def getregEndDate(self):
        return self.__regStartDate

    def getCourseID(self):
        return self.__courseID

    def getTrainerID(self):
        return self.__trainerID

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result



@app.route("/classes")
def classess():
    class_list = Classes.query.all()
    return jsonify(
        {
            "data": [classes.to_dict()
                     for classes in class_list]
        }
    ), 200

