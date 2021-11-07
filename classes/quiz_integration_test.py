import unittest
import flask_testing
import json
from app import app, db, ClassList, EnrolmentList, Quiz, Questions

class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestCreateQuiz(TestApp):
    def test_create_quiz(self):
        quiz = Quiz(quizDuration='10',
                    passingCriteria='5', quizType='UG', lessonID=1)

        request_body = {
            'quizDuration': quiz.quizDuration,
            'passingCriteria': quiz.passingCriteria,
            'quizType': quiz.quizType,
            'lessonID': quiz.lessonID
        }

        response = self.client.post("/quiz-create",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
            'quizID': 1,
            'quizDuration': '10',
            'passingCriteria': '5',
            'quizType': 'UG',
            'lessonID': 1
        })
        
    def test_create_quiz_question(self):
        qns = Questions(quizID=10, qnNo=1,
                     question='You are great today.', options='True,False', answer='True')

        request_body = {
            'quizID': qns.quizID,
            'qnNo': qns.qnNo,
            'question': qns.question,
            'options': qns.options,
            'answer': qns.answer
        }

        response = self.client.post("/question-create",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
            'quizID': 10,
            'qnNo': 1,
            'question': 'You are great today.',
            'options': 'True,False',
            'answer': 'True'
        })

if __name__ == '__main__':
    unittest.main()
