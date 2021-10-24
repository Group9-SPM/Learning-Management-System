from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from quizClass import Quiz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)
CORS(app)

class Questions(db.Model):
    __tablename__ = 'quizQuestions'

    quizID = db.Column(db.Integer, db.ForeignKey('quiz.quizID'), primary_key=True)
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

@app.route("/question/<int:quizID>")
def quizQuestions(quizID):
    quizQuestions = Questions.query.filter_by(quizID=quizID)
    if quizQuestions:
        return jsonify({
            "data": [quizQuestions.to_dict()
                     for quizQuestions in quizQuestions]
        }), 200
    else:
        return jsonify({
            "message": "No questions found."
        }), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True)