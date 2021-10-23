from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from courseClass import Course
from employeeClass import Employee

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

class Classes(db.Model): 
    
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
    courseID = db.Column(db.Integer, db.ForeignKey(Course.courseID))
    trainerID = db.Column(db.Integer, db.ForeignKey(Employee.empID))
    
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
def classes():
    class_list = Classes.query.all()
    return jsonify(
        {
            "data": [classes.to_dict()
                     for classes in class_list]
        }
    ), 200

@app.route("/classes/<int:courseID>")
def class_by_courseID(courseID):
    classCourseID = Classes.query.filter_by(courseID=courseID).first()
    if classCourseID:
        return jsonify({
           
            "data": [indivClass.json() for indivClass in classCourseID]
        }), 200
    else:
        return jsonify({
            "message": "No available classes."
        }), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)