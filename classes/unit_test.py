import unittest
from app import Classes,ClassList, Employee, Learner, Course


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
        
# Nicole - Course
class TestCourse(unittest.TestCase):
    def test_to_dict(self):
        c1 = Course(courseID=1, courseName='Repair 101', courseDesc="Learn how to repair things", courseDuration="3h")
        self.assertEqual(c1.to_dict(), {
            'courseID': 1,
            'courseName': 'Repair 101',
            'courseDesc': 'Learn how to repair things', 
            'courseDuration': '3h'}
        )

if __name__ == "__main__":
    unittest.main()