import unittest
from app import Classes,ClassList, Employee, Learner, Quiz, Questions


#amanda - Employee & Learner
class TestEmployee(unittest.TestCase):
    def test_to_dict(self):
        e1 = Employee(empID='1',empName='Emma', department='HR', username ="emma65", roleType="L")
        self.assertEqual(e1.to_dict(), {
            'empID': '1',
            'empName': 'Emma',
            'department': 'HR',
            "username": "emma65",
            "roleType":"L"}
        )

class TestLearner(unittest.TestCase):
    def test_to_dict(self):
        l1 = Learner(empID='1', badges='3', empName='Emma', department='HR', username ="emma65", roleType="L")
        self.assertEqual(l1.to_dict(), {
            'empID': '1',
            'badges': '3', 
            'empName': 'Emma',
            'department': 'HR',
            "username": "emma65",
            "roleType":"L"}
        )

class TestQuiz(unittest.TestCase):
    def test_to_dict(self):
        q1 = Quiz(quizID='4', quizDuration='20', passingCriteria='6', quizType='UG', lessonID ="2")
        self.assertEqual(q1.to_dict(), {
            'quizID': '4',
            'quizDuration': '20', 
            'passingCriteria': '6',
            'quizType': 'UG',
            "lessonID": "2"}
        )

class TestQuestion(unittest.TestCase):
    def test_to_dict(self):
        q1 = Questions(quizID='1', qnNo='1', question='SPM is difficult.', options='True,False', answer ="True")
        self.assertEqual(q1.to_dict(), {
            'quizID': '4',
            'qnNo': '1', 
            'question': 'SPM is difficult.',
            'options': 'True,False',
            "answer": "True"}
        )

if __name__ == "__main__":
    unittest.main()