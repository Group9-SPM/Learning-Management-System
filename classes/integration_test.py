import unittest
import flask_testing
import json
import datetime
from app import app, db, Learner, Classes, EnrolmentList, Course, ClassList, Quiz, Questions, Lesson

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

#Nicole - TestClassList & TestAssignLearner
class TestClassList(TestApp):

    def test_classList_by_class(self):
        l1=Learner(badges="1", department="R&D", empID=2,
                        empName="Amy Tan", roleType="L", username="amy123")
        l2=Learner(department="R&D", empID=3, empName="Lucy Wong",
                        roleType="L", username="lucy123")
        c1=Classes(classID=1, courseID=1, endDate=datetime.datetime.now(),
                        endTime="13:00",  maxSlot=30, minSlot=10,
                        regEndDate=datetime.datetime.now(), regStartDate=datetime.datetime.now(),
                        size=30, startDate=datetime.datetime.now(), startTime="12:00", trainerID=4)
        cl1=ClassList(classID=c1.classID, learnerID=l1.empID)
        cl2=ClassList(classID=c1.classID, learnerID=l2.empID)
        db.session.add(l1)
        db.session.add(c1)
        db.session.add(l2)
        db.session.add(cl1)
        db.session.add(cl2)
        db.session.commit()

        response=self.client.get("/classList/1")
        self.assertEqual(response.json,
        {
                "data": [
                            {
                                "badges": "1",
                                "classID": 1,
                                "department": "R&D",
                                "empID": 2,
                                "empName": "Amy Tan",
                                "finalQuizGrade": None,
                                "learnerID": 2,
                                "roleType": "L",
                                "username": "amy123"
                            },
                            {
                                "badges": None,
                                "classID": 1,
                                "department": "R&D",
                                "empID": 3,
                                "empName": "Lucy Wong",
                                "finalQuizGrade": None,
                                "learnerID": 3,
                                "roleType": "L",
                                "username": "lucy123"
                            }
                        ]
        })

    def test_classList_by_learner(self):

        l1 = Learner(badges="1", department="R&D", empID=2,
                    empName="Amy Tan", roleType="L", username="amy123")
        c1 = Classes(classID=1, courseID=1, endDate=datetime.datetime.now(),
                    endTime="13:00",  maxSlot=30, minSlot=10,
                    regEndDate=datetime.datetime.now(), regStartDate=datetime.datetime.now(),
                    size=30, startDate=datetime.datetime.now(), startTime="12:00", trainerID=4)
        cl1 = ClassList(classID=c1.classID, learnerID=l1.empID, finalQuizGrade=None)
        db.session.add(l1)
        db.session.add(c1)
        db.session.add(cl1)
        db.session.commit()

        response = self.client.get("/classList/learner/2")
        self.assertEqual(response.json,
                        {
                            "data": [
                                {
                                "classID": 1,
                                "finalQuizGrade": None,
                                "learnerID": 2
                                }
                            ]
                        })

class TestAssignLearner(TestApp):

    def test_assign_learner(self):
        l1 = Learner(badges="1", department="R&D", empID=2,
                    empName="Amy Tan", roleType="L", username="amy123")

        c1 = Classes(classID=1,courseID=1, endDate=datetime.datetime.now(),
                    endTime="13:00",  maxSlot=30, minSlot=10,
                    regEndDate=datetime.datetime.now(), regStartDate=datetime.datetime.now(),
                    size=30, startDate=datetime.datetime.now(), startTime="12:00", trainerID=4)

        db.session.add(l1)
        db.session.add(c1)
        db.session.commit()

        request_body = [{
                            'learnerID': l1.empID,
                            'classID': c1.classID
                        }]

        response = self.client.post("/classList",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json,
                        {
                                "data" : [2],
                                "message" : "All learners assigned successfully"
                        })


