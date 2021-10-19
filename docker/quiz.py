from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

import requests

import os, sys
from os import environ

#from invokes import invoke_http
import json

import urllib.request
import mysql.connector

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

    # if ( request.get_json() is not None ):
    #     quizCreation = Questions(**data)
    #     print("h1")
    #     try:
    #         db.session.add(quizCreation)
    #         db.session.commit()
    #     except Exception as ex:
    #         db.session.rollback()
    #         return jsonify({"message": "An error occurred creating quiz."}), 500
    
    #     return jsonify(quizCreation.json()), 201

    # read data from the form and save in variable
    question = request.form['question']
    options = request.form['options']
    answer = request.form['answer']

    # store in database
    try:
        con = sql.connect('qa_database.db')
        c =  con.cursor() # cursor
        # insert data
        c.execute("INSERT INTO quizQuestions (question, options, answer) VALUES (?,?,?)",
            (question, options, answer))
        con.commit() # apply changes
        # go to thanks page
        return render_template('createThanks.html', question=question)
    except con.Error as err: # if error
        # then display the error in 'database_error.html' page
        return render_template('database_error.html', error=err)
    finally:
        con.close() # close the connection
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True)