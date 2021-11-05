from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from QuizClass import Quiz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)
CORS(app)

class Questions(db.Model):
    __tablename__ = 'quizQuestions'

    quizID = db.Column(db.Integer, db.ForeignKey(Quiz.quizID), primary_key=True)
    qnNo = db.Column(db.Integer, nullable=False)
    question = db.Column(db.String(300), nullable=False)
    options = db.Column(db.String(100), nullable=False)
    answer = db.Column(db.String(50), nullable=False)

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

@app.route('/question-create', methods=['POST'])
def create_quiz():
    data = request.get_json()
    item = Questions(
        quizID=data['quizID'], qnNo=data['qnNo'], question=data['question'],
        options=data['options'], answer=data['answer']
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
    app.run(host='0.0.0.0', port=5013, debug=True)