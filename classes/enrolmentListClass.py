from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


from classesClass import Classes
from learnerClass import Learner
from courseClass import Course

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

class EnrolmentList(db.Model): 

    __tablename__ = 'enrolmentList'

    classID = db.Column(db.Integer, db.ForeignKey(Classes.classID), primary_key=True)
    learnerID = db.Column(db.Integer, db.ForeignKey(Learner.empID), nullable=False)
    courseID = db.Column(db.Integer, db.ForeignKey(Course.courseID), nullable=False)
    enrolmentStatus = db.Column(db.String(100), nullable=False)

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


@app.route("/enrolmentList")
def enrolmentList():
    enrolments_list = EnrolmentList.query.all()
    return jsonify(
        {
            "data": [enrolment.to_dict()
                     for enrolment in enrolments_list]
        }
    ), 200

@app.route("/enrolmentList/<int:learnerID>")
def enrolments_by_learner(learnerID):
    enrolments = EnrolmentList.query.filter_by(learnerID=learnerID)
    if enrolments:
        return jsonify({
            "data": [enrolment.to_dict()
                     for enrolment in enrolments]
        }), 200
    else:
        return jsonify({
            "message": "No enrolments found."
        }), 404

@app.route("/enrolmentList", methods=['POST'])
def create_enrolment():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('learnerID', 'classID', 'courseID')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # (1): Validate class
    classes = Classes.query.filter_by(classID=data['classID']).first()
    if not classes:
        return jsonify({
            "message": "Class is not valid."
        }), 500

    # (2): Validate learner
    learner = Learner.query.filter_by(empID=data['learnerID']).first()
    if not learner:
        return jsonify({
            "message": "Learner is not valid."
        }), 500

    course = Course.query.filter_by(courseID=data['courseID']).first()
    if not course:
        return jsonify({
            "message": "Course is not valid."
        }), 500

    # (4): Create enrolment record
    enrolment = EnrolmentList(
        classID=data['classID'], learnerID=data['learnerID'],
         courseID=data['courseID'], enrolmentStatus="Pending"
    )

    # (5): Commit to DB
    try:
        db.session.add(enrolment)
        db.session.commit()
        return jsonify(enrolment.to_dict()), 201
    except Exception as e:
        return jsonify({
            "message": "Unable to commit to database. " + str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=True)


