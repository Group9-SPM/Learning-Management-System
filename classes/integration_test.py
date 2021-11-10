import unittest
import flask_testing
import json
import datetime
from app import app, db, ClassList, Learner, Classes, EnrolmentList, Course, Quiz, Questions, Lesson, LessonMaterials, LessonMaterialsViewed, QuizAttempt


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

    def test_assign_learner_within_class_size(self):
        l1 = Learner(badges="1", department="R&D", empID=2,
                    empName="Amy Tan", roleType="L", username="amy123")

        c1 = Classes(classID=1,courseID=1, endDate=datetime.datetime.now(),
                    endTime="13:00", maxSlot=30, minSlot=10,
                    regEndDate=datetime.datetime.now(), regStartDate=datetime.datetime.now(),
                    size=29, startDate=datetime.datetime.now(), startTime="12:00", trainerID=4)

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

    def test_assign_learner_exceeding_class_size(self):
        l1 = Learner(badges="1", department="R&D", empID=2,
                    empName="Amy Tan", roleType="L", username="amy123")

        c1 = Classes(classID=1,courseID=1, endDate=datetime.datetime.now(),
                    endTime="13:00", maxSlot=30, minSlot=10,
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
                                "data" : [{
                                    'learnerID': 2,
                                    'classID': 1
                                }],
                                "message" : "Class size is exceeded. Failed to assign learners."
                        })


# Amanda - TestCreateEnrolment & TestEnrolmentList
class TestCreateEnrolment(TestApp):
    def test_create_enrolment(self):
        
        co1 = Course(courseName='Repair Words 101',
                    courseDesc ='Learn how to speak repair words', courseDuration='1h')

        c1 = Classes(courseID=1, endDate=datetime.datetime.now(),
                    endTime="13:00",  maxSlot=30, minSlot=10,
                    regEndDate=datetime.datetime.now(), regStartDate=datetime.datetime.now(),
                    size=30, startDate=datetime.datetime.now(), startTime="12:00", trainerID=4)

        l1 = Learner (empID=4, badges='3', empName='Emma', department='HR', username ="emma65", roleType="L")

        e1 = EnrolmentList(classID=8, learnerID=4,
                    courseID=4, enrolmentStatus='Pending')

        db.session.add(c1)
        db.session.add(co1)
        db.session.add(l1)
        db.session.add(e1)
        db.session.commit()

        request_body = {
            'classID': c1.classID,
            'learnerID': l1.empID,
            'courseID': co1.courseID,
            'enrolmentStatus': 'Pending'
        }

        response = self.client.post("/enrolmentList",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
            'classID': 1,
            'learnerID': 4,
            'courseID': 1,
            'enrolmentStatus': 'Pending'
        })

