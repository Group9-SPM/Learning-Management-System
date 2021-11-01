from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from classesClass import Classes
from courseClass import Course

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
    lessonNum = db.Column(db.Integer, nullable=False)
    classID = db.Column(db.Integer, db.ForeignKey(Classes.classID), nullable=False)
    courseID = db.Column(db.Integer, db.ForeignKey(Course.courseID), nullable=False)
    lessonName = db.Column(db.String(100), nullable=False)
    lessonDesc = db.Column(db.String(500), nullable=False)

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

@app.route("/lesson/<int:classID>/<int:lessonNum>/<int:courseID>")
def lesson_by_num(classID, lessonNum, courseID):
    lessons = Lesson.query.filter_by(classID=classID, lessonNum=lessonNum, courseID=courseID).all()
    if lessons:
        return jsonify({
            "data": [lesson.to_dict()
                     for lesson in lessons]
        }), 200
    else:
        return jsonify({
            "message": "No lessons available yet."
        }), 201

@app.route("/lesson/<int:classID>/<int:courseID>")
def retrieve_all_lessons_by_class(classID, courseID):
    lessons = Lesson.query.filter_by(classID=classID, courseID=courseID).all()
    if lessons:
        return jsonify({
            "data": [lesson.to_dict()
                     for lesson in lessons]
        }), 200
    else:
        return jsonify({
            "message": "No lessons available yet."
        }), 201
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)

