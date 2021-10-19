class Quiz():
     
    def __init__(self, quizID, passingCriteria, quizType):
        self.__quizID = quizID
        self.__passingCriteria = passingCriteria
        self.__quizType = quizType

    def getQuizID(self):
        return self.__quizID
    def getQuizDuration(self):
        return self.__quizDuration
    def getPassingCriteria(self):
        return self.__passingCriteria
    def getQuizType(self):
        return self.__quizType
