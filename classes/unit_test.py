import unittest
from app import Employee, Learner, Course, Quiz, Questions, EnrolmentList, Classes, ClassList, LessonMaterialsViewed, QuizAttempt


#amanda - Employee & Learner
class TestEmployee(unittest.TestCase):

    def test_to_dict(self):
        e1 = Employee(empID='1',empName='Emma', department='HR', username="emma65", roleType="L")
        self.assertEqual(e1.to_dict(), {
            'empID': '1',
            'empName': 'Emma',
            'department': 'HR',
            "username": "emma65",
            "roleType":"L"}
        )

class TestLearner(unittest.TestCase):

    def test_to_dict(self):
        l1 = Learner(empID='1', badges='3', empName='Emma', department='HR', username="emma65", roleType="L")
        self.assertEqual(l1.to_dict(), {
            'empID': '1',
            'badges': '3',
            'empName': 'Emma',
            'department': 'HR',
            "username": "emma65",
            "roleType":"L"}
        )
        
# Nicole - Course and EnrolmentList
class TestCourse(unittest.TestCase):

    def test_to_dict(self):
        c1 = Course(courseID=1, courseName='Repair 101', courseDesc="Learn how to repair things", courseDuration="3h")
        self.assertEqual(c1.to_dict(), {
            'courseID': 1,
            'courseName': 'Repair 101',
            'courseDesc': 'Learn how to repair things', 
            'courseDuration': '3h'}
        )

class TestEnrolmentList(unittest.TestCase):

    def test_to_dict(self):
        el1 = EnrolmentList(courseID=1, learnerID=1, classID=1, enrolmentStatus="Pending")
        self.assertEqual(el1.to_dict(), {
            'courseID': 1,
            'learnerID': 1,
            'classID': 1, 
            'enrolmentStatus': 'Pending'}
        )

class TestLesson(unittest.TestCase):
    def test_to_dict(self):
        l1 = Lesson(lessonID='1', lessonNum='1', classID='1', courseID='1', lessonName ="Fixing Scanner", lessonDesc="How to fix scanner.")
        self.assertEqual(l1.to_dict(), {
            'lessonID': '1',
            'lessonNum': '1', 
            'classID': '1',
            'courseID': '1',
            "lessonName": "Fixing Scanner",
            "lessonDesc": "How to fix scanner."}
        )

# Diyanah - Quiz and Questions
class TestQuiz(unittest.TestCase):

    def test_to_dict(self):
        q1 = Quiz(quizID='4', quizDuration='20', passingCriteria='6', quizType='UG', lessonID="2")
        self.assertEqual(q1.to_dict(), {
            'quizID': '4',
            'quizDuration': '20',
            'passingCriteria': '6',
            'quizType': 'UG',
            "lessonID": "2"}
        )

class TestQuestion(unittest.TestCase):
    def test_to_dict(self):
        q1 = Questions(questionsID='1', quizID='1', qnNo='1', question='SPM is difficult.', options='True,False', answer="True")
        self.assertEqual(q1.to_dict(), {
            'questionsID': '1',
            'quizID': '1',
            'qnNo': '1',
            'question': 'SPM is difficult.',
            'options': 'True,False',
            "answer": "True"}
        )

# Mei Fang - Classes, ClassList, LessonMaterialsViewed and QuizAttempt
class TestClasses(unittest.TestCase):
    def test_to_dict(self):
        cls1 = Classes(classID=1, startDate='2021-05-21', endDate='2021-11-19',size=25, startTime='07:00', endTime='12:00', minSlot=10, maxSlot=25, regStartDate='2021-04-01', regEndDate='2021-05-01', courseID=1, trainerID=1)
        self.assertEqual(cls1.to_dict(), {
            'classID': 1,
            'startDate': '2021-05-21',
            'endDate': '2021-11-19',
            'size': 25,
            "startTime": '07:00',
            "endTime": '12:00',
            "minSlot": 10,
            "maxSlot": 25,
            "regStartDate": '2021-04-01',
            "regEndDate": '2021-05-01',
            "courseID": 1,
            "trainerID": 1}
        )

class TestClassList(unittest.TestCase):
    def test_to_dict(self):
        cl1 = ClassList(classID=1, learnerID=1, finalQuizGrade='A')
        self.assertEqual(cl1.to_dict(), {
            'classID': 1,
            'learnerID': 1,
            'finalQuizGrade': 'A'}
        )

class TestLessonMaterialsViewed(unittest.TestCase):
    def test_to_dict(self):
        lmv1 = LessonMaterialsViewed(materialID=1, learnerID=1, lessonID=1, completed=False)
        self.assertEqual(lmv1.to_dict(), {
            'materialID': 1,
            'learnerID': 1,
            'lessonID': 1,
            'completed': False}
        )

class TestQuizAttempt(unittest.TestCase):
    def test_to_dict(self):
        qa1 = QuizAttempt(quizAttemptID=1, quizID=1, learnerID=1, score=3, max_score=5)
        self.assertEqual(qa1.to_dict(), {
            'quizAttemptID': 1,
            'quizID': 1,
            'learnerID': 1,
            'score': 3,
            'max_score': 5}
        )

if __name__ == "__main__":
    unittest.main()