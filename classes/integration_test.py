import flask_testing
import json
import datetime
from app import app, db, ClassList, Learner, Classes

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
