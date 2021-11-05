from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from courseClass import Course

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

class Prerequisite(db.Model):
    __tablename__ = 'prerequisite'

    courseID = db.Column(db.Integer, db.ForeignKey(Course.courseID) ,primary_key=True)
    prerequisiteID = db.Column(db.Integer, primary_key=True)

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

@app.route("/prerequisite")
def prerequisite():
    prerequisite = Prerequisite.query.all()
    return jsonify(
        {
            "data": [prereq.to_dict()
                     for prereq in prerequisite]
        }
    ), 200


@app.route("/prerequisite/<int:courseID>")
def prerequisite_by_courseID(courseID):
    prerequisite = Prerequisite.query.filter_by(courseID=courseID).first()
    if prerequisite:
        return jsonify({
            "data": prerequisite.to_dict() 
        }), 200
    else:
        return jsonify({
            "message": "Error getting prerequisite course."
        }), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=True)