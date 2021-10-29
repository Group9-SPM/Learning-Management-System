from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from classesClass import Classes

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

@app.route("/lesson/<int:classID>/<int:lessonNum>")
def lesson_by_num(classID, lessonNum):
    lesson = Lesson.query.filter_by(classID=classID, lessonNum=lessonNum).first()
    if lesson:
        return jsonify({
            "data": lesson.to_dict() 
        }), 200
    else:
        return jsonify({
            "message": "Lesson not found."
        }), 404
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)