from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from quizClass import Quiz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

class Lesson(db.Model):
    __tablename__ = 'lesson'

    lessonID = db.Column(db.Integer, primary_key=True)
    classID = db.Column(db.Integer, db.ForeignKey('class.classID'), nullable=False)
    lessonName = db.Column(db.String(100), nullable=False)
    lessonDesc = db.Column(db.String(500), nullable=False)

    def __init__(self, classID, lessonID, lessonName, lessonDesc):
        self.lessonID = lessonID
        self.classID = classID
        self.lessonName = lessonName
        self.lessonDesc = lessonDesc

    def getLessonName(self):
        return self.lessonName

    def getDocuments():
        return "d.getCourseMaterials()"

    def getQuiz():
        q = Quiz()
        return q.getQuizID()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True)