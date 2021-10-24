from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_cors.core import LOG
from flask_sqlalchemy import SQLAlchemy

from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

class Quiz(db.Model):
    __tablename__ = 'quiz'

    quizID = db.Column(db.Integer, primary_key=True)
    quizDuration = db.Column(db.String(20), nullable=False)
    passingCriteria = db.Column(db.String(5), nullable=False)
    quizType = db.Column(db.String(2), nullable=False)
    lessonID = db.Column(db.Integer, nullable=False)

    def __init__(self, quizID, quizDuration, passingCriteria, quizType, lessonID):
        self.quizID = quizID
        self.quizDuration = quizDuration
        self.passingCriteria = passingCriteria
        self.quizType = quizType
        self.lessonID = lessonID
class Questions(db.Model):
    __tablename__ = 'quizQuestions'

    quizID = db.Column(db.Integer, primary_key=True)
    qnNo = db.Column(db.Integer, nullable=False)
    question = db.Column(db.String(300), nullable=False)
    options = db.Column(db.String(100), nullable=False)
    answer = db.Column(db.String(50), nullable=False)

    def __init__(self, quizID, qnNo, question, options, answer):
        self.quizID = quizID
        self.qnNo = qnNo
        self.question = question
        self.options = options
        self.answer = answer

db.create_all()

@app.route("/quiz")
def get_all():
    quizlist = Quiz.query.all()
    if len(quizlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "quiz": [quiz.json() for quiz in quizlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no learner."
        }
    ), 404

@app.route('/quiz/create', methods=['POST'])
def create_quiz():
    data = request.get_json()
    # read data from the form and save in variable
    question = request.form['inputQn']
    # options = request.form['options']
    options = 'True', 'False'
    answer = request.form['correctAns']
    print(data)
    if ( request.get_json() is not None ): 
        quizCreation = Questions(**data)
        print(quizCreation)
        try:
            db.session.add(quizCreation)
            db.session.commit()
            return jsonify(quizCreation.to_dict()), 201
        except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 500
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True)