# Amanda - TestCreateEnrolment 
class TestCreateEnrolment(TestApp):
    def test_create_enrolment(self):
        e1 = EnrolmentList(classID=8, learnerID=4,
                    courseID=4, enrolmentStatus='pending')
        
        co1 = Course(courseID='4',courseName='Repair Words 101',
                    courseDesc ='Learn how to speak repair words', courseDuration='1h')

        c1 = Classes(classID=8,courseID=4, endDate=datetime.datetime.now(),
                    endTime="13:00",  maxSlot=30, minSlot=10,
                    regEndDate=datetime.datetime.now(), regStartDate=datetime.datetime.now(),
                    size=30, startDate=datetime.datetime.now(), startTime="12:00", trainerID=4,courseName='Repair Words 101',
                    courseDesc ='Learn how to speak repair words', courseDuration='1h',empName='Emma', department='HR', username ="emma65", roleType="L")

        l1 = Learner (empID='4', badges='3', empName='Emma', department='HR', username ="emma65", roleType="L")

        db.session.add(e1)
        db.session.add(c1)
        db.session.add(co1)
        db.session.add(l1)
        db.session.commit()

        request_body = {
            'classID': c1.classID,
            'learnerID': l1.empID,
            'courseID': co1.courseID,
            'enrolmentStatus': 'pending'
        }

        response = self.client.post("/enrolmentList",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
            'classID': 8,
            'learnerID': 4,
            'courseID': 4,
            'enrolmentStatus': 'pending'
        })

 
    def test_create_enrolment_invalidClassSize(self):
        e1 = EnrolmentList(classID=8, learnerID=4,
                    courseID=4, enrolmentStatus='pending')
        
        co1 = Course(courseID='4',courseName='Repair Words 101',
                    courseDesc ='Learn how to speak repair words', courseDuration='1h')

        c1 = Classes(classID=8,courseID=4, endDate=datetime.datetime.now(),
                    endTime="13:00",  maxSlot=30, minSlot=30,
                    regEndDate=datetime.datetime.now(), regStartDate=datetime.datetime.now(),
                    size=30, startDate=datetime.datetime.now(), startTime="12:00", trainerID=4,courseName='Repair Words 101',
                    courseDesc ='Learn how to speak repair words', courseDuration='1h',empName='Lily', department='Production', username ="Lily65", roleType="T")

        l1 = Learner (empID='4', badges='3', empName='Emma', department='HR', username ="emma65", roleType="L")
        
        db.session.add(e1)
        db.session.add(c1)
        db.session.add(co1)
        db.session.add(l1)
        db.session.commit()

        request_body = {
            'classID': c1.classID,
            'learnerID': l1.empID,
            'courseID': co1.courseID,
            'enrolmentStatus': 'pending'
        }

        response = self.client.post("/enrolmentList",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {
            'message': 'Class is full.'
        })

# Diyanah - TestCreateQuiz and TestCreateQuestion
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

    def test_create_quiz_invalid_lesson(self):
        lesson = Lesson(lessonNum='10',
                    classID=1, courseID=5, lessonName='Fixing Printers', lessonDesc='How to fix printers')
        quiz = Quiz(quizDuration='10',
                    passingCriteria='5', quizType='UG', lessonID=2)
        db.session.add(lesson)
        db.session.commit()

        request_body = {
            'quizID': quiz.quizID,
            'quizDuration': quiz.quizDuration,
            'passingCriteria': quiz.passingCriteria,
            'quizType': quiz.quizType,
            'lessonID': quiz.lessonID
        }

        response = self.client.post("/quiz-create",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {
            'message': 'Unable to commit to database.'
        }) 
class TestCreateQuestion(TestApp):
    def test_create_quiz_question(self):
        qns = Questions(questionsID=1, quizID=10, qnNo=1,
                     question='You are great today.', options='True,False', answer='True')

        request_body = {
            'questionsID': qns.questionsID,
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
            'questionsID': 1,
            'quizID': 10,
            'qnNo': 1,
            'question': 'You are great today.',
            'options': 'True,False',
            'answer': 'True'
        })

if __name__ == '__main__':
    unittest.main()
