from QuizClass import Quiz
from LessonClass import Lesson
from courseClass import Course


class Learner: 
    
    def __init__(self , badges, quizGrade = Quiz.quizGrade, courseName = Course.CourseName):
        self.__badges = badges
        self.__quizGrade = quizGrade
        self.__courseName = courseName

    def getQuizGrade(self):

            return self.__quizGrade

    def getEnrolledCourse(self):
            return self.__courseName
    
    #def getAppliedClass(self):
