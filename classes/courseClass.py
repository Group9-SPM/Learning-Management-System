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


class Course(db.Model): 


    __tablename__ = 'course'

    courseID = db.Column(db.Integer, primary_key=True)
    courseName = db.Column(db.String(100), nullable=False)
    courseDesc = db.Column(db.String(500), nullable=False)
    courseDuration = db.Column(db.String(50), nullable=False)

    def __init__(self , courseID , courseName, CourseDesc, CourseDuration, PreReqCourses):
        self.__courseID = courseID
        self.__courseName = courseName
        self.__CourseDesc = CourseDesc
        self.__CourseDuration = CourseDuration
        self.__PreReqCourses = PreReqCourses

    def getCourseID(self):
        return self.__courseID
    
    def getCourseName(self):
        return self.__courseName

    def getCourseDesc(self):
        return self.__CourseDesc

    def getCourseDuration(self):
        return self.__CourseDuration
        
    def getPreReqCourses(self):
        return self.__PreReqCourses

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



@app.route("/courses")
def courses():
    course_list = Course.query.all()
    return jsonify(
        {
            "data": [course.to_dict()
                     for course in course_list]
        }
    ), 200

@app.route("/course/<string:courseName>")
def course_by_id(courseName):
    course = Course.query.filter_by(courseName=courseName).first()
    if course:
        return jsonify({
            "data": course.to_dict() 
        }), 200
    else:
        return jsonify({
            "message": "Course not found."
        }), 404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


