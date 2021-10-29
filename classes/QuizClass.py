from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from lessonClass import Lesson

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)
CORS(app)

class Quiz(db.Model):
    __tablename__ = 'quiz'

    quizID = db.Column(db.Integer, primary_key=True)
    quizDuration = db.Column(db.String(20), nullable=False)
    passingCriteria = db.Column(db.String(5), nullable=False)
    quizType = db.Column(db.String(2), nullable=False)
    lessonID = db.Column(db.Integer, db.ForeignKey(Lesson.lessonID), nullable=False)


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


@app.route("/quiz")
def quizList():
    quizList = Quiz.query.all()
    return jsonify(
        {
            "data": [item.to_dict()
                     for item in quizList]
        }
    ), 200

@app.route('/quiz-create', methods=['POST'])
def create_quiz():
    data = request.get_json()
    print(data)
    item = Quiz(
        quizDuration=data['quizDuration'], passingCriteria=data['passingCriteria'],
        quizType=data['quizType'], lessonID=data['lessonID']
    )
    if ( request.get_json() is not None ): 
        try:
            db.session.add(item)
            db.session.commit()
            return jsonify(item.to_dict()), 201
        except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 500
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5014, debug=True)