from LessonClass import Lesson
from courseClass import Course

class Trainer:
    def __init__(self,courseName =  Course.courseName ):
        self.__courseName= courseName

    #def getClass(self):


    def getAssignedCourse(self, courseName):
        return self.__courseName
