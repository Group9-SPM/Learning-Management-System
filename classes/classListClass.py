from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from classesClass import Classes
from learnerClass import Learner

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

class ClassList(db.Model): 

    __tablename__ = 'classList'

    classID = db.Column(db.Integer, db.ForeignKey(Classes.classID), primary_key=True)
    learnerID = db.Column(db.Integer, db.ForeignKey(Learner.empID), nullable=False)
    progressPercentage = db.Column(db.Integer, nullable=False)
    finalQuizGrade = db.Column(db.String(5))

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



@app.route("/classList/<int:classID>")
def classList_by_class(classID):
    classlist = ClassList.query.filter_by(classID=classID)
    if classlist:
        return jsonify({
            "data": [learner.to_dict()
                     for learner in classlist]
        }), 200
    else:
        return jsonify({
            "message": "No learners assigned."
        }), 404

@app.route("/classList/learner/<int:learnerID>")
def classList_by_learner(learnerID):
    assignedClasses = ClassList.query.filter_by(learnerID=learnerID)
    if assignedClasses:
        return jsonify({
            "data": [classes.to_dict()
                     for classes in assignedClasses]
        }), 200
    else:
        return jsonify({
            "message": "No assigned classes."
        }), 404


@app.route("/classList", methods=['POST'])
def assign_learner():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('learnerID', 'classID')):
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

    # (4): Create assignment record in ClassList
    assignment = ClassList(
        classID=data['classID'], learnerID=data['learnerID'],
        progressPercentage=0
    )

    # (5): Commit to DB
    try:
        db.session.add(assignment)
        db.session.commit()
        return jsonify({
            "data": assignment.to_dict(),
            "message": "Learner assigned successfully"
        }), 201
    except Exception as e:
        return jsonify({
            "message": "Unable to commit to database. " + str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5012, debug=True)