class TestEnrolmentList(TestApp):
    def test_enrolmentList_by_learnerID(self):

        co1 = Course(courseID = 1, courseName='Repair Words 101',
                    courseDesc ='Learn how to speak repair words', courseDuration='1h')


        co2 = Course(courseID = 2,courseName='Repair 101',
                     courseDesc ='Learn how to repair words', courseDuration='3h')        


        c1 = Classes(classID=1 , courseID=1, endDate=datetime.datetime.now(),
                    endTime="13:00",  maxSlot=30, minSlot=10,
                    regEndDate=datetime.datetime.now(), regStartDate=datetime.datetime.now(),
                    size=30, startDate=datetime.datetime.now(), startTime="12:00", trainerID=4)
        
        c2 = Classes(classID=3 , courseID=2, endDate=datetime.datetime.now(),
                    endTime="13:00",  maxSlot=30, minSlot=10,
                    regEndDate=datetime.datetime.now(), regStartDate=datetime.datetime.now(),
                    size=30, startDate=datetime.datetime.now(), startTime="12:00", trainerID=4)

        l1 = Learner (empID=1, badges='3', empName='Emma', department='HR', username ="emma65", roleType="L")

        e1 = EnrolmentList(classID=c1.classID, learnerID=l1.empID,
                    courseID=co1.courseID, enrolmentStatus='Successful')

        e2 = EnrolmentList(classID=c2.classID, learnerID=l1.empID,
                    courseID=co2.courseID, enrolmentStatus='Pending')

        db.session.add(co1)
        db.session.add(co2)
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(l1)
        db.session.add(e1)
        db.session.add(e2)
        db.session.commit()

        response=self.client.get("/enrolmentList/1")
        self.assertEqual(response.json,
        {
                "data": [
                            {
                                "classID":1,
                                "learnerID":1,
                                "courseID":1,
                                "enrolmentStatus":"Successful"
                            },
                            {
                                "classID":3,
                                "learnerID":1,
                                "courseID":2,
                                "enrolmentStatus":"Pending"
                            }
                        ]
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

# Mei Fang - TestLesson, TestLessonMaterials, TestLessonMaterialsViewed, TestQuizAttempt
class TestLesson(TestApp):
    def test__lesson_by_num(self):
        co1 = Course(courseID=4,courseName='Repair Words 101',
            courseDesc ='Learn how to speak repair words', courseDuration='10mins')
        c1=Classes(classID=1, courseID=co1.courseID, endDate=datetime.datetime.now(),
                        endTime="13:00",  maxSlot=30, minSlot=10,
                        regEndDate=datetime.datetime.now(), regStartDate=datetime.datetime.now(),
                        size=30, startDate=datetime.datetime.now(), startTime="12:00", trainerID=4)
        l1=Lesson(lessonID=1, lessonNum=1, classID=c1.classID, courseID=co1.courseID, lessonName='Basic English', lessonDesc='Basic English words.')

        db.session.add(co1)
        db.session.add(c1)
        db.session.add(l1)
        db.session.commit()

        response = self.client.get("/lesson/1/1/4")
        self.assertEqual(response.json,
                        {
                            "data":
                                {
                                "lessonID": 1,
                                "lessonNum": 1,
                                "classID": 1,
                                "courseID": 4,
                                "lessonName":'Basic English',
                                "lessonDesc":'Basic English words.'
                                }
                        })

    def test__lesson_by_class(self):
        co1 = Course(courseID=4,courseName='Repair Words 101',
            courseDesc ='Learn how to speak repair words', courseDuration='10mins')
        c1=Classes(classID=1, courseID=co1.courseID, endDate=datetime.datetime.now(),
                        endTime="13:00",  maxSlot=30, minSlot=10,
                        regEndDate=datetime.datetime.now(), regStartDate=datetime.datetime.now(),
                        size=30, startDate=datetime.datetime.now(), startTime="12:00", trainerID=4)
        l1=Lesson(lessonID=1, lessonNum=1, classID=c1.classID, courseID=co1.courseID, lessonName='Basic English', lessonDesc='Basic English words.')

        db.session.add(co1)
        db.session.add(c1)
        db.session.add(l1)
        db.session.commit()

        response = self.client.get("/lesson/1/4")
        self.assertEqual(response.json,
                        {
                            "data":[
                                {
                                "lessonID": 1,
                                "lessonNum": 1,
                                "classID": 1,
                                "courseID": 4,
                                "lessonName":'Basic English',
                                "lessonDesc":'Basic English words.'
                                }
                            ]
                        })

    def test__lesson_by_lessonID(self):
        ln1=Lesson(lessonID=1, lessonNum=1, classID=1, courseID=4, lessonName='Basic English', lessonDesc='Basic English words.')
        l1 = Learner(empID=1, badges=3, empName='Emma', department='HR', username ="emma65", roleType="L")
        lmv1 = LessonMaterialsViewed(materialID=1, learnerID=l1.empID, lessonID=ln1.lessonID, completed=False)
        q1 = Quiz(quizID=1, quizDuration='10', passingCriteria='5', quizType='UG', lessonID=1)
        qa1 = QuizAttempt(quizAttemptID=1, quizID=q1.quizID, learnerID=l1.empID, score=3, max_score=5)

        db.session.add(ln1)
        db.session.add(l1)
        db.session.add(lmv1)
        db.session.add(q1)
        db.session.add(qa1)
        db.session.commit()

        response = self.client.get("/lesson/lessonByID/1/1")
        self.assertEqual(response.json,
                        {
                            "data": {
                                "lessonID": 1,
                                "lessonNum": 1,
                                "classID": 1,
                                "courseID": 4,
                                "lessonName":'Basic English',
                                "lessonDesc":'Basic English words.'
                                },
                            "quiz_attempts": True,
                            "quiz_available": True
                        })

class TestLessonMaterials(TestApp):
    def test__lessonMaterials_by_lesson(self):
        ln1=Lesson(lessonID=1, lessonNum=1, classID=1, courseID=4, lessonName='Basic English', lessonDesc='Basic English words.')
        lm1 = LessonMaterials(materialID=1, materialURL="https://drive.google.com/file/d/1tbOmz0GipcX-_c2oXj4MnzZNodiN85x-/view?usp=sharing", content='Basic_1.pdf', lessonID=ln1.lessonID)
        qa1 = QuizAttempt(quizAttemptID=1, quizID=1, learnerID=1, score=3, max_score=5)

        db.session.add(ln1)
        db.session.add(lm1)
        db.session.add(qa1)
        db.session.commit()

        response = self.client.get("/lessonMaterials/1/1")
        self.assertEqual(response.json,
                        {
                            "data": [
                                {
                                "materialID": 1,
                                "materialURL": "https://drive.google.com/file/d/1tbOmz0GipcX-_c2oXj4MnzZNodiN85x-/view?usp=sharing",
                                "content":'Basic_1.pdf',
                                "lessonID": 1
                                }
                            ]
                        })

class TestLessonMaterialsViewed(TestApp):
    def test__lessonMaterialsViewed_by_lesson_material(self):
        lmv1 = LessonMaterialsViewed(materialID=1, learnerID=1, lessonID=1, completed=False)
        q1 = Quiz(quizID=1, quizDuration='10', passingCriteria='5', quizType='UG', lessonID=lmv1.lessonID)
        qa1 = QuizAttempt(quizAttemptID=1, quizID=q1.quizID, learnerID=lmv1.learnerID, score=3, max_score=5)

        db.session.add(lmv1)
        db.session.add(q1)
        db.session.add(qa1)
        db.session.commit()

        response = self.client.get("/lessonMaterialsViewed/check/1/1/1")
        self.assertEqual(response.json,
                        {
                            "data":
                                {
                                "materialID": 1,
                                "learnerID": 1,
                                "lessonID": 1, 
                                "completed": False
                                },
                            "status": "success"
                        })

    def test_lessonMaterialsViewed_add_by_lesson_material(self):
        lmv1 = LessonMaterialsViewed(materialID=1, learnerID=1, lessonID=1, completed=False)

        db.session.add(lmv1)
        db.session.commit()

        response = self.client.get("/lessonMaterialsViewed/add/1/1/1")

        self.assertEqual(response.json, {
            'message': "Lesson Material already viewed."
        })

    def test_lessonMaterialsViewed_update_by_lesson_material(self):
        lmv1 = LessonMaterialsViewed(materialID=1, learnerID=1, lessonID=1, completed=False)

        db.session.add(lmv1)
        db.session.commit()

        response = self.client.get("/lessonMaterialsViewed/update/1/1/1")

        self.assertEqual(response.json, {
            'message': "Updated Completed."
        })

class TestQuizAttempt(TestApp):
    def test_retrieveQuizAttempts(self):
        q1 = Quiz(quizID=1, quizDuration='10', passingCriteria='5', quizType='UG', lessonID=1)
        qa1 = QuizAttempt(quizAttemptID=1, quizID=q1.quizID, learnerID=1, score=3, max_score=5)

        db.session.add(q1)
        db.session.add(qa1)
        db.session.commit()

        response = self.client.get("/quizAttempts/check/1/1")
        self.assertEqual(response.json,
                        {
                            "data": [
                                {
                                "quizAttemptID": 1,
                                "quizID": 1, 
                                "learnerID": 1,
                                "score": 3, 
                                "max_score": 5
                                }
                            ]
                        })

    def test_submit_quiz(self):
        qn1 = Questions(questionsID=1, quizID=1, qnNo=1, question='You had a great day', options='True,False', answer='True')
        qa1 = QuizAttempt(quizID=qn1.quizID, learnerID=1, score=1, max_score=1)

        db.session.add(qn1)
        db.session.add(qa1)
        db.session.commit()

        request_body = {
                            "quiz_id": qn1.quizID,
                            'learner_id': qa1.learnerID,
                            'lesson_id': 1,
                            'qn_1': 'True'
                        }

        response = self.client.post("/submitQuiz",
                                    data=request_body,
                                    content_type='multipart/form-data')
        self.assertEqual(response.json,
                        {       
                            "quizAttemptID": 2,
                            "quizID" : 1,
                            "learnerID" : 1,
                            "score": 1,
                            "max_score": 1
                        })


if __name__ == '__main__':
    unittest.main()
