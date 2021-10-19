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


class Employee: 

    __tablename__ = 'employee'

    empID = db.Column(db.Integer, primary_key=True)
    empName = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    roleType = db.Column(db.String(1), nullable=False)


    def __init__(self ,empID, employeeName , Department, Username, RoleType):
        self.__empID = empID
        self.__employeeName = employeeName
        self.__Department = Department
        self.__Username = Username
        self.__RoleType = RoleType 

    def getEmpID(self, empID):
        return self.__empID
    
    def getName(self, employeeName):
        return self.__employeeName

    def getDepartment(self, Department):
        return self.__Department

    def getRoleType(self, RoleType):
        return self.__RoleType

    def getUsername(self,Username):
        return self.__Username

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


@app.route("/employee")
def employee():
    employee_list = Employee.query.all()
    return jsonify(
        {
            "data": [employee.to_dict()
                     for employee in employee_list]
        }
    ), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
