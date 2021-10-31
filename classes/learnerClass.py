from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from employeeClass import Employee


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

class Learner(Employee): 

    __tablename__ = 'learner'

    badges = db.Column(db.String(300))
    empID = db.Column(db.Integer, db.ForeignKey(Employee.empID), primary_key=True)
    
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
        

@app.route("/learner")
def learner():
    learner_list = Learner.query.all()
    return jsonify(
        {
            "data": [learner.to_dict()
                     for learner in learner_list]
        }
    ), 200
    

@app.route("/learner/<int:empID>")
def learner_by_empID(empID):
    learner = Learner.query.filter_by(empID=empID).first()
    if learner:
        return jsonify({
            "data": learner.to_dict() 
        }), 200
    else:
        return jsonify({
            "message": "No learner with that empID."
        }), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)
